from LinkedList import LinkedList

linked_list = LinkedList()

linked_list.add(2)
linked_list.add(4)
linked_list.add(6)
linked_list.add(1)

linked_list.print_list()
print("========================")

linked_list.add_at(10, 1)

linked_list.print_list()
print("========================")

linked_list.add_at(20, 3)

linked_list.print_list()
print("========================")

linked_list.add_at(50, 0)
linked_list.print_list()
print("========================")

linked_list.add_at(100, 7)
linked_list.print_list()
print("========================")

linked_list.delete_last()
linked_list.print_list()
print("========================")

linked_list.delete_last()
linked_list.print_list()
print("========================")

print("MY EDIT")
