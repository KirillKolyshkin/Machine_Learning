import matplotlib.pyplot as plt
import numpy as np


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def getCurU(x_c, y_c, x, y, x_cur_c, y_cur_c, m):
    sum = 0
    for i in range(0, len(x_c)):
        sum = sum + (dist(x, y, x_cur_c, y_cur_c) / dist(x, y, x_c[i], y_c[i])) ** (2 / (1 - m))
    return sum


def cluster(k, x, y, x_c, y_c, m, clust):
    # clust = [[0] * k for t in range(len(x))]
    for i in range(0, len(x)):
        sum = 0
        for j in range(0, len(x_c)):
            clust[i][j] = getCurU(x_c, y_c, x[i], y[i], x_c[j], y_c[j], m)
            sum += clust[i][j]
        for j in range(0, len(x_c)):
            clust[i][j] /= sum
    # return clust


def recalc_centers(k, x, y, x_c, y_c, clust, m):
    for i in range(0, k):
        count = 0
        num_x = 0
        num_y = 0
        denum_x = 0
        denum_y = 0
        for j in range(0, len(x)):
            num_x += pow(clust[j][i], m) * x[j]
            denum_x += pow(clust[j][i], m)
            num_y += pow(clust[j][i], m) * y[j]
            denum_y += pow(clust[j][i], m)
        x_c[i] = num_x / denum_x
        y_c[i] = num_y / denum_y
    plt.scatter(x, y)
    plt.scatter(x_c, y_c, color='r')
    plt.show()


def decision_function(x, y, x_c, y_c, clust):
    result = 0
    for j in range(0, len(x)):
        prob_array = clust[j]
        for i in range(0, len(prob_array)):
            result += prob_array[i] * dist(x[j], y[j], x_c[i], y_c[i])
    return result


def kStep(k, m):
    k, n = 4, 100
    x = np.random.randint(1, 100, n)
    y = np.random.randint(1, 100, n)
    x_cc = np.mean(x)
    y_cc = np.mean(y)
    r = []
    clust = [[0] * k for t in range(len(x))]
    for i in range(0, n):
        r.append(dist(x[i], y[i], x_cc, y_cc))
    R = max(r)
    x_c, y_c = [], []
    for i in range(0, k):
        x_c.append(R * np.cos(2 * np.pi * i / k) + x_cc)
        y_c.append(R * np.sin(2 * np.pi * i / k) + y_cc)
    for i in range(0, n):
        clust
    plt.scatter(x, y)
    plt.scatter(x_c, y_c, color='r')
    plt.show()

    current_decision = 1
    previous_decision = current_decision
    cluster(k, x, y, x_c, y_c, m, clust)
    current_decision = decision_function(x, y, x_c, y_c, clust)

    while abs(previous_decision - current_decision) > 0.2:
        previous_decision = current_decision
        recalc_centers(k, x, y, x_c, y_c, clust, m)
        cluster(k, x, y, x_c, y_c, m, clust)
        current_decision = decision_function(x, y, x_c, y_c, clust)


def main():
    kStep(4, 1.5)


main()
