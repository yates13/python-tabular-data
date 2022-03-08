#! /usr/bin/env python3

"A module for linear regression on iris species"

"Adding the required packages"

import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


#def seperate(dataset):
    #new = dataset.species.nunique()
    #print(new)
    #versicolor = dataset[dataset.species == "Iris_versicolor"]
    #split = dataset.iloc[4:4,4]
    #split = dataset.species.unique()
    #print(versicolor) 

def species(versicolor):
    """Makes a linear regression model based on the given iris species
    """
    x = dataset.petal_length_cm
    y = dataset.sepal_length_cm
    regression = dataset.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "red", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("n")



if __name__ == '__main__':
    dataset = pd.read_csv("iris.csv")
    versicolor = dataset[dataset.species == "Iris_versicolor"]
    #seperate(dataset)
    #data = dataset.species.unique()
    species(versicolor)
    
