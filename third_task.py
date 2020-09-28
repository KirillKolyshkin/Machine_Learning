import matplotlib.pyplot as plt
import numpy as np


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def cluster(k, x, y, x_c, y_c):
    clust = []
    for i in range(0, len(x)):
        min = 0
        min_dist = dist(x[i], y[i], x_c[min], y_c[min])
        for j in range(1, k):
            if min_dist > dist(x[i], y[i], x_c[j], y_c[j]):
                min = j
                min_dist = dist(x[i], y[i], x_c[j], y_c[j])
        clust.append(min)
    return clust


def recalc_c(k, x, y, x_c, y_c, clust):
    error = 0
    for i in range(0, k):
        count = 0
        curX = 0
        curY = 0
        for j in range(0, len(x)):
            if clust[j] == i:
                count = count + 1
                curX = curX + x[j]
                curY = curY + y[j]
        x_c[i] = curX / count
        y_c[i] = curY / count
    plt.scatter(x, y)
    plt.scatter(x_c, y_c, color='r')
    plt.show()
    newclust = cluster(k, x, y, x_c, y_c)
    if newclust != clust:
        error = recalc_c(k, x, y, x_c, y_c, newclust)
    else:
        for i in range(0, k):
            for u in range(0, len(x)):
                if clust[u] == i:
                    error = error + dist(x_c[i], y_c[i], x[u], y[u])
    return error


def kStep(k):
    n = 100
    x = np.random.randint(1, 100, n)
    y = np.random.randint(1, 100, n)
    x_cc = np.mean(x)
    y_cc = np.mean(y)
    r = []
    for i in range(0, n):
        r.append(dist(x[i], y[i], x_cc, y_cc))
    R = max(r)
    x_c, y_c = [], []
    for i in range(0, k):
        x_c.append(R * np.cos(2 * np.pi * i / k) + x_cc)
        y_c.append(R * np.sin(2 * np.pi * i / k) + y_cc)
    plt.scatter(x, y)
    plt.scatter(x_c, y_c, color='r')
    plt.show()
    clust = cluster(k, x, y, x_c, y_c)
    num = recalc_c(k, x, y, x_c, y_c, clust)
    return num


def main():
    flag = 1
    counter = 4
    previous_num = kStep(2)
    cur_num = kStep(3)
    cur_lambda = previous_num - cur_num
    while flag == 1:
        previous_num = cur_num
        cur_num = kStep(counter)
        if previous_num - cur_num < cur_lambda:
            flag = 0
        counter = counter + 1



main()
