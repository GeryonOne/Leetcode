"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b 
where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, float('inf'), float('-inf'))

    def traverse(self, node, min_val, max_val):
        if not node:
            return max_val - min_val

        min_val = min(min_val, node.val)
        max_val = max(max_val, node.val)

        left_diff = self.traverse(node.left, min_val, max_val)
        right_diff = self.traverse(node.right, min_val, max_val)

        return max(left_diff, right_diff)


# Example usage:
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

solution = Solution()
result = solution.maxAncestorDiff(root)
print(result)
