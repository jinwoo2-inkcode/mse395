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
    mask_sample = dimensions.copy()
    for i in range(len(mask_sample)):
        for j in range(len(mask_sample[i])):
            if randint(0,1000)/10 < porosity:
                mask_sample[i][j] = 1

    return mask_sample

def spray_simulation(test):
    """
    use gaussian random selection to simulate saliva burst from mouth
    args:
        test: mask sample
    returns:
        Simulated porosity of sample
    """
    n_iteration = 1000
    n_true = 0
    n_false = 0
    for _ in range(n_iteration):
        #gaussian each time iteration is run
        #parameters of normal: mean, stdev
        x = math.floor(normal(len(test)/2, len(test)/100))
        y = math.floor(normal(len(test)/2, len(test)/100))
        if test[x][y] == 0:
            n_false += 1
        else:
            n_true += 1
    return n_true/(n_true+n_false)

#required dimensions
mask_size = np.zeros((1000,1000))
mask_porosity = 74 #https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7410795/ modified mask
filter_porosity = 70

"""
Cloth (no filter)	    	14.29375
Cloth (coffee filter)		0.4875
Cloth (paper towel)	    	1.26875
"""

cloth_filter = ["Cloth (no filter)", "Cloth (coffee filter)", "Cloth (paper towel)"]
cloth_samples = [85.706, 99.5125, 98.73125]


filter_object =  mask(np.zeros((1000,1000)), filter_porosity)
n_iteration = 5000


#execution
test1 = mask(mask_size, mask_porosity)
test2 = mask(filter_object, mask_porosity)

test = test1 #type of mask used
cloth_tests = []

for i in cloth_samples:
    cloth_tests.append(mask(mask_size, i))

for j in range(len(cloth_tests)):
    print(cloth_filter[j], spray_simulation(cloth_tests[j]))

# for _ in range(5):
#     print(spray_simulation(mask(mask_size, 85)))