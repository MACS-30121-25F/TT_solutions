# CS121 Lab 3: Functions

import math
import numpy
import pylab

def sinc(x):
    '''
    Real value sinc function  f(x) == sin(x)/x

    Inputs:
        x: float

    Return: float
    '''
    # Make sure we don't divide by zero  
    if x != 0:
        return math.sin(x) / x
    else:
        # sin(0) / 0 == 1
        return 1.0
    
    
def square (x):
    '''
    Returns the square of the given number.
    '''
    return (x * x)
    

def plot_points(xs, ys, title, xlab, ylab):
    '''
    Display a plot with the given points using matplotlib.
    '''
    
    assert len(xs) == len(ys), "mismatched point data!"
                
    # plot the figure
    pylab.figure()
    pylab.plot(xs,ys)
    pylab.title(title)
    pylab.xlabel(xlab)
    pylab.ylabel(ylab)
    pylab.show()
    

def plot_sinc(left_boundary, right_boundary, dx):
    '''
    Plot the sinc function from left_boundary...right_boundary with
    increments of size dx.
    '''
    xs = numpy.arange(left_boundary, right_boundary, dx) 

    # apply the sinc function onto the xs list
    ys = []
    for x in xs:
        ys.append(sinc(x))
                
    plot_points(xs, ys, "Sinc function", "X values", "sinc(x)")
    
    
def plot_square(left_boundary, right_boundary, dx):
    '''
    Plot the square function from left_boundary...right_boundary with
    increments of size dx.
    '''
    xs = numpy.arange(left_boundary, right_boundary, dx) 

    # apply the sinc function onto the xs list
    ys = []
    for x in xs:
        ys.append(square(x))
                
    plot_points(xs, ys, "Square function", "X values", "x^2")
