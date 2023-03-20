namespace Solution;

// commented out is a solution that uses a List instead of a Dictionary

// public class Trie
// {
//     public TrieNode Root; 

//     public Trie() 
//     {
//         Root = new TrieNode(' '); 
//     }
    

//     public void Insert(string word) 
//     {
//         insert(word, Root); 
//     }


//     private void insert(string word, TrieNode node)
//     {
//         if(word.Length == 0)
//             return; 
//         char c = word[0]; 
//         TrieNode next = node.NextNodes.Find(node => node.C == c); 
//         if(next is null)
//         {
//             next = new TrieNode(c); 
//             node.NextNodes.Add(next); 
//         } 
//         if(word.Length == 1)
//             next.IsEnd = true; 
        
//         insert(word.Substring(1), next);  
//     }

    
//     public bool Search(string word) 
//     {
//         return search(word, Root); 
//     }


//     private bool search(string word, TrieNode node)
//     {
//         if(word.Length == 0)
//             return node.IsEnd; 
//         char c = word[0]; 
//         TrieNode next = node.NextNodes.Find(node => node.C == c); 
//         if(next is null)
//             return false; 
//         return search(word.Substring(1), next);         
//     }

    
//     public bool StartsWith(string prefix) 
//     {
//         return startsWith(prefix, Root); 
//     }


//     private bool startsWith(string word, TrieNode node)
//     {
//         if(word.Length == 0)
//             return true; 
//         char c = word[0]; 
//         TrieNode next = node.NextNodes.Find(node => node.C == c); 
//         if(next is null)
//             return false; 
//         return startsWith(word.Substring(1), next); 
//     }

// }


// public class TrieNode
// {
//     public char C; 
//     public List<TrieNode> NextNodes; 
//     public bool IsEnd; 


//     public TrieNode(char C) 
//     {
//         this.C = C; 
//         NextNodes = new List<TrieNode>(); 
//         IsEnd = false; 
//     }
// }


// Implementation with a dictionary instead of a list for faster access times

public class Trie
{
    public TrieNode Root; 

    public Trie() 
    {
        Root = new TrieNode(' '); 
    }
    

    public void Insert(string word) 
    {
        insert(word, Root); 
    }


    private void insert(string word, TrieNode node)
    {
        if(word.Length == 0)
            return; 
        char c = word[0]; 
        TrieNode next; 
        if(node.NextNodes.ContainsKey(c))
        {
            next = node.NextNodes[c]; 
        }
        else
        {
            next = new TrieNode(c); 
            node.NextNodes.Add(c, next); 
        }
        if(word.Length == 1)
            next.IsEnd = true; 
        
        insert(word.Substring(1), next);  
    }

    
    public bool Search(string word) 
    {
        return search(word, Root); 
    }


    private bool search(string word, TrieNode node)
    {
        if(word.Length == 0)
            return node.IsEnd; 
        char c = word[0]; 
        if(!node.NextNodes.ContainsKey(c))
            return false; 
        TrieNode next = node.NextNodes[c]; 
        if(next is null)
            return false; 
        return search(word.Substring(1), next);         
    }

    
    public bool StartsWith(string prefix) 
    {
        return startsWith(prefix, Root); 
    }


    private bool startsWith(string word, TrieNode node)
    {
        if(word.Length == 0)
            return true; 
        char c = word[0]; 
        if(!node.NextNodes.ContainsKey(c))
            return false; 
        TrieNode next = node.NextNodes[c]; 
        return startsWith(word.Substring(1), next); 
    }

}


public class TrieNode
{
    public char C; 
    public Dictionary<char, TrieNode> NextNodes; 
    public bool IsEnd; 


    public TrieNode(char C) 
    {
        this.C = C; 
        NextNodes = new (); 
        IsEnd = false; 
    }
}