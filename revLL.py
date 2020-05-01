
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


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        # given 2 LL 
        # each node is int, written in reverse order
        # read in reverse each LL 
        # add the 2 LL (one total num) 
        
        # return sum as a LL
            # create a LL with sum answer
            # reverse the LL 
            
        num1=[]
        num2=[]
        
        curr1=l1
        curr2=l2
        
        while curr1 and curr2:
            if curr1 and curr2 is not None:
                num1.append(curr1.val)
                num2.append(curr2.val)
            curr1 = curr1.next
            curr2 = curr2.next
        # reverse & convert to 1 num
        rev1=num1[::-1]
        rev2=num2[::-1]
        # string
        n1= [str(i) for i in rev1]
        n2 =[str(i) for i in rev2]
        # join 
        num_1 = int("".join(n1))
        num_2= int("".join(n2))
        
        new_sum = str(num_1 + num_2)
        # reverse new sum
        # split new_sum into single nums
        new_sum = list(new_sum[::-1])
       
        # turn list into ints
        for i in range(len(new_sum)):
            # instead of creating new array
            new_sum[i] = int(new_sum[i])
        
        print(f"new_sum {(new_sum)}")
        
        # return LL with nodes in order of 7-0-8
        new_LL = ListNode(-1)
        curr = new_LL
        # print(f"CURR {curr}")
        # add ele of new_sum to new_LL tree as nodes
        track =0
        
        while track < len(new_sum):
            for i in range(0, len(new_sum)):
                print(f"ele: {new_sum[i]}")
                               
                # curr= ListNode(new_sum[i])
                curr.next=  ListNode(new_sum[i])
                print(f"c ={curr}")
                track+=1
                curr=curr.next 
        
       
        # get rid of dummyhead
        new_LL=new_LL.next
        return new_LL
        
        def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      
        print(f"Root {root}")
        def create_dict(root, my_dict):
            if root.left:
                
                create_dict( root.left, my_dict)
            
            my_dict[root.val] = [root.left, root.right]
           
           
            if root.right:
        
                create_dict( root.right, my_dict)
        
            print(f"DICT {my_dict}")
        
        #if leaves on left, finish listingthe 2 child of R element
        #list the 2 chid of the left leaf first
        #list 2 child of right leaf on Left section 
       
        my_dict ={}
        create_dict(root, my_dict)
        child_n= [p,q]
        for k in my_dict:
            if all(elem in child_n for elem.val in my_dict[k]):
                print(f"k {k}")
                return k
            
            
            
            class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #iterate through ...
        #do some logic based on the root val as iterate
        while root:
            if max(p.val, q.val) < root.val:
                #for search move the root left (search smaller), if the MAX of the p&q are < root
                root = root.left
            elif min(p.val, q.val) > root.val:
                #move search to right(search larger) if MIN of p&q are > root 
                root = root.right
            else:
                # if max or min bounds are correctly greater & correctly less than root.value 
                #than can be ancestor
                return root
        return None
          
            