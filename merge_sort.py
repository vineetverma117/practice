class MergeSort:
    
    def merge(self, A, B):
        i = 0
        j = 0
        result = []
        len_A = len(A)
        len_B = len(B)
        while(i<len_A and j<len_B):
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
                
        while(i<len_A):
           result.append(A[i])
           i += 1
           
        while(j<len_B):
           result.append(B[j])
           j += 1 
        return result
    
    def merge_sort(self, A):
        length = len(A)
        if(length <=1):
            return A
        mid = length//2
        left = self.merge_sort(A[:mid])
        right = self.merge_sort(A[mid:])
        return self.merge(left, right)
        
        
if __name__ == '__main__':
    A = [10, 40, 20, 55, 11, 10, 80, 9, 5, 2]
    obj = MergeSort()
    result = obj.merge_sort(A)
    print(result)
