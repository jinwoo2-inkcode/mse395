import numpy as np
import numpy.linalg as la

def mask(dimensions, porosity):
    """
    creates sample mask to work with
    args:
        dimensions: 2D-array for mask size
        porosity: porosity of mask
    returns:
        2D-array mask with set porosity via booleans (0 = false, 1 = true)
    """
    return

#required dimensions
mask_size = np.zeros((1000,1000))
mask_porosity = ""
n_iteration = 1000


#execution
test = mask(mask_size, mask_porosity)

#use gaussian random selection to simulate saliva burst from mouth
n_true = 0
n_false = 0
for _ in range(n_iteration):
    #gaussian each time iteration is run
    if test[x,y] == 0:
        n_false += 1
    else:
        n_true += 1

