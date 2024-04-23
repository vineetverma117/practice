import numpy as num
class MatrixMul:
    
    def matrix_size(self, A, B):
        row1 = len(A)
        col1 = len(A[0])
        row2 = len(B)
        col2 = len(B[0])
        return row1, col1, row2, col2
        
    def get_result_matrix(self, A, B):
        row1, col1, row2, col2 = self.matrix_size(A, B)
        
        result = []
        for result_row in range(row1):
            result.append([0]*col2)
        return result
        
    def multiply_by_numpy(self, A, B):
        #using python numpy library
        return num.dot(A, B)
        
    def multiply_custom(self, A, B):
        row1, col1, row2, col2 = self.matrix_size(A, B)
        result = self.get_result_matrix(A, B)
        for i in range(row1):
            for j in range(col2):
                for k in range(col1):
                    result[i][j] = result[i][j] + A[i][k]*B[k][j]
        return result                
    
    def get_identity_matrix(self, A):
        row1 = len(A)
        col1 = len(A[0])
        
        result = self.get_result_matrix(A, A)
        for i in range(row1):
            for j in range(col1):
                result[i][j] = 1 if(i==j) else 0
        return result
        
    def matrix_power(self, A, power):
        if power == 0:
            return self.get_identity_matrix(A)
        elif power == 1:
            return A
        elif power%2 == 0:
            B = self.matrix_power(A, power/2)
            return self.multiply_custom(B, B)
        elif power%2 == 1:
            # operator // will return floor value
            B = self.matrix_power(A, power//2)
            return self.multiply_custom(A, self.multiply_custom(B, B))
            
if __name__ == '__main__':
    #matrix A
    A = [[1, 2, 3],
         [1, 2, 3],
         [1, 2, 3]]
     
    B = [[1, 2, 3, 4],
         [1, 2, 3, 4],
         [1, 2, 3, 4]]
    
    obj = MatrixMul() 
    result = obj.get_result_matrix(A, B)
    
    print(obj.multiply_by_numpy(A, B))
    print(obj.multiply_custom(A, B))
    print(obj.matrix_power(A, 3))
