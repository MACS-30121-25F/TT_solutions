===========================
Team Tutorial #2: Functions
===========================

For instructions on how to get started on these tutorials, 
please see Team Tutorial #1.

Structure of this tutorial
--------------------------

In Team Tutorial #1, you were exposed to functions and called
some functions that were provided for you, but you did not write any functions
yourself.  In this tutorial, you will write your own functions.

By the end of this tutorial, you should be able to:

#. write simple functions and
#. call them from the interpreter and from other functions.

You will need both of these skills for Programming Assignment #2.
This tutorial has two main sections:

* **Part 1: Simple practice**: In this part, we will show you the necessary steps to write a function from scratch, then you will get practice writing your own functions.

* **Part 2: Extended activity**: The second part will provide practice with abstraction by showing you how to generalize some of the code you wrote in TT #1. It provides additional practice for PA #2. 

Please note that, while you could do both of these activities with your team in one sitting, it may be better to work through the first part earlier in the module, and the second part once you’ve become more comfortable with functions.

Getting started
---------------

If this is your first time working through a Team Tutorial, please see the "Getting started" section of Team Tutorial #1 to set up your Team Tutorials repository.

To get the files for this set of short exercises, first set the
``GITHUB_USERNAME`` environment variable by running the following
command at the Linux command line (replacing ``replace_me`` with your
GitHub username)::

       GITHUB_USERNAME=replace_me

(remember you can double-check whether the variable is properly set by
running ``echo $GITHUB_USERNAME``)

Then navigate to your Team Tutorials repository and ``pull`` the new
material:

::

      cd ~/{course_number_lower}
      cd team-tutorials-$GITHUB_USERNAME
      git pull upstream main

You will find the files you need in the ``tt2`` directory.

Simple practice: Functions
--------------------------

Functions are fundamental building blocks to programs that allow us to name a piece of code and re-use it multiple times with different inputs. 
They are an essential part of programming in Python and you will use them repeatedly in your work.

In this section, we will show you the steps to write a function from scratch, and then give you some tasks to work on. 
When you get to the tasks, we suggest that one person on the team have Visual Studio Code (VS Code) and ``ipython3`` open and visible to everyone, and that you all collaboratively decide on the answer to each task. 

If you get stumped in any of these, you may want to see if you can figure out the answer by re-reading the relevant sections of the book. 
The concepts in this tutorial are discussed in the Introduction to Functions chapter of the book.
If you get really stumped, don’t hesitate to ask for help.


Geometry
~~~~~~~~

Start by opening the file ``geometry.py`` in VS Code and an ``ipython3`` window.  
We will write our function implementations in ``geometry.py`` and test them in ``ipython3``. 
When you start ``ipython3``, it's a good idea to set up autoreload so that the changes you make in your .py
files will be reflected in the interpreter:

::

    $ ipython3

    In [1]: %load_ext autoreload

    In [2]: %autoreload 2

A point in the real plane can be described by an x coordinate and a y
coordinate, written mathematically as the point (x, y). The distance between
the point (x, y) and the origin (the point (0, 0)) is given by the formula:

.. math::
   \sqrt{x^2 + y^2}

Let's start by writing a function that takes a point as input, computes the
distance between that point and the origin, and returns that distance.

Writing the function header is a good place to start. 
First, we need to pick out a name for our function. 
In Python, you can name a function (almost) anything, but we should pick something descriptive, like ``dist_to_origin``. 

.. code-block:: python

   def dist_to_origin

Now we need to decide what the parameters to our function should be.
What types can we use to describe a point in Python? 
Since a point is specified by two numbers, we could write a function that takes two arguments, like this:

.. code-block:: python

   def dist_to_origin(x, y):

Or we could use a tuple, like this:

.. code-block:: python

   def dist_to_origin(p):

where ``p`` is a 2-tuple of numbers (a tuple with two floats or
integers).  Since a point is really just one object, a tuple is a more
apt description of a point.

Now we need to write a docstring that describes what the function does, what it 
expects as input (including the type of input), and what it returns.

