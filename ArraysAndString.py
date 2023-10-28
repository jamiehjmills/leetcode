# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4501/

# Example 1: Given a string s, return true if it is a palindrome, false otherwise.

def check_if_palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            print("no")
            return False
        left += 1
        right -= 1

#check_if_palindrome("test")

# Example 2: Given a sorted array of unique integers and a target integer,
# return true if there exists a pair of numbers that sum to target, false otherwise.
# This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
#
# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

def find_target_array(s, target):

    left = 0
    right = len(s) - 1

    while left < right:

        if (s[left] + s[right]) > target:
            right -= 1
        elif (s[left] + s[right]) < target:
            left += 1
        elif (s[left] + s[right]) == target:
            print('{0},{1}'.format(right, left))
            return True

find_target_array([1, 2, 4, 6, 8, 9, 14, 15] , 13)
