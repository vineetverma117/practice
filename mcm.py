import sys
class MCM:
    
    def mcm_recurtive(self, p, i, j):
        if i == j:
            return 0

        min_val = sys.maxsize
        for k in range(i, j):
            count = self.mcm_recurtive(p, i, k) + \
                    self.mcm_recurtive(p, k+1, j) + \
                    p[i-1]*p[j]*p[k]
            if count < min_val:
                min_val = count
        return min_val
        
    def mcm_memoization(self, p, i, j, dp):
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
            
        dp[i][j] = sys.maxsize
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], \
                       self.mcm_memoization(p, i, k, dp) +\
                       self.mcm_memoization(p, k+1, j, dp)+\
                       p[i-1]*p[j]*p[k])
        return dp[i][j]
        
# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3]
    N = len(arr)
     
    obj = MCM()
    
    print("Minimum number of multiplications:")
    print(obj.mcm_recurtive(arr, 1, N-1))
    
    dp = [[-1 for i in range(100)]
          for row in range(100)]
    print(obj.mcm_memoization(arr,1, N-1, dp))
