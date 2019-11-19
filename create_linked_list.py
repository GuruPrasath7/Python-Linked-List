class Node:
	def __init__(self, data):
        """ The structure of a node of a linked list """
		self.data = data
		self.next = None
    
class LinkedList:
    def __init__(self, head):
        """ The current pointer only should be moved, not head. """
        self.head = None
        self.current = None

linked_list = LinkedList()

""" Inserting the head of the linked list """
head = Node(1)
linked_list.head = head
linked_list.current = linked_list.head

""" Inserting the second element by linking it with the first element """
second = Node(2)
linked_list.current.next = second
linked_list.current = second

""" Inserting the third element by linking it with the second element """
third = Node(3)
linked_list.current.next = third
linked_list.current = third
