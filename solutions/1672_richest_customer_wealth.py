class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maximum = 0
        i = 0
        for customer in accounts:
            suma = j = 0
            for money in accounts[i]:
                suma += accounts[i][j]
                j += 1
            i += 1    
            if suma > maximum:
                maximum = suma
                
        return maximum
