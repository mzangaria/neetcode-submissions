class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pre = {}
        max_len = 0

        for num in nums:
            if num in pre:
                continue

            left = pre.get(num - 1, 0)
            right = pre.get(num + 1, 0)

            length = left + right + 1
            pre[num] = length

            # update real boundaries
            pre[num - left] = length
            pre[num + right] = length

            max_len = max(max_len, length)

        return max_len