

def deleteDuplicate(head):

    current = head
    if head:
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
    return current


