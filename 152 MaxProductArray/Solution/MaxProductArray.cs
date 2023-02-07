namespace Solution;
public class WordDictionary
{
    // This was my initial approach, using recursion to calculate the max

    // public int MaxProduct(int[] nums) 
    // {
    //     return maxProductHelper(nums, 0, nums.Length - 1);  
    // }


    // private int maxProductHelper(int[] nums, int minIndex, int maxIndex)
    // {
    //     if(minIndex > maxIndex)
	// 		return Int32.MinValue; 
    //     int product = 1; 
    //     for(int i = minIndex; i <= maxIndex; i++)
    //     {
    //         product = nums[i] * product; 
    //     }
    //     int max =  Math.Max(maxProductHelper(nums, minIndex + 1, maxIndex), maxProductHelper(nums, minIndex, maxIndex - 1)); 
    //     return Math.Max(max, product);  
    // }

    // Below was my next approach, not using recursion

    // public int MaxProduct(int[] nums) 
    // {
    //     int champion = int.MinValue; 
    //     for(int length = 1; length <= nums.Length; length++)
    //     {
    //         for(int startIndex = 0; startIndex <= nums.Length - length; startIndex++)
    //         {
    //             int product = 1; 
    //             for(int i = startIndex; i < startIndex + length; i++)
    //                 product = product * nums[i]; 
    //             if(champion < product)
    //                 champion = product; 
    //         }
    //     }
    //     return champion;    
    // }


    // Both of the above solutions were too slow, so a new approach is needed
    // 
    // Given a max value, adding another number from the array will have the following effect: 
    // Positive: max value is multiplied by the positive number 
    // Negative: magnitude is increased but negative, multiplying by the minimum (negative) number will give us our new max 

    public int MaxProduct(int[] nums) 
    {
        int champion = nums.Max(); 
        int minValue = 1; 
        int maxValue = 1; 
        foreach(int num in nums)
        {
            // multiply by the next number and take the maximum number until the array is complete
            int[] possibilities = new int[3]
            {
                num, 
                num * maxValue, 
                num * minValue
            }; 
            maxValue = possibilities.Max(); 
            minValue = possibilities.Min(); 
            if(champion < maxValue)
                champion = maxValue; 
        }
        return champion;    
    }

    
}



