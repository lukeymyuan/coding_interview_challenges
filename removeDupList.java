import java.util.HashSet;

public class removeDuplicates
{
    static class node
    {
        int val;
        node next;

        public node(int val)
        {
            this.val = val;
        }
    }

    /* Function to remove duplicates from a
       unsorted linked list */
    static void removeDuplicate(node head)
    {
        // Hash to store seen values
        HashSet<Integer> seen = new HashSet<>();
        node curr = head;
        node prev = null;
        while(curr!=null){
            if(!seen.contains(curr.val)){
                seen.add(curr.val);
                prev = curr;
            }
            else{
                prev.next = curr.next;
            }
            curr = curr.next;
        }

    }

    /* Function to print nodes in a given linked list */
    static void printList(node head)
    {
        while (head != null)
        {
            System.out.print(head.val + " ");
            head = head.next;
        }
    }

    public static void main(String[] args)
    {
        /* The constructed linked list is:
         10->12->11->11->12->11->10*/
        node start = new node(10);
        start.next = new node(12);
        start.next.next = new node(11);
        start.next.next.next = new node(11);
        start.next.next.next.next = new node(12);
        start.next.next.next.next.next = new node(11);
        start.next.next.next.next.next.next = new node(10);

        System.out.println("Linked list before removing duplicates :");
        printList(start);

        removeDuplicate(start);

        System.out.println("\nLinked list after removing duplicates :");
        printList(start);
    }
}
