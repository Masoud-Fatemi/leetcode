class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = {}
        limit = len(nums)/2

        for num in nums:
            if num in temp:
                temp[num]+=1
            else:
                temp[num] = 1
        
        for k, v in temp.items():
            if v > limit:
                return k