# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head):
        node = ListNode()
        ret = node
        temp = 0
        flag = False
        while (head):
            if flag:
                temp += head.val
                if head.val == 0:
                    flag = False
                    node.val = temp
                    node.next = ListNode()
                    node = node.next
                    temp = 0
            if head.val == 0:
                flag = True
            head = head.next
        node = ret
        while (node.next.next):
            node = node.next
        node.next = None
        return ret


nodes = ListNode(0,
                 ListNode(3,
                          ListNode(1,
                                   ListNode(0,
                                            ListNode(4,
                                                     ListNode(5,
                                                              ListNode(2,
                                                                       ListNode(0))))))))
ans = Solution().mergeNodes(nodes)
while (ans):
    print(ans.val)
    ans = ans.next
