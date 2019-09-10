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
        The proposed solution is having two lists:
            - The first list has on each position the product of all prefixes
            - The second list has on each position the product of all sufixes
            - The result list
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

def solution_without_division(nums):
    # Generate prefix products
    prefix_products = []
    # Iterate over list of nums: O(N)
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    # Iterate over list of nums: O(N)
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    # Iterate over a range of len(nums): O(N)
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result


if __name__ == '__main__':
    print solution_with_division([1,2,3,4,5])
    print solution_without_division([1,2,3,4,5])