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


# Example 4: 392. Is Subsequence.
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string,
# while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

def is_subsequence(x):

    left = 0
    right = left+1

    b = "abcde"

    while right < len(x):
        if b.index(x[left]) < b.index(x[right]):
            left += 1
            right += 1
        elif b.index(x[left]) > b.index(x[right]):
            return False

    return True


print(is_subsequence("a"))


# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
# https://leetcode.com/problems/squares-of-a-sorted-array/

def is_sorted(a):
    left = 0
    right = len(a) - 1
    x = [0] * len(a)
    i = right

    while i >= 0:
        if abs(a[left]) > abs(a[right]):
            x[i] = (a[left]*a[left])
            left += 1
        else:
            x[i] = (a[right]*a[right])
            right -= 1

        i -= 1

    return x

print(is_sorted([-2,-1,0,2,3]))
