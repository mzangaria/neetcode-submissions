class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # merge
        first, second = head, prev
        while second:
            nxt1 = first.next
            nxt2 = second.next

            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2