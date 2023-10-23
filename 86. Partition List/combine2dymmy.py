class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
node3 = ListNode(3)
node2 = ListNode(2,node3)
node1 = ListNode(1,node2)
"""
dummyL = ListNode(-101)
pL = dummyL
while pL:
   pL = pL.next

node9 = ListNode(9)
dummyH = ListNode(101,node9)
    
dummyH = dummyH.next
dummyL = dummyL.next
pL = dummyH

