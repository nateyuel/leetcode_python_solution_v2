# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1

        store = defaultdict(list)
        store[root] = [1, root.val, root]
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                poped = queue.popleft()
            
                if poped.left:
                    store[poped.left] = [1, poped.left.val, poped]
                    queue.append(poped.left)
                if poped.right:
                    store[poped.right] = [1, poped.right.val, poped]
                    queue.append(poped.right)
        
        rev_store = dict(reversed(list(store.items())))
        for node, (count, tot, parent) in rev_store.items():
            if node != parent:
                rev_store[parent][0] += count
                rev_store[parent][1] += tot 
        
        result = 0
        for node, (count, tot, _) in rev_store.items():
            if node.val == tot // count:
                result += 1

        return result 