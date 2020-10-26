import sys
import numpy as np


def first_connection():
    min = weight[0][1]
    i_min, j_min = 0, 1
    for i in range(0, n):
        for j in range(i + 1, n):
            if weight[i][j] < min:
                min = weight[i][j]
                i_min, j_min = i, j
    tree[i_min][j_min] = tree[j_min][i_min] = min
    weight[i_min][j_min] = weight[j_min][i_min] = sys.maxsize
    connect_pnt[i_min] = connect_pnt[j_min] = 1


def lync_all():
    min = sys.maxsize
    i_min, j_min = None, None
    for i in range(0, n):
        if connect_pnt[i] == 1:
            for j in range(n):
                if connect_pnt[j] == 0:
                    if min > weight[i][j]:
                        min = weight[i][j]
                        i_min, j_min = i, j
    tree[i_min][j_min] = tree[j_min][i_min] = min
    weight[i_min][j_min] = weight[j_min][i_min] = sys.maxsize
    connect_pnt[i_min] = connect_pnt[j_min] = 1


def delete_connection():
    max = 0
    i_max, j_max = None, None
    for i in range(0, n):
        for j in range(i + 1, n):
            if tree[i][j] > max:
                max = tree[i][j]
                i_max = i
                j_max = j
    tree[i_max][j_max] = tree[j_max][i_max] = 0


def addPoints(i, j, cl):
    for t in range(n):
        if clust_pnt[t] == 0 and tree[t][j] != 0 and t != i:
            clust_pnt[t] = cl
            addPoints(t, j, cl)
        if clust_pnt[t] == 0 and tree[i][t] != 0 and t != j:
            clust_pnt[t] = cl
            addPoints(i, t, cl)


def cluster():
    cl = 1
    for i in range(n):
        for j in range(n):
            if (clust_pnt[i] == 0 and clust_pnt[j] == 0) and tree[i][j] != 0:
                clust_pnt[i] = clust_pnt[j] = cl
                addPoints(i, j, cl)
                cl += 1


n, k = 5, 2
weight = [[0 for i in range(n)] for i in range(n)]
for i in range(0, n):
    for j in range(i + 1, n):
        weight[i][j] = np.random.randint(1, 100)
        weight[j][i] = weight[i][j]
tree = [[0 for i in range(n)] for i in range(n)]
connect_pnt = [0 for i in range(n)]
first_connection()
while 0 in connect_pnt:
    lync_all()
for i in range(k - 1):
    delete_connection()
print(tree)
clust_pnt = [0 for i in range(n)]
cluster()
print(clust_pnt)
