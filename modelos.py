import numpy as np

def linear_func(x, a, b):
    return a + b*x
def exponential_func(x, a, b):
    return a * np.exp(b * x)
def logarithmic_func(x,a,b):
    return a + b * np.log(x)
def potential_func(x,a,b):
    return a * x ** b
def hiperbolic_func(x, a, b):
    return a + b/x