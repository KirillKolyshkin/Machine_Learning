import pandas as pd
import matplotlib.pyplot as plt

gender = None
age = None


def read_file(file):
    global gender
    global age
    table = pd.read_csv(file, delimiter=",")
    print(type(table))
    gender = table['Sex'].values
    age = table['Age'].values


read_file("titanik.csv")

counter = 0
for item in gender:
    if (item == 'male'):
        gender[counter] = 0
    if (item == 'female'):
        gender[counter] = 1
    counter += 1

plt.scatter(gender, age, c=gender, cmap='RdBu')
plt.show()
