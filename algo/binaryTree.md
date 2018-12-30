
## Traverse a Tree
* Pre-order Traversal
	Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.
	遇到了就记录
	
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traversal(self,x):
        
        if not x:
            return None
        self.res.append(x.val)
        if x.left:
            self.traversal(x.left)
        if x.right:
            self.traversal(x.right)
            
    def preorderTraversal_recursive(self, root):
        self.res = []
        self.traversal(root)
        return self.res
        
    def preorderTraversal_stack(self, root):
        res = []
        stack = [root]
        while stack:
            
            x = stack.pop()
            if x:
                res.append(x.val)
                if x.right:
                    stack.append(x.right)
                if x.left:
                    stack.append(x.left)
        return res
    
    def preorderTraversal_cache(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cache = []
        while root is not None:
            res.append(root.val)
            if root.left is not None:
                if root.right:
                    cache.append(root)
                root = root.left
            else:
                while root.right is None:
                    try:
                        root = cache.pop()
                    except:
                        return res
                root = root.right
        return res
```
* In-order Traversal
	In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.
	没了左儿子再记
* Post-order Traversal
	Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.
	没了儿子再记

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1OTAzNTY4NDFdfQ==
-->