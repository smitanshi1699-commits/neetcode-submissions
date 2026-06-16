# #Definition for singly-linked list.
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#     def print_list(self):
#         current = self.head
#         output = ""
#         while current is not None:
#             output+= str(current.data)
#             current = current.next
#             if current is not None:
#                 output += "->"
#     def insert(self ,new_data):
#         new_node = Node(new_data) 
#         if self.head is None:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node
#     def delete(self,new_key):
#         if self.head is None:
#             print("List is empty")
#             return
#         current = self.head
#         previous = None
#         while current is not None:
#             if current.data == new_key:
#                 if previous is None:
#                     self.head = current.next
#                 else:
#                     previous.next = current.next
#                 return
#             else:
#                 previous = current
#                 current = current.next
#         print("key not FOUND")
#         return

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
        
        