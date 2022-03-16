#! /usr/bin/env python3

"A script to get linear regression plots for petal and sepal lengths"

#Importing all the libararies that need to make graphs
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats

#reading the CSV file 
dataframe = pd.read_csv("iris.csv")

#Making subsets from main dataframe
setosa = dataframe[dataframe.species=="Iris_setosa"]
virginica = dataframe[dataframe.species=="Iris_virginica"]
versicolor = dataframe[dataframe.species=="Iris_versicolor"]
species = [setosa,virginica,versicolor]

#make a for loop to create the graphs
for i in species: 
    x = i.petal_length_cm
    y = i.sepal_length_cm
    regression = stats.linregress(x,y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("i.png")
quit()
