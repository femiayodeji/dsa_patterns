class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __str__(self):
        node = self
        result = []
        seen = set()
        while node:
            if id(node) in seen:
                result.append("~")
                break
            seen.add(id(node))
            result.append(node.val)
            node = node.next
        return str(result)

    def reverse_brute(self, node = None):
        if node is None:
            node = self

        values = []
        while node:
            values.append(node.val)
            node = node.next
        
        dummy = ListNode(None)
        cur = dummy
        for i in range(len(values) - 1, -1, -1):
            num = values[i]
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next

    def reverse_optimal(self, node = None):
        if node is None:
            node = self

        prev = None
        cur = node
        
        while cur:
            save = cur.next
            cur.next = prev
            prev = cur
            cur = save
        return prev

    def merge_brute(self, node2):
        if node2 is None:
            return self
        node1 = self

        values = []
        while node1:
            values.append(node1.val)
            node1 = node1.next
        while node2:
            values.append(node2.val)
            node2 = node2.next
        values.sort()
        
        dummy = ListNode(None)
        cur = dummy
        for num in values:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next

    def merge_optimal(self, node2):
        if node2 is None:
            return self
        node1 = self

        dummy = ListNode(None)
        cur = dummy
        while node1 and node2:
            if node1.val <= node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next
        cur.next = node1 or node2
        return dummy.next

    def remove_at_end_brute(self, node, n):
        if node is None:
            node = self
        length = 0
        cur = node
        while cur:
            length += 1
            cur = cur.next
        
        if length == n: 
            return node.next
        
        cur = node
        for i in range(1, length - n):
            cur = cur.next
        cur.next = cur.next.next
        return node

    def remove_at_end_optimal(self, node, n):
        if node is None:
            node = self

        slow = node
        fast = node
        
        for i in range(n+1):
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return node

    def has_cycle_brute(self, node = None):
        if node is None:
            node = self
            
        seen = set()
        
        cur = node
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        
        return False

    def has_cycle_optimal(node = None):
        if node is None:
            node = self

        slow = node
        fast = node
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True

        return False



if __name__ == "__main__":
    # Create individual nodes
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head2 = ListNode(1)
    node23 = ListNode(3)
    node24 = ListNode(4)
    node27 = ListNode(7)

    # Link them together
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    head2.next = node23
    node23.next = node24
    node24.next = node27
    # node27.next = node23


    print(head.has_cycle_brute(head2))
