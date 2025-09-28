l0 = []
l1 = [1, "abc", 5.7, [1, 3, 5]]
l2 = [10, 11, 12, 13, 14, 15, 16]
l3 = [7, -5, 6, 27, -3, 0, 14]
l4 = [0, 1, 1, 3, 2, 4, 6, 1, 7, 8]

def print_result(t, n, e):
    print(t + " " + str(n) + ": "  + str(e))

print_result("list",1, [7, "xyz", 2.7])
print_result("list",2, len(l1))
print_result("list",3.1, l1[2])
print_result("list",3.2, l1[3][2])
# the next line will fail with out of bounds exception
#print_result("list",4, l1[4])
print_result("list",5, l1[-1])
l1[3][1]=15.0
print_result("list",6, l1[3][1])
print_result("list",7, l2[1:6])
print_result("list",8, l2[:3])
print_result("list",9, l2[1:])
l0.append(1)
l0.append(2)
l0.append(3)
l0.append(4)
print_result("list",10, l0[2])
l2 = l0 + l1
l2[0] = 27
print_result("list",11.1, l2)
print_result("list",11.2, l0)

all_pos = True
for x in l3:
    if x <= 0:
        all_pos = False
        break
print_result("loop", 1, all_pos)

pos_only = []
for x in l3:
    if x > 0:
        pos_only.append(x)
print_result("loop", 2, pos_only)

is_pos_0 = []
for x in l3:
    is_pos_0.append(x > 0)
print_result("loop", 3, is_pos_0)

is_pos_1 = [False]*len(l3)
for i in range(len(l3)):
    is_pos_1[i] = (l3[i] > 0)
print_result("loop", 4, is_pos_1)


M=max(l4)+1
counts = [0]*M
for x in l4:
    counts[x] = counts[x] + 1
print_result("loop", 5, counts)
