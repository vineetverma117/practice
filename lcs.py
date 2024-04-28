
class LCS:
    def lcs_recursion(self, X, Y, m, n):
        if m == 0 or n==0:
            return 0
        elif X[m-1] == Y[n-1]:
            return 1 + self.lcs_recursion(X, Y, m-1, n-1)
        else:
            return max(self.lcs_recursion(X, Y, m, n-1),
                       self.lcs_recursion(X, Y, m-1, n))
                       
    def lcs_dp(self, X, Y, m, n, dp):
        if m==0 or n==0:
            return 0
            
        if dp[m][n] != -1:
            return dp[m][n]
            
        if X[m-1] == Y[n-1]:
            dp[m][n] = 1 + self.lcs_dp(X, Y, m-1, n-1, dp)
            return dp[m][n]
        else:
            dp[m][n] = max(self.lcs_dp(X, Y, m, n-1, dp),
                           self.lcs_dp(X, Y, m-1, n, dp))
            return dp[m][n]
            
    def lcs_dp_bottom_up(self, X, Y, m, n):
        L = [[None]*(n+1) for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i-1]  == Y[j-1]:
                    L[i][j] = 1 + L[i-1][j-1]
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[m][n]         
    
if __name__ == '__main__': 
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    m = len(S1)
    n = len(S2)
    
    obj = LCS()
    print(obj.lcs_recursion(S1, S2, m, n))
    dp = [[-1 for column in range(n+1)]
          for row in range(m+1)]
    print(obj.lcs_dp(S1, S2, m, n, dp))         
    print(obj.lcs_dp_bottom_up(S1, S2, m, n))
