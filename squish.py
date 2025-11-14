import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *
data = np.loadtxt("Marshmallow.csv", delimiter=",", dtype=str)
print(data[0,:])
