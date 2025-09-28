"""
CS121 Team Tutorial 2: Functions
"""

def count_twos(lst):
    """
    Count the number of twos in a list

    Input:
       lst (list): the list

    Returns (int): The number of twos in lst
    """
    count = 0
    for item in lst:
        if item == 2:
            count = count + 1
    return count

# Add your are_any_true function here

# Add your add_lists function here

# Add your add_one function here

def go():
    '''
    Write code to verify that your functions work as expected here.
    Try to think of a few good examples to test your work.
    '''

    lst1 = [1, 2, 1, 0, 2, 0, 2]
    lst2 = [1, 1, 1, 0, 2, 0, 0]
    print(count_twos(lst1))
    print(count_twos(lst2))

    # Add your tests here

if __name__ == "__main__":
    go()
