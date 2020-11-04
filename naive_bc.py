import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def read_file(file):
    data = pd.read_csv(file, delimiter=";")
    return data


diseases = read_file("disease.csv")
symptomes = read_file("symptom.csv")

disease_probs = []  # вероятность болезней

diseases_num = diseases['количество пациентов'].values
patient_count = diseases_num[-1]
for item in diseases_num[:-1]:
    disease_probs.append(item / patient_count)

our_simptoms = [np.random.randint(0, 2) for i in range(len(symptomes) - 1)]
our_probs = [1] * (len(diseases["Болезнь"]) - 1)
for i in range(len(diseases["Болезнь"]) - 1):
    our_probs[i] *= disease_probs[i]
    for j in range(len(symptomes) - 1):
        if our_simptoms[j] == 1:
            our_probs[i] *= float(symptomes.iloc[j][i + 1])
max = 0
maxIndex = 0
for i in range(len(our_probs)):
    if our_probs[i] > max:
        max = our_probs[i]
        maxIndex = i
print("вероятнее всего у вас " + diseases['Болезнь'].values[maxIndex])

