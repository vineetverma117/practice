

class Fibonacci:
    
    def fib(self, n):
        a = 0
        b = 1
        if n < 0:
            print("incorrect")
        elif n <=1:
            return n
        else:
            for i in range(2, n+1):
                c = a + b
                a = b
                b = c
        return b
        
    def fib_recursive(self, n):
        if n <=1:
            return n
        return self.fib_recursive(n-1) + self.fib_recursive(n-2)
        
    def fib_dynamic(self, n):
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]
                
obj = Fibonacci()
print(obj.fib(9))
print(obj.fib_recursive(9))
print(obj.fib_dynamic(9))
### 0 1 1 2 3 5 8 13 21 34
