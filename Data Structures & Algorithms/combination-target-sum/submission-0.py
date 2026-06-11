class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = [] 
        curr = []
        n = len(nums)
        
        def build(i: int, remaining: int):
            if remaining == 0:
                ans.append(curr.copy())
                return
            
            if i == n or remaining < 0:
                return

            curr.append(nums[i])
            build(i, remaining - nums[i])
            
            curr.pop()

            build(i + 1, remaining)
        
        build(0, target)
        return ans