from random import randint

from utils.permutationUtils import generate_random_permutation, generate_new_value


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = generate_random_permutation(self.__problParam["number_of_cities"])
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        # order XO
        pos1 = randint(-1, self.__problParam["number_of_cities"] - 1)
        pos2 = randint(-1, self.__problParam["number_of_cities"] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if el not in newrepres:
                if len(newrepres) < self.__problParam["number_of_cities"] - pos1:
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring

    def swap_mutation(self):
        # insert mutation
        '''
        pos1 = randint(0, self.__problParam["number_of_cities"] - 1)
        pos2 = randint(0, self.__problParam["number_of_cities"] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)
        '''
        pos1 = randint(0, len(self.__repres) - 1)
        pos2 = pos1

        while pos2 == pos1:
            pos2 = randint(0, len(self.__repres) - 1)

        self.__repres[pos1], self.__repres[pos2] = self.__repres[pos2], self.__repres[pos1]

    def mutation(self):
        chance = generate_new_value(0,1)
        if self.__problParam["mutation_chance"] <= chance:
            self.swap_mutation()


    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness