

class TreeNode:
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_bin_tree_bfs(root: TreeNode) -> list:
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        root = stack.pop(0)
        if root:
            result.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
        
    return result


def is_list_equal(a_list, b_list):
    a_len = len(a_list)
    b_len = len(b_list)
    if a_len != b_len:
        return False
    for i in range(a_len):
        if a_list[i] != b_list[i]:
            return False
    return True

if __name__ == "__main__":
    """
       a1
     b2   c3
    d4 e5 f6 g7
    """
    a = TreeNode(1, 
                 TreeNode(2, TreeNode(4), TreeNode(5)),
                 TreeNode(3, TreeNode(6), TreeNode(7))
                 )
    assert is_list_equal(get_bin_tree_bfs(a), [1, 2, 3, 4, 5, 6, 7]) == True