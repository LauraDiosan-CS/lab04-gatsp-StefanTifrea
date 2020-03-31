def get_cycle_fitness(cycle, network):

    s = 0
    cities = network["matrix"]
    # print(cities)
    for i in range(network["number_of_cities"] - 1):
        nodeA = cycle[i]
        nodeB = cycle[i+1]
        # print(nodeA)
        # print(nodeB)
        s += cities[nodeA][nodeB]

    return s + cities[cycle[network["number_of_cities"] - 1]][cycle[0]]



