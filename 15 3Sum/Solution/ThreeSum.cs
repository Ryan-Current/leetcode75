namespace Solution;
public class ThreeSum
{
    
    public IList<IList<int>> ThreeSum(int[] nums) 
    {
        // sorting the array allows us to have a left and right and avoid duplicates 
        Array.Sort(nums); 
        List<IList<int>> answers = new(); 
        for(int i = 0; i < nums.Length; i++)
        {
            if(i > 0 && nums[i] == nums[i-1])
                continue;
            int left = i+1; 
            int right = nums.Length - 1; 
            while(left < right)
            {
                int sum = nums[i] + nums[left] + nums[right];
                if(sum < 0)
                    left++; 
                else if(sum > 0)
                    right--; 
                else 
                {
                    answers.Add(new List<int> { nums[i], nums[left], nums[right] }); 
                    left++; 
                    right--; 
                    // while we aren't hitting the end of the array and we are checking the 
                    // same number, move on
                    while(left != nums.Length - 1 && nums[left] == nums[left - 1])
                        left++; 
                    while(right != 0 && nums[right] == nums[right + 1])
                        right--; 
                }
            }
        }
        return answers; 
    }

}