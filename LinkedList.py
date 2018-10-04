from ListNode import ListNode

class LinkedList:

	def __init__(self):
		self.head = None

	def add(self, data):
		new_node = ListNode(data)

		if self.head is None:
			self.head = new_node
		else:
			temp = self.head
			while temp.next is not None:
				temp = temp.next
			temp.next = new_node

	def print_list(self):
		temp = self.head

		while temp is not None:
			print(str(temp.data))
			temp = temp.next


