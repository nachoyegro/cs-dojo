"""
    Problem:
        Given a list of numbers and a number k, 
        return whether any two numbers from the list add up to k.
        For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Solution 1:  
        I tried it with backtracking. Iterating over all elements, each time i have to make a decision:
        Does the actual number belongs to the solution? So i try it with the number as a part of the solution,
        and then try it with the number not being part of the solution

    Solution 2:
        Iterate over all elements of the list. 
        If the substraction of k and the actual element is in the set of already in the set of viewed numbers
        It means that the sum of that element and the actual, is k
"""

def sum_backtracking(k, numbers):
    if k == 0:
        #This means that at least two numbers sums k
        return True
    if not numbers:
        #If the list is empty, then this is not a good path
        return False
    i = numbers[0]
    #First, the solution with "i" as a part of it
    solution_with_number = sum_backtracking(k-i, numbers[1:])
    #Then, the solution without "i" as a part of it
    solution_without_number = sum_backtracking(k, numbers[1:])
    #If some solution sums k, then it should be True
    return solution_with_number or solution_without_number

def sum_n(k, lst):
    """
        O(N) since lookups of sets are O(1) each
    """
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False

if __name__ == '__main__':
    print sum_backtracking(17, [10, 15, 3, 7])
    print sum_n(17, [3, 15, 10, 7])
    