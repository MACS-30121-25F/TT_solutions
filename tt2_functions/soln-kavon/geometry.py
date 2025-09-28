# CS121 Lab 3: Functions

import math

def dist (a, b):
    '''
    Computes the Euclidian distance between the 2D points a & b.
    
    Inputs:
      a, b : both a pair of numbers
      
    Output:
      the distance between those two points.
    '''
    
    (ax, ay) = a
    (bx, by) = b
    xdiff = (ax - bx) ** 2
    ydiff = (ay - by) ** 2
    return math.sqrt(xdiff + ydiff)

def perimeter (a, b, c):
    '''
    Computes the perimeter of the given triangle using Euclidian distance.
    
    Inputs:
      a, b, c : all three are pairs of numbers
      
    Output:
      the perimeter of the triangle formed by the input points.
    '''
    
    l1 = dist(a, b)
    l2 = dist(a, c)
    l3 = dist(b, c)
    return (l1 + l2 + l3)

def go():
    '''
    Write a small amount of code to verify that your functions work

    Verify that the distance between the points (0, 1) and (1, 0) is
    close to math.sqrt(2)

    After that is done, verify that the triangle with vertices at 
    (0, 0), (0, 1), (1, 0) has a perimeter 2 + math.sqrt(2)
    '''

    testDist = dist((0,1), (1,0))
    expectDist = math.sqrt(2)
    print ("test of dist. \n\toutput:\t\t" + str(testDist) 
            + "\n\texpected:\t" + str(expectDist) + "\n")
            
    testPerimeter = perimeter((0, 0), (0, 1), (1, 0))
    expectPerimeter = 2 + math.sqrt(2)
    print ("test of perimeter. \n\toutput:\t\t" + str(testPerimeter) 
            + "\n\texpected:\t" + str(expectPerimeter) + "\n")

if __name__ == "__main__":
    go()
    
                
