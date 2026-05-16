class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2 = head, head
        i = 0

        while p2:
            if i > n:
                p1 = p1.next

            if p2.next is None:
                # removing head only when n == length
                if i + 1 == n:
                    return head.next

                p1.next = p1.next.next
                return head

            p2 = p2.next
            i += 1

        return head