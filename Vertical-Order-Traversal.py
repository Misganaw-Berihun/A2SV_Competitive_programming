# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        array = []
        minn = inf
        maxx = 0
        
        def dfs(node, row, col):
            if not node:
                return
            
            nonlocal minn 
            minn = min(minn, col)
            nonlocal maxx 
            maxx = max(maxx, col)
            array.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
            
        dfs(root, 0, 0)
        array.sort()
        maxx -= minn
        maxx += 1
        answer = [[] for i in range(maxx)]
        for col, row, val in array:
            answer[col - minn].append(val)
        
        return answer
