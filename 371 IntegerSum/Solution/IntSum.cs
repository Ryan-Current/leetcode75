namespace Solution;
public class IntSum
{
    // binary addition
    //   0011
    // + 0001
    // = 0100
    // (places for carryover can be found by a & b)
    // (places for no carryover can be found by a ^ b)
    public int GetSum(int a, int b) 
    {
        // this value will give us where the integer is
        int carryover = (a & b) << 1; 
        int sum = a ^ b; 
        while(carryover != 0)
        {
            int temp = sum ^ carryover; 
            carryover = (sum & carryover) << 1; 
            sum = temp; 
        }
        return sum; 
    }
}