class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        b= []
        def divide_and_conqure(left, right): 
            if left > right:
                return None
            mid = (left + right) // 2
           
            left = divide_and_conqure(left, mid-1)
            right = divide_and_conqure(mid+1, right)
            return TreeNode(nums[mid], left, right)
        return divide_and_conqure( 0, len(nums)-1)

