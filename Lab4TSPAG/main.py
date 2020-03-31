from domain.ga import GA
from utils.fitnessUtils import get_cycle_fitness
from utils.readDataUtils import read_matrix_network, read_tsp_network, read_matrix_network_space
import networkx as nx
import matplotlib.pyplot as plots

def plot_network(network, communities):

    pos = nx.spring_layout(network)  # compute graph layout
    plots.figure(figsize=(10, 10))  # image is 8 x 8 inches
    nx.draw_networkx_nodes(network, pos, node_size=600, node_color=communities)
    nx.draw_networkx_edges(network, pos, alpha=0.3)
    plots.show()


def algorithm(graph):

    best_fitness = 999999999999
    solution = []
    ga_parameters = {"population": 100, "generations": 100, "graph": graph, "function": get_cycle_fitness}
    chromosome_parameters = {"number_of_cities": graph["number_of_cities"], "function": get_cycle_fitness, "mutation_chance": 0.8}

    ga = GA(ga_parameters, chromosome_parameters)
    ga.initialisation()
    ga.evaluation()

    lengths = [ga.bestChromosome().fitness]

    for gen in range(ga_parameters["generations"]):
        print("Gen: " + str(gen))
        current_fitness = ga.bestChromosome().fitness
        current_representation = ga.bestChromosome().repres
        lengths.append(current_fitness)
        if current_fitness < best_fitness:
            best_fitness = current_fitness
            solution = current_representation

        print(solution)
        print("Current fitness: " + str(current_fitness))
        ga.oneGenerationElitism()

    print("Ending solution: " + str(solution))
    print("Final fitness: " + str(best_fitness))
    plots.plot(lengths)
    plots.show()

def run():

    while True:
        print("1 - Easy\n"
              "2 - Medium\n"
              "3 - Hard\n"
              "4 - Berlin\n"
              "0 - Exit\n")
        command = input("Choose: ")

        if command == "0":
            return

        if command == "1":
            algorithm(read_matrix_network("data/easy_tsp.txt"))

        if command == "2":
            algorithm(read_matrix_network_space("data/medium_tsp.txt"))

        if command == "3":
            # algorithm(read_tsp_network("data/hard_tsp.txt"))
            algorithm(read_matrix_network_space("data/hard_tsp.txt"))

        if command == "4":
            algorithm(read_tsp_network("data/berlin.txt"))

run()
