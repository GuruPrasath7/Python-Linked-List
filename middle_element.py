class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	mid_data = 0 
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
	
    def find_mid_element(self, single, double):
		if double.next is None:
			self.mid_data = single.data
			return 
		if double.next:
			self.find_mid_element(single.next, double.next.next)
		return self.mid_data
        
print(" **** Finding the middle element in the linked list **** ")

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

print("The middle element is", linked_list.find_mid_element(linked_list.head, linked_list.head))
