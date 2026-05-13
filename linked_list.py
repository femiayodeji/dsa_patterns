class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __str__(self):
        node = self
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return str(result)

    def reverse_list_brute(self, node = None):
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

    def reverse_list_optimal(self, node = None):
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

        
if __name__ == "__main__":
    # Create individual nodes
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    # Link them together
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print(head.reverse_list_brute())
    print(head.reverse_list_optimal())