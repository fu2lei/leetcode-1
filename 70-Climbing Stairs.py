class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [1, 2, 3]
        for i in range(3, n):
            x = arr[i - 1] + arr[i - 2]
            arr.append(x)
        return arr[n - 1]