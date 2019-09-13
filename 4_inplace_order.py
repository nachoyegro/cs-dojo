"""
    Problem: 
        Given an array of integers, 
        find the first missing positive integer in linear time and constant space. 
        In other words, find the lowest positive integer that does not exist in the array. 
        The array can contain duplicates and negative numbers as well.

        For example, the input [3, 4, -1, 1] should give 2. 
        The input [1, 2, 0] should give 3.

        You can modify the input array in-place.

"""


#This solution is O(N) in time and constant space
def first_missing_number(nums):
    #If the array is empty, the first missing number is 1
    if not nums:
        return 1
    #Iterate over index and element of the array
    for i, num in enumerate(nums):
        #Start swapping until the number i want in this position corresponds with the index
        #Or the number is not between 0 and len(nums)
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            #v is the number at index i
            #nums[v-1] is the number that is taking the place that corresponds "v"
            #So i swap them
            #The new "v" is the number that was taking place of the old "v"
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            #If the actual number is well positioned, then break the while
            if nums[i] == nums[v - 1]:
                break
    #Once the array is "ordered" by index
    #I iterate over it, until i find a number that does not correspond with its index + 1
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    #If all of them corresponds, the first number is len(nums) + 1
    return len(nums) + 1


#This solution is O(N) in time, but needs extra space to store the numbers in a set
def first_missing_number_set(nums):
    nums_set = set(nums)
    #In case every number is in the set, the position len(nums)+2 is not
    for i in range(1, len(nums)+2):
        if i not in nums_set:
            return i

if __name__ == '__main__':
    array = [3, 1, -1, 2, 0]
    array2 = [3,1,2,4]
    array3 = []
    assert first_missing_number_set(array) == 4
    assert first_missing_number_set(array2) == 5
    assert first_missing_number_set(array3) == 1