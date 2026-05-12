class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} 

        for num in nums: 
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        heap = []
        j = 0
        for num, val in counter.items():
            j += 1
            if j <= k: 
                heapq.heappush(heap, (val, num))
                continue
            
            if heap[0][0] < val:
                heapq.heappop(heap)
                heapq.heappush(heap, (val, num))
        
        return [num for val, num in heap]
            
        
