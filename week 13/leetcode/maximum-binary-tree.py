class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:


        def conqure(nums): 
            if len(nums) == 1:
                return TreeNode(nums[0])
            
            if len(nums) < 1: 
                return None
            mx = 0
            idx = 0
            for i in range(len(nums)):
                if nums[i] > mx: 
                    mx = nums[i]
                    idx = i 
            node = TreeNode(nums[idx])
            node.left = conqure(nums[:idx])
            node.right = conqure(nums[idx+1:])
            return node

        return conqure(nums)
        