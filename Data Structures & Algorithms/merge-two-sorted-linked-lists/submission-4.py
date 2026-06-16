# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        orange = list1
        blue = list2
        dummy = ListNode(0)
        tail = dummy
        while orange is not None and blue is not None:
            if orange.val <= blue.val:
                tail.next = orange
                orange = orange.next
            else :
                tail.next = blue
                blue = blue.next
            tail = tail.next
        tail.next = orange or blue
        return dummy.next
        
        