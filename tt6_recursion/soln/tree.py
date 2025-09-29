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
    assert t is not None

    if not t["children"]:
        return 1

    num_leaves = 0
    for kid in t["children"]:
        num_leaves += count_leaves(kid)

    return num_leaves


def add_values(t):
    assert t is not None

    if not t["children"]:
        return t["val"]

    num_leaves = t["val"]
    for kid in t["children"]:
        num_leaves += add_values(kid)

    return num_leaves
    
    

