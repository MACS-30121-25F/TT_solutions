# CS121 Lab 3: Functions

import math
import numpy
import pylab

def sinc(x):
    '''
    Real valued sinc function  f(x) == sin(x)/x

    Inputs:
        x: float

    Return: float
    '''
    # Make sure we don't divide by zero  
    if x!=0:
        return math.sin(x)/x
    else:
        # sin(0) / 0 is defined as the limiting value 1
        return 1.0


def square(x):
    '''
    Square function f(x) == x*x
    '''
    return x*x
    

def cossq(x):
    '''
    Cossq function f(x) == cos(x) * x
    '''
    return math.cos(x)*x
    
def plot_result(X, Y, title, x_label, y_label):
    pylab.figure()
    pylab.plot(X,Y)
    pylab.title(title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def plot_sinc(left_boundary, right_boundary, dx):
    X = numpy.arange(left_boundary, right_boundary, dx) 

    # apply the sinc function onto the X list
    Y = []
    for x in X:
        Y.append(sinc(x))
                
    plot_result(X, Y, "Sinc function", "X values", "sinc(x)")
    

def plot_square(left_boundary, right_boundary, dx):
    X = numpy.arange(left_boundary, right_boundary, dx) 
    Y = []

    # apply the square function onto the X list
    for x in X:
        Y.append(square(x))
        
    plot_result(X, Y, "Square function", "X values", "square(x)")
    

def plot_cossq(left_boundary, right_boundary, dx):
    X = numpy.arange(left_boundary, right_boundary, dx) 
    Y = []

    # apply the square function onto the X list
    for x in X:
        Y.append(cossq(x))
        
    plot_result(X, Y, "Cossq function", "X values", "cossq(x)")


def go():
    dx = .01
    left_boundary = -10
    right_boundary = 10 

    plot_sinc(left_boundary, right_boundary, dx)
    plot_square(left_boundary, right_boundary, dx)
    plot_cossq(left_boundary, right_boundary, dx)
