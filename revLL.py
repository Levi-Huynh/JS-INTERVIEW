   
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

        class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # get most left
        
        if not root:
            return root
        
        curr= root
        while curr.left:
            #iterate
            curr = curr.left
        
        #curr should be most left here
        #curr = root
        #return left, null in betweeen each & r, sorted 
        #root now is most left curr 
        root = curr
        print(f"test {root.left}. c: {curr}")
        while curr.left and curr.right:
            for i in range(0, 10):
               
                curr.left= None
                curr.right= #
            curr = curr.right 
        
        return curr
