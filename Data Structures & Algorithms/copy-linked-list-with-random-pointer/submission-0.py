"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        myHashMap = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            myHashMap[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = myHashMap[curr]
            copy.next = myHashMap[curr.next]
            copy.random = myHashMap[curr.random]
            curr = curr.next
        return myHashMap[head]