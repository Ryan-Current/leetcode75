namespace Solution;
public class Codec 
{

    // Encodes a tree to a single string.
    public string serialize(TreeNode root) 
    {
        if (root == null)
            return "[]"; 
        List<TreeNode> order = new List<TreeNode>(){root}; 
        string str = "[";
        int i = 0; 
	    int lastNum = 0; 
        while(i < order.Count)
        {
            if(order[i] is not null)
            {
                order.Add(order[i].left); 
                order.Add(order[i].right); 
				lastNum = i; 
            }
            i++; 
        }
	    
        for(i = 0; i < lastNum + 1; i++)
        {
            str = str + (order[i] is null ? "null," : order[i].val + ","); 
        }
        // remove the last comma and add the closing bracket 
        if(str.Substring(str.Length - 1, 1).Equals(","))
            str = str.Substring(0, str.Length - 1); 
        str = str + "]"; 

        return str; 
        
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(string data) 
    {
        if(data.Equals("[]"))
            return null; 
        data = data.Substring(1, data.Length - 2); 
		
        string[] stringNodes = data.Split(',');
		

        TreeNode[] treeNodes = new TreeNode[stringNodes.Length]; 
		 
        for(int i = 0; i < stringNodes.Length; i++)
        {
            if(stringNodes[i].Equals("null"))
                treeNodes[i] = null; 
            else 
                treeNodes[i] = new TreeNode(int.Parse(stringNodes[i])); 
        }
        int depth = 0; 
        while(2*depth + 2 <= treeNodes.Length)
        {
            if(treeNodes[depth] is null)
                continue; 
            treeNodes[depth].left = treeNodes[2*depth+1]; 
			if(2*depth+2 < treeNodes.Length)
            	treeNodes[depth].right = treeNodes[2*depth+2]; 
            depth++; 
        } 
        return treeNodes[0]; 
    }


}


public class TreeNode 
{
    public int val;
    public TreeNode left;
    public TreeNode right;


    public TreeNode(int x) { val = x; }
}
