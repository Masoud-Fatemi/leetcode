class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos, neg = [], []
        results = []

        for item in nums: 
            if item > 0:
                pos.append(item)
            else:
                neg.append(item)
        
        for index in xrange(len(nums)/2):
            results.append(pos[index])
            results.append(neg[index])
            
        return results
