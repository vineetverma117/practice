#Best case/Avg case = O(nlogn) Worstcase: O(n2)
#extra space: O(logn) (stack space)
class QuickSort:
    
    def partition(self, A, low, high):
        #if you select pivot last item
        pivot = A[high]
        i = low-1
        
        for j in range(low, high):
            if A[j] < pivot:
                i = i + 1
                A[i], A[j] = A[j], A[i]
            
        A[i+1], A[high] = A[high], A[i+1]
        return i+1
        
    def partition_low(self, A, low, high):
        #if you select pivot first item
        pivot = A[low]
        i = low
        for j in range(low+1, high+1):
            if A[j] < pivot:
                i = i + 1
                A[i], A[j] = A[j], A[i]
            
        A[i], A[low] = A[low], A[i]
        return i    
        
    def quick_sort(self, A, low, high):
        if(low < high):
            pi = self.partition(A, low, high)
            self.quick_sort(A, low, pi-1)
            self.quick_sort(A, pi+1, high)
        return A
        
if __name__ == '__main__':
    A = [2, 10, 30, 40, 4, 6, 5]
    obj = QuickSort()
    result = obj.quick_sort(A, 0, len(A)-1)
    print(result)
