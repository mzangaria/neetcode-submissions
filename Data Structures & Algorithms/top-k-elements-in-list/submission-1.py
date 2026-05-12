class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} 

        for num in nums: 
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for num, val in counter.items():
            freq[val].append(num)
        
        output = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output
            
        
