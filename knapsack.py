class Knapsack_0_1:
    table = None
    
    def fill_null_table(self, W, N):
        self.table = []
        for each in range(N+1):
            self.table.append([-1]*(W+1))
    
    def knapsack_dynamic(self, weight, profit, W, N):
        if W == 0 or N==0:
            return 0
            
        if self.table[N][W] != -1:
            return self.table[N][W]
            
        if W < weight[N-1]:
            self.table[N][W] = self.knapsack_dynamic(weight, profit, W, N-1)
            return self.table[N][W]
        else:
            self.table[N][W] = max(profit[N-1] + \
                self.knapsack_dynamic(weight, profit, W-weight[N-1], N-1),
                self.knapsack_dynamic(weight, profit, W, N-1)
            )
            return self.table[N][W]


    def knapsack_recursion(self, weight, profit, W, N):
        
        if W == 0 or N==0:
            return 0
            
        elif W < weight[N-1]:
            return self.knapsack_recursion(weight, profit, W, N-1)
            
        else:
            return max(profit[N-1] + \
               self.knapsack_recursion(weight, profit, W-weight[N-1], N-1),
               self.knapsack_recursion(weight, profit, W, N-1)
            )
        
    
# Driver code
if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    obj = Knapsack_0_1()
    obj.fill_null_table(W, n)
    print(obj.knapsack_recursion(weight, profit, W, n))
    print(obj.knapsack_dynamic(weight, profit, W, n))
