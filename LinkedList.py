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

	# position is 0 based
	def add_at(self, data, position):
		new_node = ListNode(data)

		if position < 0:
			print("Invalid position - " + str(position))
			return

		if position is 0:
			new_node.next = self.head
			self.head = new_node
			return

		temp = self.head
		count = 1
		while temp is not None and count < position:
			temp = temp.next
			count += 1

		if count is not position or temp is None:
			print("Invalid position - " + str(position))
		else:
			current_next = temp.next
			temp.next = new_node
			new_node.next = current_next

	def print_list(self):
		temp = self.head

		while temp is not None:
			print(str(temp.data))
			temp = temp.next


