#! /usr/bin/env python3

"A module for linear regression on iris species"

"Adding the required packages"

import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

def regression(species_subset, i):
    """
    Makes a linear regression model based on the given iris species that are obtained 
    through species_regression function
    ---------
    Arguments:
        In: 
            species_subset = each uniques species in the data set
            i = each iteration of the unique species
        Out: 
            linear regression graphs for each species
    --------
    Example:
        Iris_setosa.png
    """
    x = species_subset.petal_length_cm
    y = species_subset.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "red", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.title("%s" % i)
    plt.legend()
    plt.savefig("%s.png" % i)
    plt.clf()

def species_regression():
    """
    Loops through unique species in dataset in order to run linear regression function.
    Figures are renamed with appropriate species information and 
    plt.clf is used to clear the plot between figures. 
    ------
    Parameters:
        species_subset = each uniques species in the data set
        i = each iteration of the unique species
    Returns:
        all unique species from the data 
    """
    species_list = dataset.species.unique()
    print(species_list)
    for i in species_list:
        print(i)
        species_subset = dataset[dataset.species == i] 
        regression(species_subset, i)

if __name__ == '__main__':
    dataset = pd.read_csv("iris.csv")
    species_regression()
