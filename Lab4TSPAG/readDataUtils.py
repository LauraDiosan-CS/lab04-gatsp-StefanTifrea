import tsplib95 as tsp
import networkx as nx


def read_matrix_network(path):
    network = {}
    f = open(path, "r")
    network["number_of_cities"] = int(f.readline())

    cities = []
    for i in range(network["number_of_cities"]):
        cities.append([])

    for i in range(network["number_of_cities"]):
        distances = f.readline().split(",")
        for x in distances:
            cities[i].append(int(x))
    network["matrix"] = cities

    return network


def read_tsp_network(path):
    network = {}
    graph = tsp.load_problem(path).get_graph()
    network["number_of_cities"] = len(graph.nodes())
    network["matrix"] = nx.to_numpy_matrix(graph)

    return network


def read_matrix_network_space(path):
    network = {}
    f = open(path, "r")
    network["number_of_cities"] = int(f.readline())

    cities = []
    for i in range(network["number_of_cities"]):
        cities.append([])

    for i in range(network["number_of_cities"]):
        distances = f.readline().split()
        for x in distances:
            cities[i].append(int(x))
    network["matrix"] = cities

    return network