class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
		    y = -x
        else:
		    y = x
        
        
        n = 0
        while y > 0:
            n *= 10
            n += y % 10
            y /= 10
            
        if n > 2 ** 31 -1:
            n = 0
            
        if x < 0:
	        return -n
        return n