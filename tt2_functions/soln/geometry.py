# CS121 Team Tutorial 2: Functions

import math

def dist_to_origin(p):
    (x, y) = p
    return math.sqrt((x * x) + (y * y))

def dist(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
           
def perimeter(p1, p2, p3):
    return dist(p1, p2) + dist(p2, p3) + dist(p3, p1);
                
def go():
    '''
    Write a small amount of code to verify that your functions work

    Verify that the distance between the points (0, 1) and (1, 0) is
    close to Math.sqrt(2)

    After that is done, verify that the triangle 
    with vertices at (0, 0), (0, 1), (1, 0) has 
    a perimeter 2 + Math.sqrt(2)
    '''
    
    print("The distance between (1, 0) and the origin is: {:f}".format(dist_to_origin((1, 0))))
    print("The distance between (0, 1) and (1, 0) is: {:f}".format(dist((0, 1), (1, 0))))
    print("The perimeter is: {:f}".format(perimeter((0, 0), (0, 1), (1, 0))))

if __name__ == "__main__":
    go()
    
                

