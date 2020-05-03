
""" 2. Build graph
-nodes: parents /child
-edges: relationship between parent/child
-directed: parent can only be parent, child can only be child
-acyclic
- node on avg connected to more than 1/2 other nodes?: sparse
- DFS- find the farthest relationship/path

Given the dataset and the ID of an
individual in the dataset, returns their earliest known
ancestor – the one at the farthest distance from the input
individual.

If there is more than one ancestor tied for "earliest",
return the one with the lowest numeric ID.

If the input individual has no parents, the function should
return -1.

#if vertext has no more neighbors


Assuming a bit more memory usage is not a problem and if the first
item of your tuple is hashable, you can create a dict out of your
list of tuples and then looking up the
value is as simple as looking up a key from the dict

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
^ if has children, it is in ancester[tuple#][0]
^ if has parent it is in ancester[tuple#][1], if start is not in ancester[i][1], has no parent
^ track through list to check of parent has parent
^ once parent no longer has parent, return that vertex, thats the farthest ancestor

^ Extra:count the number of times its in ancester[i][1] == number of ancestors
 """


from util import Stack, Queue


def get_parents(ancestors, start):
    arr_par = []
    for i in range(len(ancestors)):
        print("get parents", start, ancestors[i], ancestors[i][1])
        if start == ancestors[i][1]:
            print("start found", start, ancestors[i][1])
            arr_par.append(ancestors[i][0])

    if len(arr_par) > 0:
        return arr_par
    else:
        return None


def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    s.push([starting_node])
    visited = set()

    # ancestors=[(), ()] is list of sets/tuples
    while s.size() > 0:
        # Pop the vertex from back/end of stack, keeps check all in stack in order
        path = s.pop()
        a = path[-1]  # last element in list
        stack_size = s.size()

        if a not in visited:  # only explore that node if not yet explored
            visited.add(a)
            amount_parents = len(visited)
            print("popped", a, "path", path, visited,
                  stack_size, s, amount_parents)
            find_parents = get_parents(ancestors, a)
            # if find parents exist, add parents to stack
            if find_parents is not None:
                # needs to return list of parents
                for parent in get_parents(ancestors, a):
                    path_copy = path.copy()

                    if parent is not None:
                        # each parent of 6 added [6, 5, 3 ] 3 is popped & check for parent
                        print("parent", parent)
                        path_copy.append(parent)
                    # [6,3,5] 3 or 5 is popped
                    # check for neighbor of 3 or 5,
                    # add parents of 3 to stack [6, 5, 2, 1]
                    # pop off 1
                    # check for parents of 1
                        s.push(path_copy)
                    # return negative one, if only one node was enqued& popped (resulting in len(visited)==1), & find_parent returns none
            if find_parents is None and stack_size == 0 and amount_parents == 1:
                return -1
            if find_parents is None and stack_size == 0 and amount_parents > 1:
                return a
            # returns smaller parent by default, since parents in tupls are sorted by
            # the smaller parent will always be popped last, since stack
            # pops by last in (larger parent appended last)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 6))


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterate through ...
        # do some logic based on the root val as iterate
        while root:
            if max(p.val, q.val) < root.val:
                # for search move the root left (search smaller), if the MAX of the p&q are < root
                root = root.left
            elif min(p.val, q.val) > root.val:
                # move search to right(search larger) if MIN of p&q are > root
                root = root.right
            else:
                # if max or min bounds are correctly greater & correctly less than root.value
                # than can be ancestor
                return root
        return None


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
#         stack=[]
#         stack.append([root])
#         res=[]
        
#         while len(stack) > 0:
#             path=stack.pop()
#             v=path[-1]
#             if v is not None:
#                 res.append(v.val)
            
#             if v and v.children is not None:
#                 for child in v.children[::-1]:
#                     path_copy=path.copy()
#                     path_copy.append(child)
#                     stack.append(path_copy)
            
            
            
#         print(f"{res}")
            
#         return res

        if not root:
            return []
        if not root.children:
            return [root.val]
        l=[]
        #dfs sorts by parent, then child, then next parent in bfs span
        for child in root.children:
            l+=self.preorder(child)
        
        
        l.insert(0,root.val)
        return l

        class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        #stack of path for left node & stack of path for right node
        def findChildren(root):
            res=[]
            if root:
                if root.left:
                    res.append(root.left)
                if root.right:
                    res.append(root.right)
                if len(res) > 0:
                    return res
                else:
                    return None
        
        def dfs(root,res):
        
            stack = []
            stack.append([root])
        
            while len(stack) >0:
                path= stack.pop()
                
              
                res.append(path)
                v=path[-1]
        
                if findChildren(v) is not None:  
                    for child in findChildren(v):
                        path_copy=path.copy()
                        path_copy.append(child)
                        stack.append(path_copy)
      
            return res
        
        
        if root is None: 
            return 0
        if root.left is None and root.right is None :
            return 0
        
        resL=[]
        resR=[]
        max_lenL=[]
        max_lenR=[]
        if root:
            l=dfs(root.left,resL)
            r=dfs(root.right, resR)
        
        print(f" LEFTl: {l}\n RIGHT: {r} {r[-1]}")
        
    
        if len(l) == 1 and l[-1] == [None]:
            print("l is none")
           
            for i in range(len(r)):
                max_lenR.append(len(r[i]))
            return max(max_lenR)
        
        elif len(r) == 1 and r[-1] == [None]:
            print("r is none")
            
            for i in range(len(l)):
                max_lenL.append(len(l[i]))
            print(f"R is none max: {max(max_lenL)}")
            return max(max_lenL)
        
        elif len(l) >=1 and len(r) >=1:
            print("equals")
            for i in range(len(l)):
                max_lenL.append(len(l[i]))
            for i in range(len(r)):
                 max_lenR.append(len(r[i]))
                    
            max_len=max(max_lenL) + max(max_lenR)
            print(f"maxL {max_lenL} maxR {max_lenR}")
            return max_len
        
       