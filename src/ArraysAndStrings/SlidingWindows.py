# Example 1: Given an array of positive integers nums and an integer k,
# find the length of the longest subarray whose sum is less than or equal to k.

nums = [3,1,2,7,4,2,1,1,5]

def find_longest(nums, k):

    left = 0
    right = 0
    curr = 0
    answer = 0

    for index, item in enumerate(nums):
        right = index
        curr += nums[right]
        while(curr > k):
            curr -= nums[left]
            left += 1

        answer = max(answer, right-left+1)

    return answer


print(find_longest(nums, 4))




