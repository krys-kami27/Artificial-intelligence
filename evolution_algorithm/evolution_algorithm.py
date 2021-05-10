import random
import matplotlib.pyplot as plt
import time


def full_graph():
    # makes full graph
    places = {place: [num for num in range(1, 26)] for place in range(1, 26)}
    for x in range(1, 26):
        places[x].remove(x)
    return places


def random_graph():
    # makes random graph which have
    # 50% connections of full graph
    places = {place: [] for place in range(1, 26)}
    streets = 0
    while streets < 150:
        pair = random.sample(range(1, 26), 2)
        if pair[0] not in places[pair[1]]:
            places[pair[0]].append(pair[1])
            places[pair[1]].append(pair[0])
            streets += 1
    return places


def population_mark(graph, population_n):
    # function returns values of every creature
    marks = []
    for creature in population_n:
        mark = []
        for place in creature:
            for element in graph[place]:
                if [place, element] not in mark and [element, place] not in mark:
                    mark.append([place, element])
        marks.append(len(mark))
    return marks


def find_best(values, population_n):
    # return optimum from actual population
    index = values.index(max(values))
    creature = population_n[index]
    max_value = max(values)
    return [max_value, creature]


def selection(value, population_n):
    # selection of actual population

    # tournment involve constant=2 organism
    population_next = []
    for _ in range(len(population_n)):
        tournament = random.sample(range(len(population_n)), 2)
        if value[tournament[0]] >= value[tournament[1]]:
            population_next.append(population_n[tournament[0]])
        else:
            population_next.append(population_n[tournament[1]])
    return population_next


def mutation(population, graph, p_mut):
    # makes possible mutations on creatures
    for creature in range(len(population)):
        for place in range(len(population[0])):
            result = random.randint(1, 100)
            if result in range(1, int(100 * p_mut)):
                posiblities = random.choice(graph[population[creature][place]])
                population[creature][place] = posiblities
    return population


def evolution_algorithm(graph, population_0, t_max, p_mut):
    population_n = population_0
    t = 0
    value = population_mark(graph, population_n)
    najlepszy = find_best(value, population_n)
    while t < t_max:
        sel = selection(value, population_n)
        mut = mutation(sel, graph, p_mut)
        # print(mut)
        value = population_mark(graph, mut)
        najlepszy_pokolenie = find_best(value, mut)
        if najlepszy_pokolenie[0] > najlepszy[0]:
            najlepszy[0] = najlepszy_pokolenie[0]
            najlepszy[1] = najlepszy_pokolenie[1]
        population_n = mut
        t += 1
    return najlepszy


def main():
    maximum = []
    times = []
    population_size = 100
    # time test and population size
    for x in range(1, population_size):
        timer = time.time()
        P_0 = [random.sample(range(1, 26), 8) for _ in range(1+x)]
        # mutation probability = 0.1
        # maximum iterations = 10
        # population have x creatures
        optimum = evolution_algorithm(random_graph(), P_0, 10, 0.1)
        maximum.append(optimum[0])
        times.append(time.time() - timer)
    plt.stem([x for x in range(1, population_size)], maximum, 'o')
    plt.xlabel('Range of population')
    plt.ylabel('Maximumthe largest street coverage')
    plt.show()
    plt.stem([x for x in range(1, population_size)], times, 'o')
    plt.xlabel('Range of population')
    plt.ylabel('Execution time')
    plt.show()
    print(sum(maximum)/len(maximum))
    print(sum(times)/len(times))

    # number iterations test
    maximum = []
    # time test and population size
    for x in range(1, 100):
        P_0 = [random.sample(range(1, 26), 2) for _ in range(2)]
        # mutation probability = 0.1
        optimum = evolution_algorithm(random_graph(), P_0, x, 0.5)
        maximum.append(optimum[0])
    plt.stem([x for x in range(1, 100)], maximum, 'o')
    plt.xlabel('Number of iterations')
    plt.ylabel('Maximumthe largest street coverage')
    plt.show()
    print(sum(maximum)/len(maximum))

    # mutation probability test
    maximum = []
    for x in range(1, 100):
        P_0 = [random.sample(range(1, 26), 2) for _ in range(2)]
        # maximum iterations = 10
        optimum = evolution_algorithm(random_graph(), P_0, 10, 0.01 * x)
        maximum.append(optimum[0])
    plt.stem([x for x in range(1, 100)], maximum, 'o')
    plt.xlabel('Probability of mutation in %')
    plt.ylabel('Maximumthe largest street coverage')
    plt.show()
    print(sum(maximum)/len(maximum))

    #  maxiumum for all numbers of policemans
    maximum = []
    for x in range(1, 26):
        P_0 = [random.sample(range(1, 26), x) for _ in range(10)]
        # mutation probability = 0.1
        # maximum iterations = 10
        # population have 10 creatures
        optimum = evolution_algorithm(random_graph(), P_0, 10, 0.1)
        maximum.append(optimum[0])
    plt.stem([x for x in range(1, 26)], maximum, 'o')
    plt.xlabel('Number of policemans')
    plt.ylabel('Maximumthe largest street coverage')
    plt.show()
    print(sum(maximum)/len(maximum))


if __name__ == "__main__":
    main()
