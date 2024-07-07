# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carrybit = 0
    
        head = ListNode(0)
        curr = head
        while l1 is not None or l2 is not None or carrybit != 0:
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0 
            
            sum = temp1 + temp2 + carrybit
            carrybit = 0 

            if sum >= 10:
                sum -= 10
                carrybit = 1

            newNode = ListNode(sum)
            curr.next = newNode
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

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
    
i1 = [2,4,3]
i2 = [5,6,4]
a = 0

l1 = do(i1)
l2 = do(i2)
print(Solution.addTwoNumbers(a,l1,l2))    