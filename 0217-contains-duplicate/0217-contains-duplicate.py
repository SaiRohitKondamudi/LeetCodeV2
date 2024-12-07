class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = set()
        
        for i in range(len(nums)):
            if nums[i] in hmap:
                return True
            # hmap[nums[i]] = i
            hmap.add(nums[i])
        
        return False
        