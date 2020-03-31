from random import randint, sample

from domain.chromosome import Chromosome


class GA:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['population']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, self.__param["graph"])

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def worstChromosome(self):
        worst = self.__population[0]
        for c in self.__population:
            if c.fitness > worst.fitness:
                worst = c
        return worst

    def selection(self):
        '''
        pos1 = randint(0, self.__param['population'] - 1)
        pos2 = randint(0, self.__param['population'] - 1)
        if self.__population[pos1].fitness < self.__population[pos2].fitness:
            return pos1
        else:
            return pos2
        '''
        k = randint(self.__param['population']//2, self.__param['population'] - 1)
        positions = sample(range(0, self.__param['population'] - 1), k)
        best_position = positions[0]
        best_fitness = self.__population[positions[0]].fitness

        for poz in positions:
            if self.__population[poz].fitness < best_fitness:
                best_fitness = self.__population[poz].fitness
                best_position = poz

        return best_position


    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['population']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['population'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        for _ in range(self.__param['population']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParam['function'](off.repres,self.__param["graph"])
            worst = self.worstChromosome()
            if off.fitness < worst.fitness:
                worst = off
