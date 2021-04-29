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
        True means the spot is blocked
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

def mask_improvised(dimensions, porosity, pore):


    x = len(dimensions)
    y = len(dimensions[0])
    mask_sample = np.ones((x,y))
    im_iter = round(porosity/(math.pi*(0.5*pore)**2)*10000) #conversion from cm to um


    for i in range(im_iter):
        x_point = randint(0,x-1)
        y_point = randint(0,y-1)
        #print(x_point,y_point)
        mask_sample[x_point][y_point] = 0
        #print(mask_sample[x_point][y_point])
        for j in range(math.floor(math.sqrt(pore))):
            if x_point+j < x-1:
                #print("x+j")
                for k in range(math.floor(math.sqrt(pore))):
                    if y_point+k < y-1:
                        #print("y+j")
                        mask_sample[x_point+j][y_point+k] = 0      

    return mask_sample

#required dimensions
mask_size = np.zeros((1000,1000))
mask_porosity = 74 #https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7410795/ modified mask
filter_porosity = 70



"""
Mask Type                   % Transmission  Poro Size
Cloth (no filter)	    	14.29375        100 um      https://www.materialstoday.com/characterization/comment/focus-on-apparel-complexity/
Cloth (coffee filter)		0.4875          10 um       https://knowyourgrinder.com/all-about-the-humble-coffee-filter/#:~:text=Most%20paper%20coffee%20filters%20come,size%205%2Dmicron%20filter%20would.
Cloth (paper towel)	    	1.26875         20 um       https://thesurvivalmom.com/reality-coffee-filters-preparedness-uses-hint-mostly-fail/#:~:text=Paper%20towels%20are%20designed%20to,particularly%20good%20filter%20in%20general.
"""

"""
COVID-19 particle size: 1.4 um https://www.sphosp.org/wp-content/uploads/2020/04/Letter-in-response-to-N-95-use-RA-Final.pdf
"""

#previous code
# cloth_filter = ["Cloth (no filter)", "Cloth (coffee filter)", "Cloth (paper towel)"]
# cloth_samples = [85.706, 99.5125, 98.73125]

# covid_particle_size = 1.4

# filter_object =  mask(np.zeros((1000,1000)), filter_porosity)
# n_iteration = 5000


# #execution
# test1 = mask(mask_size, mask_porosity)
# test2 = mask(filter_object, mask_porosity)

# test = test1 #type of mask used
# cloth_tests = []

# for i in cloth_samples:
#     cloth_tests.append(mask(mask_size, i))

# for j in range(len(cloth_tests)):
#     print(cloth_filter[j], spray_simulation(cloth_tests[j]))

#readvised code
cloth_filter = ["Cloth (no filter)", "Cloth (coffee filter)", "Cloth (paper towel)"]
cloth_samples = [85.706, 99.5125, 98.73125]

test1 = mask_improvised(mask_size, 85.706, 100)
test2 = mask_improvised(mask_size, 99.5125, 10)
test3 = mask_improvised(mask_size, 98.73125, 20)

print(spray_simulation(test1))
print(spray_simulation(test2))
print(spray_simulation(test3))