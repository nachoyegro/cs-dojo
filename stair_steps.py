"""
    Problem:
    There's a staircase with N steps, 
    and you can climb 1 or 2 steps at a time. 
    Given N, write a function that returns the number of unique ways you can climb the staircase. 
    The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:

        1, 1, 1, 1
        2, 1, 1
        1, 2, 1
        1, 1, 2
        2, 2

    What if, instead of being able to climb 1 or 2 steps at a time, 
    you could climb any number from a set of positive integers X? 
    For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. 
    Generalize your function to take in X. 


    Solution:
        I made three different solutions:
            - The first is a bad one, using only recurssion. It is bad because for some steps
                you calculate it twice or more times.
            - The second is a better one, assuming you can take one or two steps at a time.
                Using Dynamic Programming you store the result in an array of length number_of_steps + 1 
            - The third one is like the second solution, but with variable number of steps
"""


def num_ways_bad(number_of_steps):
    """
        Recursive solution
        num_ways_bad(number_of_steps-2) is calculated at least twice 
    """
    if number_of_steps==0 or number_of_steps==1:
        return 1
    else:
        return num_ways_bad(number_of_steps-1) + num_ways_bad(number_of_steps-2)



def num_ways_one_or_two_steps(number_of_steps, steps):
    if number_of_steps == 0 or number_of_steps == 1:
        return 1
    #Possibilities by taking one step + possibilities by taking two steps at a time
    return steps[number_of_steps-1] + steps[number_of_steps-2] 

def solution_one_or_two_steps(number_of_steps):
    steps = [0]*(number_of_steps+1)
    for i in range(number_of_steps+1):
        steps[i] = num_ways_one_or_two_steps(i, steps)
    return steps[number_of_steps]



def num_ways_x_steps(number_of_steps, X, steps):
    if number_of_steps == 0:
        #Now i can't assume that i can go from step 0 to step 1
        return 1
    total = 0
    for x in X:
        if x <= number_of_steps:
            # If i can take x steps
            total += steps[number_of_steps - x]
    return total

def solution_x_steps(number_of_steps, X):
    steps = [0]*(number_of_steps+1)
    for i in range(number_of_steps+1):
        steps[i] = num_ways_x_steps(i, X, steps)
    return steps[number_of_steps]
    
if __name__ == '__main__':
    for i in range(5):
        print 'The bad solution of {} for one or two steps is {}'.format(i, num_ways_bad(i))
        print 'The good solution of {} for one or two steps is {}'.format(i, solution_one_or_two_steps(i))
        print 'The solution of {} for steps {} is {}'.format(i, [1, 2, 3], solution_x_steps(i, [1,2,3]))