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
        
        def insert(self, data, linked_list):
        	node = Node(data)
        	linked_list.current.next = node
	
    	def print_linkedList(self, head):
        	temp = head
        	while temp:
            		print(temp.data)
            		temp = temp.next
            
linked_list = LinkedList()

print("Enter the number of elements to be inserted in the linked list: ")
size = int(input())

print("Enter the elements to be inserted in the linked list: ")
i = 0
while i < size:
	element = int(input())
	if not linked_list.head:
		node = Node(element)
		linked_list.head = node
		linked_list.current = node
	else:
		node = Node(element)
		linked_list.current.next = node
		linked_list.current = node
	i+=1

print("The inserted linked list is: ")
linked_list.print_linkedList(linked_list.head)

