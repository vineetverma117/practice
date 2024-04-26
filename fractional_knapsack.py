class Knapsack:
    
    def __init__(self, profit, weight):
        self.weight = weight
        self.profit = profit

    @staticmethod
    def fractionalKnapsack(array, W):
        array = sorted(array, key = lambda x: x.profit/x.weight, reverse=True)
        remaining = W
        profit = 0
        for each_rec in array:
            if(remaining > each_rec.weight):
                profit = profit + each_rec.profit
                remaining = remaining - each_rec.weight
            else:
                if(remaining > 0):
                    profit = profit + (each_rec.profit/each_rec.weight)*remaining
                    remaining = 0
        return profit
    
if __name__ == '__main__':
    W = 50
    array = [Knapsack(60, 10), Knapsack(100, 20), Knapsack(120, 30)]
    print(Knapsack.fractionalKnapsack(array, W))
