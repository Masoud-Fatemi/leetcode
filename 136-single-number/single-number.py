class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = {}

        for num in nums:
            if num in temp:
                temp[num]+=1
            else:
                temp[num] = 1
        
        for k, v in temp.items():
            if v == 1:
                return k