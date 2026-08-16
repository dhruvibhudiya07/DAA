# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head:
            return None
        values = []
        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next
        values.sort()
        temp = head
        i = 0
        while temp:
            temp.val = values[i]
            i += 1
            temp = temp.next
        return head
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        