class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_dict, t_dict = {}, {}
        steps = 0

        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1

        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1

        print(s_dict)
        print(t_dict)

        for letter in s_dict:
            
            if letter in t_dict and s_dict[letter] > t_dict[letter] :
                steps += (s_dict[letter] - t_dict[letter]) 
            
            if letter not in t_dict:
                steps += s_dict[letter] 

        return steps
