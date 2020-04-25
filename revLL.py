   
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head is not None:
            #temp var for head.next
            next_node = head.next
            #set actual head.next to prev value (iterate)
            head.next = prev
            #iterate prev to head
            prev = head
            #iterate head to next
            head = next_node 
        #return prev based on standout/output
        return prev