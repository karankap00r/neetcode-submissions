class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        product = 1
        zeros_count = 0
        for num in nums:
            if num == 0:
                zeros_count += 1
            else:
                product *= num

        if zeros_count > 1:
            return [0] * len(nums)

        result = []
        for num in nums:
            if num == 0:
                result.append(product)
            elif zeros_count:
                result.append(0)
            else:
                result.append(product // num)

        return result