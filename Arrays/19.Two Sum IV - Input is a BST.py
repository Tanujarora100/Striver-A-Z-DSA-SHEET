from typing import Optional


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Approach 1 using DFS and Two Pointers
        # In order Traversal to find the SORTED ARRAY of BST
        # Use Two Pointers to find if a target exist or not.
        def find(root, leaders):
            if root is None:
                return None
            find(root.left, leaders)
            leaders.append(root.val)
            find(root.right, leaders)
        leaders = []
        find(root, leaders)
        start = 0
        end = len(leaders)-1
        while start < end:
            if leaders[start]+leaders[end] == k:
                return True
            elif leaders[start]+leaders[end] < k:
                start = start+1
            else:
                end = end-1
        return False
    # Time Complexity-O(N)
    # Space Complexity-O(N)+O(N)-STACK SPACE


# Approach 2 Using DFS and Set


    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.helper(root, k, set())

    def helper(self, root, k, seen):
        if not root:
            return None
        if (k - root.val) in seen:
            return True
        seen.add(root.val)
        left = self.helper(root.left, k, seen)
        right = self.helper(root.right, k, seen)

        return left or right

    '''
    The time complexity of this function is O(n), because the DFS of the BST takes O(n) time in the worst case
    where n is the number of nodes in the BST.
    The space complexity of this function is also O(n), because the space used by 
    the function is dominated by the space used to store the seen set, which is also O(n) in the worst case.
    '''
