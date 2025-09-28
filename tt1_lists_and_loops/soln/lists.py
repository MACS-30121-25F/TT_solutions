# These are the solutions to the "Simple practice: Lists"
# part of Team Tutorial 1. Please note that, for most tasks,
# you will need to copy-paste the corresponding code into
# a Python interpreter to observe the result.

lst0 = []
lst1 = [1, "abc", 5.7, [1, 3, 5]]
lst2 = [10, 11, 12, 13, 14, 15, 16]
lst3 = [7, -5, 6, 27, -3, 0, 14]
lst4 = [0, 1, 1, 3, 2, 4, 6, 1, 7, 8]

# Task 1
lst5 = [7, "xyz", 2.7]

# Task 2
len(lst1)

# Task 3
lst1[2]

# Task 4
# The following code will produce this error:
# IndexError: list index out of range

# lst1[4]

# Task 5
lst2[-1]

# Task 6
lst1[3][2]

# Task 7
lst1[3][1] = 15.0

# Task 8
lst2[1:6]

# Task 9
lst2[:3]

# Task 10
lst2[1:]

# Task 11
lst0.append(1)
lst0.append(2)
lst0.append(3)
lst0.append(4)

lst0[3]

#Task 12
n1 = lst2 + lst3

n1[0] = 1000
n1[-1] = 2000

# Try printing the contents of lst2 and lst3.
# Observe how changing n1 doesn't affect lst2
# or lst3.