# Definition for singly-linked list.

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):

        slow = head

        # 1 1 2 3 3

        while slow != None and slow.next != None:
            if slow.val == slow.next.val:
                slow.next = slow.next.next
            else:
                slow = slow.next


        return head


