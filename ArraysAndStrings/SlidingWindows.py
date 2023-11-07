# Example 1: Given an array of positive integers nums and an integer k,
# find the length of the longest subarray whose sum is less than or equal to k.
# This is the problem we have been talking about above. We will now formally solve it.

k = [3,1,2,7,4,2,1,1,5]


def find_longest(k):
    left = 0
    right = 1

    target = 8

    ans = 0
    max = 0
    sum = k[left] + k[right]

    while right < len(k):
        if sum > target:
            while left < right and sum > target:
                sum -= k[left]
                max -= 1
                left += 1
        else:
            right += 1
            sum += k[right]
            max += 1


### Java ###

# nums = [3,1,2,7,4,2,1,1,5]

# public int findLength(int[] nums, int k) {
#     int left = 0;
#     int curr = 0; // curr is the current sum of the window
#     int ans = 0;
#
#     for (int right = 0; right < nums.length; right++) {
#         curr += nums[right];
#         while (curr > k) {
#             curr -= nums[left];
#             left++;
#         }
#
#         ans = Math.max(ans, right - left + 1);
#     }
#
#     return ans;
# }

## TODO: copy the Java code above. 
