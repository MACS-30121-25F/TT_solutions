# These are the solutions to the "Simple practice: Loops"
# part of Team Tutorial 1. You can run this file like this:
#
#    python3 loops.py
#
# to observe the result of each task.

lst0 = []
lst1 = [1, "abc", 5.7, [1, 3, 5]]
lst2 = [10, 11, 12, 13, 14, 15, 16]
lst3 = [7, -5, 6, 27, -3, 0, 14]
lst4 = [0, 1, 1, 3, 2, 4, 6, 1, 7, 8]

# Task 13
all_pos = True
for x in lst3:
    if x <= 0:
        all_pos = False
        break

print("Task 13")
print("all_pos:", all_pos)
print()


# Task 14
pos_only = []
for x in lst3:
    if x > 0:
        pos_only.append(x)

print("Task 14")
print("pos_only:", pos_only)
print()


# Task 15
is_pos = []
for x in lst3:
    is_pos.append(x > 0)

print("Task 15")
print("is_pos:", is_pos)
print()


# Task 16
M = max(lst4) + 1
counts = [0] * M
for x in lst4:
    counts[x] = counts[x] + 1

print("Task 16")
print("counts:", counts)

