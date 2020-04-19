def insertNodeAtPosition(head,data, position):
    pos = 0
    current_head = head
    previous_head = head
    while pos <= position:
        if pos == position:
            new_head = SinglyLinkedListNode(data)
            previous_head.next = new_head
            new_head.next = current_head
            return head
        else:
            pos += 1
            previous_head = current_head
            current_head = current_head.next
    return head
