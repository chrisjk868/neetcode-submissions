class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Consider each nums[i] being in the first, second, ... n-th position
        # [1 2 3]
        # [1 | 2 3]
        # - [2 | 3], [3 | 2]
        #   - [3], [2]
        # [2 | 1 3]
        # - [1 | 3], [3 | 1]
        #   - [3], [1]
        # [3 | 2 1]
        #   ...
        ans = []
        n = len(nums)
        def dfs(i):
            if i >= n:
                ans.append(nums[:])
            for j in range(i, n): # Switches the j-th number with i-th number
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
            return
        dfs(0)
        return ans
        