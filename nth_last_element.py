class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
    i = 1
	data = -1
    def __init__(self, head):
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
            
    def find_nth_last_element(self, head, n):
		if head == None:
			return
		self.find_nth_last_element(head.next, n)
		print(self.i, head.data)
		if self.i == n:
			self.i += 1
			self.data =  head.data
			return
			
		self.i += 1
		return self.data
        
        
print(" **** Finding the nth last element in the linked list **** ")

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

print("Enter the nth last position: ")
n = int(input())

print("The nth last element is", linked_list.find_nth_last_element(linked_list.head, n))
