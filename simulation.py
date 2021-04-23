import numpy as np
import numpy.linalg as la
from random import randint
from numpy.random import normal
import math

def mask(dimensions, porosity):
    """
    creates sample mask to work with
    args:
        dimensions: 2D-array for mask size
        porosity: porosity of mask
    returns:
        2D-array mask with set porosity via booleans (0 = false, 1 = true)
    """
    for i in range(len(dimensions)):
        for j in range(len(dimensions[i])):
            if randint(0,100) < porosity:
                dimensions[i][j] = 1

    return dimensions

#required dimensions
mask_size = np.zeros((1000,1000))
mask_porosity = 74 #https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7410795/ modified mask
filter_porosity = 70

filter_object =  mask(np.zeros((1000,1000)), filter_porosity)
n_iteration = 1000


#execution
test1 = mask(mask_size, mask_porosity)
test2 = mask(filter_porosity, mask_porosity)

#use gaussian random selection to simulate saliva burst from mouth
n_true = 0
n_false = 0

for _ in range(n_iteration):
    #gaussian each time iteration is run
    #parameters: mean, stdev, size
    x = math.floor(normal(len(test)/2, len(test)/100))
    y = math.floor(normal(len(test)/2, len(test)/100))
    if test[x][y] == 0:
        n_false += 1
    else:
        n_true += 1

print(n_true, n_false)
