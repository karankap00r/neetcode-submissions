import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1

        sorted_nums_by_freq_inverse = sorted(num_map, key=lambda x: num_map[x], reverse=True)
        # heap = []
        # for num, freq in num_map.items():
        #     heapq.heappush(heap, (-freq, num))

        # result = []
        # for idx in range(k):
        #     result.append(sorted_nums_by_freq_inverse[idx])

        return sorted_nums_by_freq_inverse[:k]