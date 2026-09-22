class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        # Find the middle of the linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        current = slow

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Compare first half and reversed second half
        first = head
        second = prev

        max_sum = 0

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum