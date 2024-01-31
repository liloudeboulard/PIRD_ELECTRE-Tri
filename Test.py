
import pandas as pd
import numpy as np
from numpy import random, vstack, empty
import PreProcess
import Process

# Import of data from csv file as a Pandas Dataframe
d = pd.read_csv('Input_data.csv')
P = 0.018 # trial and error
d['P'] = P
λ = 0.75
repetition = 1


# Preprocess.py

# MC(data)
preProcess_data = PreProcess.MC(d)
print(preProcess_data)

# refIntervals(data)
preProcess_ref = PreProcess.refIntervals(d)
print(preProcess_ref)
"""
# Condition to be fulfilled (b_(k-1,max)<b_(k,min)) by the reference profiles
errors = []
for index, row in preProcess_ref.iterrows():
    for col_index in range(1, len(row)-1, 2):  # Start at the 2nd column, skip every two columns
        if row[col_index] >= row[col_index + 1]:
            errors.append((index, col_index, col_index + 1))

if errors:
    print("Errors found:")
    for error in errors:
        print(f"Index {error[0]} : Column {error[1]} et Column {error[2]}")
    print(f"Total number of errors : {len(errors)}")
else:
    print("No errors found.")
"""

# Process.py

# conc(data)
print("test conc")
test_concA, test_concB = Process.conc(preProcess_data, preProcess_ref)
print(test_concA.shape[1])
# print(test_concA)
print(test_concB.shape[1])

# disco(data)*
print("test disco")
test_discA, test_discB = Process.disco(preProcess_data, preProcess_ref)
print(test_discA.shape[1])
print(test_discB.shape[1])

# gconc(data, dconc1)
print("test gconc")

print("Data Shape:", preProcess_data.shape)
print("Data Index:", preProcess_data.index)
print("Column Index 28:", preProcess_data.iloc[:, 28])


test_gconcA = Process.gconc(preProcess_data, test_concA)
test_gconcB = Process.gconc(preProcess_data, test_concB)
print(test_gconcA.shape)
print(test_gconcB.shape)

# credibility(dgconc, ddisc)
print("test credibility")
test_credA = Process.credibility(test_gconcA, test_discA)
test_credB = Process.credibility(test_gconcB, test_discB)
print(test_gconcA.shape)
print(test_gconcB.shape)

# over_ranking_relations(cred1, cred2, param)
print("test over_ranking_relations")
test_relation = Process.over_ranking_relations(test_credA, test_credB, λ)
print(test_relation)
