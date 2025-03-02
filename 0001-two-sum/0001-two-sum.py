class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hmap:
                return [i, hmap[comp]]
            hmap[nums[i]] = i
        
        return []