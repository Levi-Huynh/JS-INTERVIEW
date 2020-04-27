
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head is not None:
            # temp var for head.next
            next_node = head.next
            # set actual head.next to prev value (iterate)
            head.next = prev
            # iterate prev to head
            prev = head
            # iterate head to next
            head = next_node
        # return prev based on standout/output
        return prev

        class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        # get most left

        if not root:
            return root

        curr = root
        while curr.left:
            # iterate
            curr = curr.left

        # curr should be most left here
        # curr = root
        # return left, null in betweeen each & r, sorted
        # root now is most left curr
        root = curr
        print(f"test {root.left}. c: {curr}")
        while curr.left and curr.right:
            for i in range(0, 10):

                curr.left = None
                curr.right =
            curr = curr.right

        return curr

 def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        
        # [root, left(< root), right (> root), left(left less than leftchild), left(right null/grater than righ child), right(left), right(left=none)]
        
         
        # root index should be middle of list?
        root_index = int(math.floor(len(nums)/2))
        new_root = nums[root_index]
        print(f" new_root{new_root}")
        great_val=[]
        lesser_val=[]
        res=[]
        # res.append(new_root)
        for i in range(len(nums)):
            # check to see if total values that are greater than root & lesser than root, don't differ by more than 1
            # else not blalnce 
            if nums[i] > new_root:
                print(f"greater {nums[i]}")
                great_val.append(nums[i])
            if nums[i] < new_root:
                print(f"lesser {nums[i]}")
                lesser_val.append(nums[i])
            
        diff = abs(len(great_val) - len(lesser_val))
        if diff > 1:
            return None
            
        # sort great_val and lesser_val
        lesser_val.sort(reverse=True)
        great_val.sort(reverse=True)
        print(f"SORT {lesser_val}, {great_val}")    
        queue = []
        queue.append(new_root)
        while len(queue) >0 :
            curr= queue.pop(0)
            print(f"C {curr}")
            if curr not in res:
                res.append(curr)
            if len(lesser_val) > 1:    
                val =lesser_val.pop(0)
            else:
                val = lesser_val[-1]
            if val < curr and val not in res:
                print(f"val less {val}")
                queue.append(val)
            if len(great_val) >1: 
                val2 = great_val.pop(0)
            else:
                val2 = great_val[-1]
            if val2> curr and val2 not in res:
                print(f"val great{val2}")
                queue.append(val2)
        
        print(f"HERE res{res}")
        return res    
