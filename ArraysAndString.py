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


# Example 3: Given two sorted integer arrays arr1 and arr2,
# return a new array that combines both of them and is also sorted.

def combine(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans


print(combine([2,5,7], [3,6,8,9]))

