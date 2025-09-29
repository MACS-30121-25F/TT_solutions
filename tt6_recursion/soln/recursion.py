from math import sin
def is_power_of_two(n):
  if n == 1:
    return True
  elif n < 1:
    return False
  else:
    return (n % 2 == 0) and is_power_of_two(n/2)

def is_increasing(l):
  if (len(l) <= 1):
    return True
  else:
    if (l[0] < l[1]):
      return is_increasing(l[1:])
    else:
      return False

def is_apparently_increasing(l):
  if (len(l) <= 1):
    return True
  else:
    if (l[1] == -1):
      new_l = [l[0]]
      new_l.extend(l[2:])
      return is_apparently_increasing(new_l)
    elif (l[0] < l[1]):
      return is_apparently_increasing(l[1:])
    else:
      return False

def all_values_increasing_and_greater_than(l, n):
  return (len(l) < 1) or ((l[0] > n) and all_values_increasing_and_greater_than(l[1:], l[0]))

def another_is_increasing(l):
  if len(l) == 0:
    return True
  return all_values_increasing_and_greater_than(l[1:], l[0])

def fib(n):
  if (n == 0) or (n == 1):
    return 1
  else:
    return fib(n-1) + fib(n-2)

def root2(n):
  return n*n - 2

def sinP5(n):
  return sin(n)-0.5

def find_root(f, epsilon, a, b):
  c = (a+b)/2.0
#  print a
#  print b
#  print c
#  print "-"
  if abs(f(c)) < epsilon:
     return c
  elif f(c) > 0:
    if f(a) > 0:
      return find_root(f, epsilon,c, b)
    else: # f(b) > 0
      return find_root(f, epsilon, a,c)
  else: # f(c) < 0
    if f(c) < 0:
      return find_root(f, epsilon,c, b)
    else: # f(c) > 0
      return find_root(f, epsilon, a, c)
