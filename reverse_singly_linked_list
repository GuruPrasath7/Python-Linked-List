class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList: 
	def __init__(self):
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
        def reverse_linked_list(self, head):
		
		temp = head.next		
			
		reversed_list = head
		reversed_list.next = None

		while temp:
			to_be_attached = temp
			temp = temp.next
			
			to_be_attached.next = reversed_list
			reversed_list = to_be_attached
		
		return self.print_linkedList(reversed_list)

print(" **** Reverse the singly linked list **** ")

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

print("The Reversed Linked List is")
linked_list.reverse_linked_list(linked_list.head)
