class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        k = len(nums) - 1
        done = set()
        nums.sort()
        while k >= 2:
            left = 0
            right = k - 1
            target = -1*nums[k]
            while left < right:
                if nums[left]+nums[right] == target:
                    sorted_tuple = tuple(sorted([nums[left], nums[right], nums[k]]))
                    if sorted_tuple not in done:
                        result.append([nums[left], nums[right], nums[k]])
                        done.add(sorted_tuple)
                    left += 1
                    right -= 1
                elif nums[left]+nums[right]<target:
                    left += 1
                else:
                    right -= 1
            k -= 1
        return result