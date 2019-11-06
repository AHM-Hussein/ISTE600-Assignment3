import sys
import os
import pandas as pd
from pandas import DataFrame


def read_arff(filename, data):
    # Read in data from file line by line
    if os.path.exists(filename):
        infile = open(filename, 'r')
        save_data = 0

        line = infile.readline()

        while line:
            line = line.strip()

            # add instances to the list
            if (save_data == 1):
                data.append(line.split(','))

            # start saving instances once we actually reach the instances in the file
            if (line.count('@data') > 0):
                save_data = 1

            line = infile.readline()

        infile.close()
    else:
        print('Unable to load data.txt')
        exit(1)

    # Get specific columns from the dataset
    # data = pd.DataFrame(data, columns = list('press','mass','age','class'))
    # Convert continuous attributes to float and class labels to integers
    for i in range(0, len(data)):
        data[i][0] = data[i][0]
        data[i][1] = data[i][1]
        data[i][2] = data[i][2]
        data[i][3] = data[i][3]


data = []

read_arff("diabetes_desc1.arff", data)

fid = open('diabetes_desc2.arff', 'w')

fid.write('@relation diabetes\n\n')
fid.write('@attribute press {low,ideal,prehigh,high}\n')
fid.write('@attribute mass {underweight,normal,overweight}\n')
fid.write('@attribute age {young,middle,elderly}\n')
fid.write('@attribute class {tested_negative,tested_positive}\n\n')
fid.write('@data\n\n')

for record in data:
    press =float(record[0])
    mass = float(record[1])
    age = float(record[2])
    label = record[3]

    # Diastolic Blood Pressure low = < 90, ideal = 90 to 120, prehigh = > 120 to 140, high = > 140
    # Body Mass Index (BMI) underweight = < 18.5, normal = 18.5 to 25, overweight = > 25
    # Age young = < 40, middle = 40 to 60, elderly = > 60

    if (press <= 90):
        press = 'low'
    elif (press >= 90 and press <= 120):
        press = 'ideal'
    elif (press >= 120 and press <= 140):
        press = 'prehigh'
    else:
        press = 'high'

    if (mass < 18.5):
        mass = 'underweight'
    elif (mass >= 18.5 and mass <= 25):
        mass = 'normal'
    elif (mass > 25):
        mass = 'overweight'

    if (age < 40):
        age = 'young'
    elif (age >= 40 and age <= 60):
        age = 'middle'
    elif (age > 60):
        age = 'elderly'

    fid.write(press + ',' + mass + ',' + age + ',' + label + '\n')

fid.close()
