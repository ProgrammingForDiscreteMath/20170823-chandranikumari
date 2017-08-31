"""
This is the code file for Assignment from 23rd August 2017.
This is due on 30th August 2017.
"""
##################################################
#Complete the functions as specified by docstrings


# 1

def entries_less_than_ten(L):
    """
    Return those elements of L which are less than ten.

    Args:
        L: a list

    Returns:
        A sublist of L consisting of those entries which are less than 10.
    """
    T=[]
    for i in L:
        if i<10:
            T.append(i)
    return T
    #Add your code here

#print (entries_less_than_ten([2, 13, 4, 66, -5]))

#Test
#print entries_less_than_ten([2, 13, 4, 66, -5]) == [2, 4, 6, -5]

# 2

def number_of_negatives(L):
    """
    Return the number of negative numbers in L.

    Args:
        L: list of integers

    Returns:
        number of entries of L which are negative
    """
    #pass ##YOUR CODE REPLACES THIS
    count=0
    for i in L:
        if (i<0):
            count=count+1
    return count
        

# TEST
#print number_of_negatives([2, -1, 3, 0, -1, 0, -45, 21]) == 3

# 3
def common_elements(L1, L2):
    """
    Return the common elements of lists ``L1`` and ``L2``.

    Args:
        L1: List
        L2: List

    Returns:
        A list whose elements are the common elements of ``L1`` and
        ``L2`` WITHOUT DUPLICATES.
    """
    #pass # your code goes here
    L3=[]
    for i in L1:
        if i not in L3:
            for j in L2:
                if (i==j):
                    L3.append(i)
                    break
                
    return L3

#TEST
#common_elements([1, 2, 1, 4, "bio", 6, 1], [4, 4, 2, 1, 3, 5]) == [1, 2, 4]

#4
def fibonacci_generator():
    """
    Generate the Fibonacci sequence.

    The Fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21,...
    is defined by a1=1, a2=1, and an = a(n-1) + a(n-2).
    """
    a, b = 0, 1
    while True:
        yield a
        """Instead of ``yeild a`` we can have ``yeild b`` also both will serve the same
        """
        a, b = b, a + b
  
    # Hint: use the ``yield`` command.

#TEST
#f = fibonacci_generator()
#[f.next() for i in range(10)] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#5
def largest_fibonacci_before(n):
    """
    Return the largest Fibonacci number less than ``n``.
    """
    #Your code goes here.
    l=0
    f=fibonacci_generator()
    while True:
        t=l
        l=f.next()
        if (l>n-1):
            break
    return t   

#TEST
#largest_fibonacci_before(55) == 34

#6
def catalan_generator():
    n=0
    while True:     
        c=(factorial(2*n))/(factorial(n)*factorial(n+1))
        yield c
        n+=1
    
    """
    Generate the sequence of Catalan numbers.

    For the definition of the Catalan number sequence see `OEIS <https://www.oeis.org/A000108>`.
    """
    #Your code goes here.
        
#TEST
#c = catalan_generator()
#[c.next() for i in range(10)] == [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]

    
    
#7
### CREATE YOUR OWN FUNCTION. Make sure it has a nice docstring.
# See https://www.python.org/dev/peps/pep-0257/
# for basic tips on docstrings.

def factorial(n):
    """
    Calculate the factorial of a number passed in argument using recursion.
    
    A recursive function is a function that calls itself during its execution.

    """
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1)) # calling its same function hence recursion

