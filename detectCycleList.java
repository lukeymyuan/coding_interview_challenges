boolean hasCycle(Node head) {
    if(head == null){
        return false;
    }
    Node slow = head, fast = head;
    while(slow!=null && fast !=null){
        slow = slow.next;
        fast = fast.next.next;
        if(fast == slow){
            return true;
        }
    }
    return false;
}
