﻿namespace Solution;
public class MaxSubArray
{
    
    public int MaxSubArray(int[] nums) 
    {
        int champion = int.MinValue; 
        int currentSum = int.MinValue; 
        for(int i = 0; i < nums.Length; i++)
        {
            // adding to a value that is negative cannot help, and it is better to just leave it at 0
            if(currentSum < 0)
                currentSum = nums[i]; 
            else 
                currentSum = nums[i] + currentSum; 
            if(champion < currentSum)
                champion = currentSum; 
        }
        return champion; 
    }

}