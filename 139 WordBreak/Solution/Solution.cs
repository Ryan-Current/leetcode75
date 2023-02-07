namespace Solution;
public class Solution
{
    public bool WordBreak(string s, IList<string> wordDict)
    {
        bool[] dyn = new bool[s.Length + 1]; 
        // if we reach the last index, then we know it is true
        dyn[s.Length] = true; 
        for(int i = s.Length - 1; i >= 0; i--)
        {
            foreach(string word in wordDict)
            {
                // are there enough characters in s to compare, and are those characters equal
                if(i + word.Length <= s.Length && s.Substring(i, word.Length).Equals(word))
                {
                    // we can match this word. Set this index to the ability to match up to this index
                    dyn[i] = dyn[i + word.Length]; 
                }
                // if 1 word is found to work then we can stop
                if(dyn[i])
                    break; 
            }
        }
        return dyn[0]; 
    }

}
