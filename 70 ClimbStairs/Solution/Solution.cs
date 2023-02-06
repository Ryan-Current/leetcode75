namespace Solution;
public class Solution
{
    // Thoughts: 
    // First I brute forced the answers of the first few by listing the permutations: 
    //
    // in | out
    // 1 | 1
    // 2 | 2
    // 3 | 3
    // 4 | 5
    // 5 | 8
    // 6 | 13
    // 
    // I realized at this point that this sequence looked familiar - it was the fibonnaci sequence
    // and the recursive definition of it is: 
    // fibonacci(0) = 1 
    // fibonacci(1) = 1
    // fibonacci(n + 1) = fibonacci(n) + fibonacci(n - 1)
    //
    // we can translate this directly into code with the function written below


    public int ClimbStairsNaive(int n)
    {
        // needed for recursive case of 2
        if(n == 0)
            return 1; 
        // base case 
        if(n == 1)
            return 1;
         
        return ClimbStairsNaive(n - 1) + ClimbStairsNaive(n - 2); 
    }


    // However, this can be improved because there are values of n that 
    // get passed to ClimbStairsNaive() multiple times, so we can take a
    // dynamic programming approach to significantly improve performance 


    public int ClimbStairs(int n)
    {
        // we know that n >= 1, so we can populate the first 
        // 2 elements of the dynamic programming array
        int[] dyn = new int[n + 1]; 
        dyn[0] = 1; 
        dyn[1] = 1; 
        for(int i = 2; i <= n; i++)
        {
            dyn[i] = dyn[i - 1] + dyn[i - 2]; 
        }
        return dyn[n]; 
    }

}
