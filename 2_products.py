"""
    Problem:
        Given an array of integers, 
        return a new array such that each element at index i of the new array 
        is the product of all the numbers in the original array except the one at i.

        For example, if our input was [1, 2, 3, 4, 5], 
        the expected output would be [120, 60, 40, 30, 24]. 
        If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Solution 1: Using division
        First, i iterate over all elements to get the product of them.
        Then, iterate over all elements again while creating the result list.
        The result list contains on every position, the total divided by the element at the actual position

    Solution 2: Without using division
        I still didn't come up with a solution for this
"""

def multiply(elements):
    total = 1
    # O(N)
    for elem in elements:
        total *= elem
    return total

def solution_with_division(elements):
    total = multiply(elements)
    result = []
    # O(N)
    for elem in elements:
        result.append(total / elem)
    return result

def solution_without_division(elements):
    pass

if __name__ == '__main__':
    print solution_with_division([1,2,3,4,5])