.. code-block:: python

   def dist_to_origin(p):
       """
       Find the distance from a point to the origin

       Input:
         p (tuple): a point in two dimensions

       Returns (float): The distance between p and the origin
       """
 
Now that we have the header and a docstring, we can write the body of the function. 

.. code-block:: python

   def dist_to_origin(p):
       """
       Find the distance from a point to the origin

       Input:
         p (tuple): a point in two dimensions

       Returns (float): The distance between p and the origin
       """
       (x, y) = p
       return math.sqrt((x * x) + (y * y))

The first line of the body of the function *unpacks* (extracts) the values from
``p`` and assigns them to the variables ``x`` and ``y``. 
This is considered more "Pythonic" than using indexing to retrieve the values
``p[0]`` and ``p[1]``. It also makes your code easier to read and is less prone to typos.
On the second line of the body, we use the ``math`` module to implement the distance to
origin formula. 

Wait! We're not quite done yet. Before moving on, we should test our function. 
Let's use ``ipython3`` and try out ``dist_to_origin`` with a few points. 

::

    In [10]: import geometry

    In [11]: p = (0, 0)

    In [12]: geometry.dist_to_origin(p)
    Out[12]: 0.0

    In [13]: p = (1, 0)

    In [14]: geometry.dist_to_origin(p)
    Out[14]: 1.0

    In [15]: p = (1, 1)

    In [16]: geometry.dist_to_origin(p)
    Out[16]: 1.4142135623730951

   

Now it's your turn.

A line segment can be described by two points (x1, y1) and (x2, y2). 
The length of a line segment can be found by computing the following 
mathematical formula:

.. math::
   \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}

**Task 1**: Write the header for a function called ``dist`` that takes in arguments 
that describe two points and returns one value that is the distance between those two points.  Make sure to include the doctsring.

**Task 2**: After you have written the function header, write the body of the function. 
Be sure to ``return`` the correct value. You will need to use the function ``math.sqrt``, 
which takes a ``float`` as an argument and returns its square root as a ``float``.

**Task 3**: Verify that your code works by using ``dist`` in the interpreter with a simple example. 
For example, compute the distance between the points (0, 1) and (1, 0). 
You should get a number very close to 1.414.
   
**Task 4**: Repeat tasks 1, 2, and 3 with a new function called ``perimeter`` that 
takes in enough information to describe three points that define a triangle and returns the perimeter of that triangle. 
You should not call ``math.sqrt`` within the body of the ``perimeter`` function.  
Try your function on the triangle with vertices (0, 0), (0, 1), and (1, 0).  
You should get a value close to ``2 + math.sqrt(2)`` (3.414214).

Lists as function parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we are going to practice writing functions that take lists as 
parameters. Start by opening the file ``list_exercises.py`` in VS Code.

Lists are often parameters to functions. 
For example, we might want to write a function that answers a question about a list, 
a function that creates a new list based on an existing list, 
or a function that modifies an existing list. 

Let's write a function that counts the number of twos in a list. 

Again, we'll start with the header. Our function needs a name (``count_twos``
is a descriptive name) and it takes one parameter, the list.
We can write the docstring now, too. 

.. code-block:: python

   def count_twos(lst):
       """
       Count the number of twos in a list

       Input:
          lst (list): the list

       Returns (int): The number of twos in lst
       """

Now we can write the function body. 
First, we need to define a variable to count the number of twos in the list.
Then we iterate through the list (this is a good time to use a ``for`` loop).
Whenever we find a two in the list, we'll increment the counter.
And finally, we return the counter. 

.. code-block:: python

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

Before we're finished, we need to test our function. 
We can do that by initializing a few test lists in ``ipython3``, passing them to our function, and checking the output.

::

    In [18]: import list_exercises

    In [19]: lst1 = [1, 3, -5, 2, 8, 2]

    In [21]: lst2 = [1, 3, -5, 4, 8, 7]

    In [22]: list_exercises.count_twos(lst1)
    Out[22]: 2

    In [23]: list_exercises.count_twos(lst2)
    Out[23]: 0

    In [24]: list_exercises.count_twos([])
    Out[24]: 0

    In [25]: list_exercises.count_twos([2])
    Out[25]: 1

    In [26]: list_exercises.count_twos([3])
    Out[26]: 0
    

