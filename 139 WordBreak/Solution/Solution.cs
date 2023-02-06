namespace Solution;
public class Solution
{
    public bool WordBreak(string s, IList<string> wordDict)
    {
        for(int i = 0; i < wordDict.Count; i++)
        {
            if(s.Length < wordDict[i].Length)
                continue; 
            if(s.Equals(wordDict[i]))
                return true; 
            if(s.Substring(0, wordDict[i].Length).Equals(wordDict[i]))
            { 
                return WordBreak(s.Substring(wordDict[i].Length), wordDict); 
            }
        }
        return false; 
    }

}
