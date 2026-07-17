class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        #HashSet 
        num_set = set(nums)
        for i in range(len(nums)+1):
            if i not in num_set:
                return i
        '''
        #BigBrains
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return  res