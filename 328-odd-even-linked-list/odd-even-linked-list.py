class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:

        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            # Connect odd nodes
            odd.next = even.next
            odd = odd.next

            # Connect even nodes
            even.next = odd.next
            even = even.next

        # Attach even list after odd list
        odd.next = even_head

        return head