def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if head is None: 
            new_node.next = head 
            head = new_node 
  
        # Special case for head at end 
    elif head.data > new_node.data: 
            new_node.next = head 
            head = new_node 
  
    else : 
  
        # Locate the node before the point of insertion 
        current = head 
        #iterate only if curr < new_node, and curr is not None
        while(current.next is not None and
            current.next.data < new_node.data): 
            current = current.next
            
        #make whatever would have been after current, updated to be after new_node
        new_node.next = current.next
        #make new node next since its greater than current
        current.next = new_node 
    return head
        