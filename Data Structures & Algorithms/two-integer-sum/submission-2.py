class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        num_map = {}
        for idx in range(len(nums)):
            other = num_map.get(target-nums[idx])
            if other is not None:
                return [other, idx]

            num_map[nums[idx]] = idx
        
        return [-1, -1]