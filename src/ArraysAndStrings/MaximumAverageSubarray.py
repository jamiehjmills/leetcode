
# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4594/
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


nums = [1,12,-5,-6,50,3]
k = 4

def findMaxAverage(nums, k):

    subMax = 0
    max = 0
    count = 0
    newCount = 0

    for index, item in enumerate(nums):
        left = index
        print("index")
        print(left)

        while(newCount < k and left < len(nums)):
            newCount = count + left
            print("newCount")
            print(newCount)
            subMax = subMax + nums[newCount]
            count = count + 1

        if max < subMax:
            max = subMax

        subMax = 0
        count = 0

    return max

print(findMaxAverage(nums, 4))

### TODO: need to make it average
