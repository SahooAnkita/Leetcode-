class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Map original node -> copied node
        node_map = {}

        # First pass: create all new nodes
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next

        # Second pass: connect next and random pointers
        current = head
        while current:
            copy = node_map[current]

            copy.next = node_map.get(current.next)
            copy.random = node_map.get(current.random)

            current = current.next

        return node_map[head]