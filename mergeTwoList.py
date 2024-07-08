# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to serve as the starting point of the merged list
        head = ListNode(0)
        # 'curr' will point to the last node in the merged list as we build it
        curr = head

        # Iterate while neither list is exhausted
        while list1 is not None and list2 is not None:
            # Compare the values of the current nodes of both lists
            if list1.val <= list2.val:
                # If the value of list1's node is smaller or equal, append it to the merged list
                curr.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # If the value of list2's node is smaller, append it to the merged list
                curr.next = list2
                # Move to the next node in list2
                list2 = list2.next
            # Move 'curr' to point to the last node in the merged list
            curr = curr.next

        # If one of the lists is exhausted, append the remaining nodes of the other list
        if list1 is not None:
            curr.next = list1
        else:
            curr.next = list2

        # Return the merged list, starting from the node after the dummy node
        return head.next


def do(a):
    cur = ListNode()
    prev = ListNode()
    h = prev
    for i in a:
        cur.val = i
        prev.next = cur
        prev = cur
        cur = ListNode()
    return h.next
    
i1 = [1,2,4]
i2 = [1,3,4]
a = 0

l1 = do(i1)
l2 = do(i2)
print(Solution.mergeTwoLists(a,l1,l2))    