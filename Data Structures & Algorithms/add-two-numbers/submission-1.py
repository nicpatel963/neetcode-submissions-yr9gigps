# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode()
        curr = ansHead
        ans,remainder = 0,0
        while l1 or l2:
            if l1 and l2:
                ans = (l1.val + l2.val + remainder)
            elif l1:
                ans = l1.val + remainder
            elif l2:
                ans = l2.val + remainder
            remainder = 0 if ans < 10 else ans // 10
            ans = ans if ans < 10 else ans%10
            curr.next = ListNode(ans)
            print(curr.val,curr.next.val)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if remainder > 0:
            curr.next = ListNode(remainder)
        return ansHead.next