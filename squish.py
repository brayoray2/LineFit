import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *
data = np.loadtxt("Marshmallow.csv", delimiter=",", dtype=str)
x = data[1:, 0].astype(np.float32)
y = data[1:, 1].astype(np.float32)
print('y = ', y)
print('x = ', x)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = round(params[0])
intercept = round(params[1])
Equation = print_equation(slope,intercept,'Cm','g')
print(Equation)#The equation of the line is: 0g/Cm + 3Cm
plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("Mass (g)") #change the units as appropriate
plt.ylabel("Height of Marshmallow (Cm)")  #change the units as appropriate
plt.show()
