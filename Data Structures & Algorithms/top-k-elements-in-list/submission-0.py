import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1

        heap = []
        for num, freq in num_map.items():
            heapq.heappush(heap, (-freq, num))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result