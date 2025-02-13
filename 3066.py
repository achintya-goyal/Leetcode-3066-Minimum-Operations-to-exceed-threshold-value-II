class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        s = nums
        heapq.heapify(s)
        while len(s)>1:
            x = heapq.heappop(s)
            y = heapq.heappop(s)
            if x>=k:
                return cnt
            heapq.heappush(s, (x*2)+y)
            cnt+=1
        return cnt
