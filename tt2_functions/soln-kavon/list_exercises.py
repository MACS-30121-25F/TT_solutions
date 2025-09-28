# CS121 Lab 3: Function

def are_any_true(xs):
    '''
    Checks if any objects in the list evaluate to True.
    
    Input:
        Normally, a list of bools.
        
    Output:
        True if there exists an object in the given list that evaluates
        to True, False otherwise.
    '''
    
    for cond in xs:
        if cond:
            return True
    return False

def add_lists(xs, ys):
    '''
    Adds the ith value in the input lists together, producing a new
    list. Equivalent to `map(lambda p: p[0]+p[1], zip(xs, ys))`.
    
    Input:
        Two equal length lists of values that can be added together.
        
    Output:
        a new list L where L[i] == xs[i] + ys[i]
    '''
    assert len(xs) == len(ys)
    
    vals = []
    for i in range(len(xs)):
        vals.append(xs[i] + ys[i])
        
    return vals


def add_one(xs):
    '''
    Adds 1 to the input list, mutating it.
    
    Input:
        a list of values that can have an integer added to it.
        
    Output:
       None, plus the effect of adding 1 to each element of the input list.
    '''
    
    for i in range(len(xs)):
        xs[i] += 1


def go():
    '''
    Write code to verify that your functions work as expected here.
    Try to think of a few good examples to test your work.
    '''

    # test are_any_true
    test_list = [False, True, True, False, True, True]
    assert      are_any_true(test_list)
    assert not( are_any_true([False, False]) )
    assert not( are_any_true([None]) )
    assert      are_any_true([1])
    assert not( are_any_true([0]) )
    assert not( are_any_true([]) )
    
    
    # test add_lists
    negOnes = [-1, -1, -1, -1]
    ones = [1, 1, 1, 1]
    twos = [2, 2, 2, 2]
    mixed = ["ab", 2]
    mixedRes = ["abab", 4]
    assert add_lists(ones, ones) == twos
    assert add_lists(add_lists(ones, ones), negOnes) == ones
    assert add_lists(mixed, mixed) == mixedRes
    
    
    # test add_one
    a = [1, 2, 3, 4, 5]
    c = [2, 3, 4, 5, 6]
    five_ones = [1, 1, 1, 1, 1]
    b = add_lists(a, five_ones)
    assert  a != b
    retVal = add_one(a)
    assert  a == b
    assert  a == c
    assert  retVal == None
    
    print ("Successfully tested all functions!")

if __name__ == "__main__":
    go()
