def f(x):
    '''
    Real valued square function  f(x) == x^2 
    '''
    return x*x

def integrate():
    # decide on the number of rectangles
    n = 10000

    # compute the width of the rectangles
    dx = 1.0/n

    total_area = 0.0
    for i in range(n):
        total_area += f(i*dx) * dx

    return total_area