Looks good! Now it's your turn.

As a side note: "zero, one, many" is a good rule of thumb when testing
list functions.  That is, verify that the function behaves as expected
for the empty list, for a list with one element, and for a list with
multiple elements.


**Task 5**: Write a function ``are_any_true`` that takes a list of booleans 
and returns ``True`` if at least one of the entries in the list is ``True``, and ``False`` otherwise. 
Make sure to try your function with a few different lists, including one that doesn't contain any ``True`` values!

**Task 6**: Write a function ``add_lists`` that takes two lists of the same length as arguments 
and adds corresponding values together: ``[a[0] + b[0], a[1] + b[1], ...]``. 
The function should return a *new* list with the result of the addition. 
You can assume that the lists are of the same length. 

Test your function with lists that contain different types of elements.

* What happens if the elements are integers?  
* What happens when they are strings?  
* What happens if the lists are of mixed types (e.g., ``[5, "a", 3.4]``)?  
* What happens if both lists are empty?

**Task 7**: Write a function ``add_one`` that takes a list and adds ``1`` to each element in the list.  
This function should modify the input list, not create a new one.  
What values should ``a`` contain after passing it to ``add_one``?

.. code::

    a = [1, 2, 3, 4, 5]
    add_one(a)
    print(a)


Extended activity: Abstraction practice
---------------------------------------

