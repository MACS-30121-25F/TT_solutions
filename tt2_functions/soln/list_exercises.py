# CS121 Team Tutorial 2: Functions

# Write functions are_any_true, add_lists, and add_one

def count_twos(lst):
    """
    Count the number of twos in a list
    """
    count = 0
    for item in lst:
        if item == 2:
            count = count + 1
    return count

def are_any_true(l):
    for v in l:
        if v:
            return True
        
    return False

def add_lists(a, b):
    assert len(a) == len(b), "Lists must be the same length"
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])

    return c
                
def add_one(a):
    for i in range(len(a)):
        a[i] = a[i] + 1

def go():
    '''
    Write code to verify that your functions work as expected here
    Try to think of a few good examples to test your work.
    '''

    lst1 = [1, 2, 1, 0, 2, 0, 2]
    lst2 = [1, 1, 1, 0, 2, 0, 0]
    print(count_twos(lst1))
    print(count_twos(lst2))

    test_list = [True, True, False, True, True]
    test_list1 = [True, True, False, True, False]
    test_list2 = [False, False, False]

    print(are_any_true(test_list))
    print(are_any_true(test_list1))
    print(are_any_true(test_list2))
    print(are_any_true([]))

    a = [1, 2, 3, 4, 5]
    b = [2, 2, 2, 2, 2]

    print(add_lists(a, b))

    print(add_lists([], []))

    add_one(a)
    print(a)

if __name__ == "__main__":
    go()
    