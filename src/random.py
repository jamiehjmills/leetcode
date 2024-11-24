print("hi")
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

nums = [1,1,1,2,2,2,3,3]
left = 0
right = 0
counts = 0

index = 1 #2
occurance = 1 #3

# [1,1,1,2,2,3]

for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        occurance += 1
    else:
        occurance = 1

    if occurance <= 2:
        nums[index] = nums[i]
        index += 1

return index