One of the tasks in TT #1 was to take a list
containing values in the range from 0 to M inclusive, and create a new
list (let's call it ``frequencies``) in which element ``i`` contains
a count of the number of times the value ``i`` occurred in the input list.
That is, ``frequencies[i]`` would be a count of the number of times
that the value ``i`` occurred in the original list.  For example, given:

::

   lst0 = [0, 1, 1, 3, 2, 4, 6, 1, 7, 8]

the expected result is:

::

   [1, 3, 1, 1, 1, 0, 1, 1, 1]

The value ``0`` occurs once in ``lst0``, the value ``1`` occurs three
times in ``lst0``, the value ``5`` does not occur in ``lst0``, etc.

Here is a function that performs this task:

::

    def compute_frequencies(lst):
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

       # allocate space to hold the frequencies
       frequencies = [0] * (max(lst) + 1)
       
       for val in lst:
           frequencies[val] = frequencies[val] + 1

       return frequencies

To compute the result, we first allocate a list of zeros that is large
enough to have an entry for every value between ``0`` and the maximum
value in the list. (We use ``max(lst) + 1`` as the size of the
``frequencies``, rather than ``max(lst)`` to give us an entry for the
largest value in the list.)  And then, we walk through the values in
the original list updating the appropriates entries in ``frequencies``
as we go.  And finally, we return the computed list of frequencies.

Now we are going to look at a function, ``find_most_frequent_values``
that takes a list and returns a list with the value or values that
occur most often in the input list.  We chose to have our function
return a list to handle the case of ties.

Here are some sample uses:

::

    In [1]: import min_max                                                          

    In [2]: lst0 = [0, 1, 1, 3, 2, 4, 6, 1, 7, 8]                                    

    In [3]: min_max.compute_frequencies(lst0)                                              
    Out[3]: [1, 3, 1, 1, 1, 0, 1, 1, 1]

    In [4]: min_max.find_most_frequent_values(lst0)                                   
    Out[4]: [1]

    In [5]: lst1 = [0, 1, 1, 3, 2, 4, 6, 1, 7, 8, 6, 6]                               

    In [6]: min_max.compute_frequencies(lst1)                                           
    Out[6]: [1, 3, 1, 1, 1, 0, 3, 1, 1]

    In [7]: min_max.find_most_frequent_values(lst1)                                   
    Out[7]: [1, 6]

In the first call, the value ``1`` occurs most often in ``lst0`` and so,
the result is ``[1]``.  In the second example, there is a a tie, both
``1`` and ``6`` occur three times in ``lst1`` and so the result is ``[1,
6]``.

We will start by using ``compute_frequencies`` to determine how
frequently each value occurs. Then we will determine the largest
frequency and use that to find the values that occur most often.
Recall that each index in the list of frequencies corresponds to a
value in the range 0 to M (inclusive).

::

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

	# Determine how frequently most frequent
        # value(s) occurs.
        frequencies = compute_frequencies(lst)
        max_freq = max(frequencies)

	# Find all the values that occur max_freq times
        rv = []
        for i, freq in enumerate(frequencies):
            if freq == max_freq:
                rv.append(i)

        return rv

   
**Task 8**: Your first task in this part is to write a function that computes the
value or values that occur *least* frequently.  You can start by making
a copy of the function ``find_most_frequent_values``. Rename the copy
``find_least_frequent_values`` and replace the code that computes the
largest frequency with code that computes the smallest non-zero
frequency.

Careful: if there is a zero in the list of frequencies,
calling the ``min()`` function on that list will return zero. Before
finding the smallest frequency, you need to make sure you've filtered
out the zeroes in the list of frequencies.

That said, after your modifications, the code for ``find_least_frequent_values``
should be nearly identical to the code for ``find_most_frequent_values``.

Here are some sample uses of this function:

::

    In [12]: lst0                                                                     
    Out[12]: [0, 1, 1, 3, 2, 4, 6, 1, 7, 8]

    In [13]: min_max.find_least_frequent_values(lst0)                                 
    Out[13]: [0, 2, 3, 4, 6, 7, 8]

    In [14]: lst1                                                                      
    Out[14]: [0, 1, 1, 3, 2, 4, 6, 1, 7, 8, 6, 6]
    
    In [15]: min_max.find_least_frequent_values(lst1)
    Out[15]: [0, 2, 3, 4, 7, 8]

    In [16]: lst2
    Out[16]: [2, 2, 2, 1, 1, 2, 2, 2]

    In [17]: min_max.find_least_frequent_values(lst2)
    Out[17]: [1]

Notice that many values in ``lst0`` and ``lst1`` occur exactly once.

Much of the code in ``find_most_frequent_values`` and
``find_least_frequent_values`` is the same and, in particular,
both functions have code that finds the indices
of the elements in the list that match a particular value.  In the case of
``find_most_frequent_values``, we use this code:

::

    # Find all the values that occur max_freq times.
    rv = []
    for i, freq in enumerate(frequencies):
        if freq == max_freq:
            rv.append(i)

to find the indices of the elements in ``frequencies`` that match
``max_freq``.  You should have very similar code in
``find_least_frequent_values``.

**Task 9**: Your next task is to abstract this code into a function that can find
the indices of the elements in a list that match some specified value.
For example, we might want to find all the spots in the list that hold
the value ``2`` (i.e., find all the numbers with a frequency of ``2``).

The work required to create this new function is as
follows:

* create a function header,
* write a docstring,
* copy the block of code above,
* update the code to use the parameters instead of ``frequencies`` and ``max_freq``,
* update the loop variables to have names that match the more general context, and
* add a statement to return the result.

Once you have written your function, try it out in ``ipython3`` with
some sample values.

Once you are sure it works, replace the relevant lines in
``find_most_frequent_values`` and ``find_least_frequent_values`` with
calls to the your new function.  Note that your implementations of
these functions will still call ``compute_frequencies`` and will still
compute the maximum (minimum) frequency.  The ``for`` loop and associated
code, however, will be replaced with a call to your new function.

This process of abstracting a block of code into a function is
something you will do over and over again as you write code for this
class and in the future.


When finished
-------------

Once you finish working on the tutorial, you should add, commit, and push
the files in the ``tt2`` directory. No, we won't be looking at them or grading
then, but this ensures you can access those files later on if you start
working on a different computer, and also allows us to look at them if you
do have any specific questions about your solutions.

