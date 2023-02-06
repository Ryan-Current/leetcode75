namespace Solution;
public class Solution
{
    public bool WordBreak(string s, IList<string> wordDict)
    {
        // check every word in the dictionary against the beginning of the string
        for(int i = 0; i < wordDict.Count; i++)
        {
            // skip the word if the string is too short to compare it 
            if(s.Length < wordDict[i].Length)
                continue; 
            // if this word matches the full string, then it can be broken
            if(s.Equals(wordDict[i]))
                return true; 
            // if this word matches the beginning of the string, then remove the beginning and 
            // continue processing the string
            if(s.Substring(0, wordDict[i].Length).Equals(wordDict[i]))
            { 
                return WordBreak(s.Substring(wordDict[i].Length), wordDict); 
            }
        }
        // if the string is not fully matched, then it cannot be split
        return false; 
    }

}
