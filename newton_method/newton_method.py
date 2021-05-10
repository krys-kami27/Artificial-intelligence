import time
import matplotlib.pyplot as plt


def steepest_gradient_descent(x, y, beta, step_num):
    step = 0
    value = ((x * x + y - 11)**2 + (x + y * y - 7)**2)
    while step != step_num and value > 1e-12:
        try:
            d_x = (4 * x**3 + 4 * x * y - 42 * x + 2 * y**2 - 14)
            d_y = (4 * y**3 + 4 * x * y - 26 * y + 2 * x**2 - 22)
            x += -beta * d_x
            y += -beta * d_y
            value = ((x * x + y - 11)**2 + (x + y * y - 7)**2)
            step += 1
        except OverflowError:
            return '-', '-', '-'
    x = float("{:.2f}".format(x))
    y = float("{:.2f}".format(y))
    value = (x * x + y - 11)**2 + (x + y * y - 7)**2
    value = float("{:.2f}".format(value))
    return x, y, value


def newton_method(x, y, beta, step_num):
    step = 0
    value = ((x * x + y - 11)**2 + (x + y * y - 7)**2)
    while step != step_num and value > 1e-12:
        try:
            d_x = 4*x**4-28*x**3-42*x**2+281*x+2*y**4+8*x*y**3
            d_x += 12*x**3*y**2-128*x*y**2-29*y**2-2*x**2*y+22*y+91
            d_x /= 12*x**3-82*x**2-42*x+12*y**3+36*x**2*y**2-130*y**2-4*x*y-26*y+273
            d_y = 2*x**4-45*x**2+14*x+4*y**4+12*x**2*y**3
            d_y += -44*y**3-2*x*y**2-26*y**2+8*x**3*y-80*x**2*y+265*y+231
            d_y /= 12*x**3-82*x**2-42*x+12*y**3+36*x**2*y**2-130*y**2-4*x*y-26*y+273
            x += -beta * d_x
            y += -beta * d_y
            value = ((x * x + y - 11)**2 + (x + y * y - 7)**2)
            step += 1
        except OverflowError:
            return '-', '-', '-'
    x = float("{:.2f}".format(x))
    y = float("{:.2f}".format(y))
    value = (x * x + y - 11)**2 + (x + y * y - 7)**2
    value = float("{:.2f}".format(value))
    return x, y, value


def main():
    # Firstly I check which beta for methods is best
    range_list = [x/100 for x in range(1, 200)]
    sgd_counter = []
    nm_counter = []
    for beta in range(1, 200):
        minimum_counter_sgd = 0
        minimum_counter_nm = 0
        for x in range(-5, 6):
            for y in range(-5, 6):
                if steepest_gradient_descent(x, y, beta/100, 100)[2] == 0:
                    minimum_counter_sgd += 1
                if newton_method(x, y, beta/100, 100)[2] == 0:
                    minimum_counter_nm += 1
        sgd_counter.append(minimum_counter_sgd)
        nm_counter.append(minimum_counter_nm)
    # graph of beta parameters
    plt.scatter(range_list, sgd_counter, color='red')
    plt.scatter(range_list, nm_counter, color='blue')
    plt.show()

    sgd_beta = (sgd_counter.index(max(sgd_counter)) + 1)/100
    nm_beta = (nm_counter.index(max(nm_counter)) + 1)/100

    times_sgd = []
    times_nm = []
    minimum_counter = 0
    print("Tests for steepest_gradient_descent method")
    for x in range(-5, 6):
        for y in range(-5, 6):
            timer = time.time()
            minimum = steepest_gradient_descent(x, y, sgd_beta, 100)
            times_sgd.append(time.time() - timer)
            print(f'for x = {x}, y = {y}, minimum = {minimum[2]} in x = {minimum[0]}, y = {minimum[1]}')
            if minimum[2] < 1e-12:
                    minimum_counter += 1
    print(f'{minimum_counter}/121 points gave correct minimum\n')

    minimum_counter = 0
    print("Tests for newton_method")
    for x in range(-5, 6):
        for y in range(-5, 6):
            timer = time.time()
            minimum = newton_method(x, y, nm_beta, 100)
            times_nm.append(time.time() - timer)
            print(f'for x = {x}, y = {y}, minimum = {minimum[2]} in x = {minimum[0]}, y = {minimum[1]}')
            if minimum[2] < 1e-12:
                minimum_counter += 1

    print(f'{minimum_counter}/121 points gave correct minimum\n')
    range_list = [x for x in range(1, 122)]
    plt.scatter(range_list, times_sgd, color='red')
    plt.scatter(range_list, times_nm, color='blue')
    plt.show()

    # test with number of maximum steps
    minimum_counter_sgd = []
    minimum_counter_nm = []
    list_steps = [x for x in range(1, 150, 1)]

    for step in range(1, 150, 1):
        counter_sgd = 0
        counter_nm = 0
        for x in range(-5, 6):
            for y in range(-5, 6):
                minimum_sgd = steepest_gradient_descent(x, y, sgd_beta, step)
                minimum_nm = newton_method(x, y, nm_beta, step)
                if minimum_sgd[2] < 1e-12:
                    counter_sgd += 1
                if minimum_nm[2] < 1e-12:
                    counter_nm += 1
        minimum_counter_sgd.append(counter_sgd)
        minimum_counter_nm.append(counter_nm)

    plt.scatter(list_steps, minimum_counter_sgd, color='red')
    plt.scatter(list_steps, minimum_counter_nm, color='blue')
    plt.show()



if __name__ == "__main__":
    main()
