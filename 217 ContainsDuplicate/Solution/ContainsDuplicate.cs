namespace Solution;
public class ContainsDuplicate
{
    
    public bool ContainsDuplicate(int[] nums) 
    {
        HashSet<int> set = new HashSet<int>(); 
        foreach(int num in nums)
        {
            if(set.Contains(num))
                return false; 
            set.Add(num); 
        }
        return true; 
    }

}