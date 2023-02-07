namespace Solution;
public class WordDictionary
{
    public Node Root { get; set; } 


    public WordDictionary() 
    { 
        Root = new Node(); 
    }


    public void AddWord(string word) 
    {
        Node currentNode = Root; 
        for(int i = 0; i < word.Length; i++)
        {
            if(!currentNode.NextLetters.ContainsKey(word[i]))
            {
                currentNode.NextLetters.Add(word[i], new Node()); 
            }
            currentNode = currentNode.NextLetters[word[i]]; 
        }
        currentNode.IsEnd = true; 
    }
    

    public bool Search(string word) 
    {
        return searchHelp(word, 0, Root); 
    }


    private bool searchHelp(string word, int index, Node node)
    {
        Node current = node; 
        for(int i = index; i < word.Length; i++)
        {
            if(word[i] == '.')
            {
                foreach(Node nextNode in current.NextLetters.Values)
                {
                    if(searchHelp(word, i + 1, nextNode))
                        return true; 
                }
                return false; 
            }
            else
            {
                if(!current.NextLetters.ContainsKey(word[i]))
                    return false; 
                current = current.NextLetters[word[i]]; 
            }
        }
        return current.IsEnd; 
    }

}


public class Node
{
    public bool IsEnd { get; set; } = false; 
    public Dictionary<char, Node> NextLetters { get; set; } = new(); 
}



