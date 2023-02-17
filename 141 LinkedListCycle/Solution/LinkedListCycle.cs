namespace Solution;
public class LinkedListCycle
{
    
    // public bool HasCycle(ListNode head) 
    // {
    //     HashSet<ListNode> visited = new HashSet<ListNode>(); 
    //     ListNode current = head; 
    //     while(current != null)
    //     {
    //         if(visited.Contains(current))
    //             return true; 
    //         visited.Add(current); 
    //         current = current.next; 
    //     }
    //     return false; 
    // }


    // another solution using less memory is to use a slow and a fast node, if there is a loop, 
    // they will eventually run into each other, and if not, there will be a null next value
    public bool HasCycle(ListNode head) 
    {
        ListNode slow = head; 
        ListNode fast = head; 
        while(slow != null && fast != null && fast.next != null)
        {
            slow = slow.next; 
            fast = fast.next.next; 
            if(slow == fast)
                return true;  
        }
        return false; 
    }

}



// Definition for singly-linked list.
public class ListNode 
{
    public int val;
    public ListNode next;


    public ListNode(int x) 
    {
        val = x;
        next = null;
    }
}
