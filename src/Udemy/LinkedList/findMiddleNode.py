class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    # def find_middle_node(self):
    #     first = self.head
    #     second = self.head # this is not affecting
    #     print("before")
    #     print(id(self.head))
    #     print(id(first))
    #     print(id(second))
    #     counts = 0
    #     print("now printing..")
    #     while first != None:
    #         counts += 1
    #         print(id(first))
    #         first = first.next
    #
    #     print("after")
    #     print(id(self.head))
    #     print(id(first))
    #     print(id(second.next.next))
    #
    #     return second

    def find_middle_node(self):

        fast = self.head
        slow = self.head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow






my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print(my_linked_list.find_middle_node().value)
#my_linked_list.find_middle_node()

"""
    EXPECTED OUTPUT:
    ----------------
    3

"""
