class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hmapfirst = {}
        hmaplast = {}
        count = {}
        for i in range(len(nums)):
            if nums[i] not in hmapfirst:
                hmapfirst[nums[i]] = i
            hmaplast[nums[i]] = i
            count[nums[i]] = count.get(nums[i],0) + 1
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, hmaplast[x] - hmapfirst[x] + 1)
        return ans
                