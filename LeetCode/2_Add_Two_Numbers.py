class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        i = 0
        while (l1 is not None):
            num1 += l1.val * (10 ** i)
            i += 1
            l1 = l1.next
        i = 0
        while (l2 is not None):
            num2 += l2.val * (10 ** i)
            i += 1
            l2 = l2.next
        l3 = ListNode()
        l3_head = l3
        for num in str(num1 + num2)[::-1]:
            l3.val = int(num)
            l3.next = ListNode()
            l3 = l3.next
        l3 = l3_head
        while (l3.next.next is not None):
            l3 = l3.next
        l3.next = None
        return l3_head

l1 = ListNode(5, ListNode(6))
l2 = ListNode(5, ListNode(4, ListNode(9)))
print(Solution().addTwoNumbers(l1, l2).next.next.next.next.val)
