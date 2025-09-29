from math import sin

def is_power_of_two(n):
    # replace the pass statement with your code
    pass


def fib(n):
    # replace the pass statement with your code
    pass

def find_root_sqrt2(epsilon, a, b):
    # replace the pass statement with your code
    pass


t0 = {"key":"node0",
      "val":27,
      "children":[]}

t1 = {"key":"node0",
      "val":1,
      "children":[{"key":"node0",
                   "val":2,
                   "children":[{"key":"node0",
                                "val":3,
                                "children":[]}]},
                  {"key":"node0",
                   "val":4,
                   "children":[]},
                  {"key":"node0",
                   "val":5,
                   "children":[]}]}


def count_leaves(t):
    '''
    Count the number of leaves in the tree rooted at t
    
    Inputs: (dictionary) a tree
    
    Returns: (integer) number of leaves in t
    '''
    assert t is not None

    if not t["children"]:
        return 1

    num_leaves = 0
    for kid in t["children"]:
        num_leaves += count_leaves(kid)

    return num_leaves


def add_values(t):
    # replace the pass statement with your code
    pass
