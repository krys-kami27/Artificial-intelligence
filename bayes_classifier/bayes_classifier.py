# Krystian Kaminski nr 304013

from matplotlib import pyplot as plt
import math
from operator import itemgetter


def open_file(filename):
    # read data from file
    file = open(filename, "r")
    data = file.readlines()
    for line in range(len(data)):
        while "\t" in data[line]:
            data[line] = data[line].split()
            data[line] = [float(num) for num in data[line]]
    file.close()
    return data


def show_graph(p1, p2, datafile):
    # present graph of two params of items
    for item in datafile:
        if item[7] == 1:
            color = 'ro'
        elif item[7] == 2:
            color = 'bo'
        elif item[7] == 3:
            color = 'go'
        plt.plot(item[p1], item[p2], color)
    plt.ylabel(f'{p1+1} parameter value')
    plt.xlabel(f'{p2+1} parameter value')
    plt.show()


def avg(data):
    # return average of data
    return sum(data)/len(data)


def stdev(data):
    #  standard deviation of data
    return (sum([(x-avg(data))**2 for x in data])/float(len(data)-1))**(1/2)


def probability(x, avg, stdev):
    # probability density function value
    return (1/((2*math.pi)**(1/2)*stdev))*math.e**(-((x-avg)**2/(2*stdev**2)))


def result_prob(data, row):
    # return comparison of probability for all groups
    line_sum = sum([data[label][0][2] for label in data])
    probs = dict()
    for group_value, data_groups in data.items():
        probs[group_value] = data[group_value][0][2]/float(line_sum)
        for i in range(len(data_groups)):
            avg, stdev, amount = data_groups[i]
            probs[group_value] *= probability(row[i], avg, stdev)
    return probs


def matrix_correct(num, results, test1, test2, test3):
    # return matrix and amount of correct results
    correct = 0
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for iter in range(70-7*num):
        prob1 = result_prob(results, test1[iter])
        if prob1[1] == max(prob1.values()):
            correct += 1
            matrix[0][0] += 1
        elif prob1[2] == max(prob1.values()):
            matrix[1][0] += 1
        else:
            matrix[2][0] += 1

        prob2 = result_prob(results, test2[iter])
        if prob2[2] == max(prob2.values()):
            correct += 1
            matrix[1][1] += 1
        elif prob2[1] == max(prob2.values()):
            matrix[0][1] += 1
        else:
            matrix[2][1] += 1

        prob3 = result_prob(results, test3[iter])
        if prob3[3] == max(prob3.values()):
            correct += 1
            matrix[2][2] += 1
        elif prob2[1] == max(prob3.values()):
            matrix[0][2] += 1
        else:
            matrix[1][2] += 1
    return matrix, correct



def main():
    # main function with all tests

    for sort in range(2):
        datafile = open_file("seeds_dataset.txt")
        if sort == 0:
            datafile = sorted(datafile, key=itemgetter(2))

        show_graph(4, 6, datafile)
        # ----------------------
        # average and stdev for all datafile
        print('\nNumber of param, average, stdev')

        data_param_values = [[datafile[x][y] for x in range(len(datafile))] for y in range(7)]
        for index in range(7):
            print(avg(data_param_values[index]), stdev(data_param_values[index]))
        # ---------------------
        # average and stdev for 3 groups
        data1 = datafile[0:70]
        data2 = datafile[70:140]
        data3 = datafile[140:210]
        data1_param_values = [[data1[x][y] for x in range(len(data1))] for y in range(7)]
        data2_param_values = [[data2[x][y] for x in range(len(data2))] for y in range(7)]
        data3_param_values = [[data3[x][y] for x in range(len(data3))] for y in range(7)]
        print('\nType 1: nuber of param, average, stdev')
        for index in range(7):
            print(index+1, avg(data1_param_values[index]), stdev(data1_param_values[index]))
        print('\nType 2: nuber of param, average, stdev')
        for index in range(7):
            print(index+1, avg(data2_param_values[index]), stdev(data2_param_values[index]))
        print('\nType 3: nuber of param, average, stdev')
        for index in range(7):
            print(index+1, avg(data3_param_values[index]), stdev(data3_param_values[index]))

        results = {1: [], 2: [], 3: []}
        for index in range(7):
            results[1].append((avg(data1_param_values[index]), stdev(data1_param_values[index]), 70))
            results[2].append((avg(data2_param_values[index]), stdev(data2_param_values[index]), 70))
            results[3].append((avg(data3_param_values[index]), stdev(data3_param_values[index]), 70))
        probabilities = result_prob(results, datafile[70])
        print(results)
        print('------------')
        print(probabilities)
        print('------------')
        percent_correct = []
        for num in range(1, 10):
            train1 = datafile[0:7*num]
            train2 = datafile[70:70+7*num]
            train3 = datafile[140:140+7*num]

            test1 = datafile[7*num:]
            test2 = datafile[70+7*num:]
            test3 = datafile[140+7*num:]

            train1_param_values = [[train1[x][y] for x in range(len(train1))] for y in range(7)]
            train2_param_values = [[train2[x][y] for x in range(len(train2))] for y in range(7)]
            train3_param_values = [[train3[x][y] for x in range(len(train3))] for y in range(7)]
            results = {1: [], 2: [], 3: []}
            for index in range(7):
                results[1].append((avg(train1_param_values[index]), stdev(train1_param_values[index]), 7*num))
                results[2].append((avg(train2_param_values[index]), stdev(train2_param_values[index]), 7*num))
                results[3].append((avg(train3_param_values[index]), stdev(train3_param_values[index]), 7*num))
            probabilities = result_prob(results, datafile[70])
            # print(probabilities)
            matrix_res = matrix_correct(num, results, test1, test2, test3)
            correct = matrix_res[1]
            matrix = matrix_res[0]
            print(correct/(210-21*num)*100)
            if num == 4:
                print('   1   2   3')
                for i in range(1, 4):
                    print(f'{i}  {matrix[i-1]}')
            percent_correct.append(correct/(210-21*num)*100)
        plt.plot([x for x in range(21, 210, 21)], percent_correct)
        plt.ylabel(f'Percent of correct results from test')
        plt.xlabel(f'amount of train data size')
        plt.show()


if __name__ == "__main__":
    main()
