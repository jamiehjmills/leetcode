class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # first, make sure we don't lose the next node
        curr.next = prev  # reverse the direction of the pointer
        prev = curr  # set the current node to prev for the next node
        curr = next_node  # move on

    return prev


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

one.next = two
two.next = three
three.next = four

head = one

result = reverse_list(head)

while result:
    print(result.val)
    result = result.next
