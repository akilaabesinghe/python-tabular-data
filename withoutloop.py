#! /usr/bin/env python3

# importing packages
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# open the dataframe 
dataframe = pd.read_csv("iris.csv")

#Graph for versicolor species
versicolor = dataframe[dataframe.species == "Iris_versicolor"]
x = versicolor.petal_length_cm
y = versicolor.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.figure(1)
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("versicolor.png")

#Graph for setosa species
dataframe2 = pd.read_csv("iris.csv")
setosa = dataframe2[dataframe2.species == "Iris_setosa"]
x = setosa.petal_length_cm
y = setosa.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.figure(2)
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("setosa.png")

# Graph for virginica species
dataframe3 = pd.read_csv("iris.csv")
virginica = dataframe3[dataframe3.species == "Iris_virginica"]
x = virginica.petal_length_cm
y = virginica.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.figure(3)
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("virginica.png")
