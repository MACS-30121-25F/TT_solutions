def compute_frequencies(lst, debug=False):
    """
    Count how often each value between 0 and M (the maximum
    value in the list) occurs in the input list.

    Inputs:
      lst: list of integers between 0 and some upper bound M
        (inclusive), where M is expected to be relative small (say,
        less than 1000).

    Returns: list where the ith element is the number of times
     i occurs in lst.
    """

    # allocate space to hold the lst
    frequencies = [0] * (max(lst) + 1)
    if debug:
        print("Initial value of frequencies:", frequencies)

    for val in lst:
        frequencies[val] = frequencies[val] + 1
        if debug:
            print("Val is: {}... incrementing frequencies[{}]".format(val, val))

    return frequencies


def find_matching_indices(lst, target_val):
    """
    Return a list of the indices that match val

    Inputs:
       lst: a list
       target_val: a value

    Returns: a list of ints
    """

    # Find all the values that match val
    rv = []
    for i, val in enumerate(lst):
        if val == target_val:
            rv.append(i)
    return rv
    

def find_most_frequent_values(lst):
    """
    Find the value or values (in the case of ties) that occur most
    frequently in the list.

    Inputs:
      lst: list of integers between 0 and some upper bound M
        (inclusive), where M is expected to be relative small
        (say, less than 1000).

    Returns: list of the int(s) that occur most frequently.
    """

    # Determine how frequently the most frequent value(s) occurs.
    frequencies = compute_frequencies(lst)
    max_freq = max(frequencies)

    return find_matching_indices(frequencies, max_freq)


def find_least_frequent_values(lst):
    """
    Find the value or values (in the case of ties) that occur most
    frequently in the list.

    Inputs:
      lst: list of integers between 0 and some upper bound M
        (inclusive), where M is expected to be relative small
        (say, less than 1000).

    Returns: list of the int(s) that occur most frequently.
    """

    # Determine how frequently the least frequent value(s) occurs.
    frequencies = compute_frequencies(lst)
    min_freq = min([v for v in frequencies if v > 0])

    return find_matching_indices(frequencies, min_freq)

