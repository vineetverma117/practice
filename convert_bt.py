
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
   
class ConvertToBt:        
    def buildUtil(self, In, post, inStrt, inEnd, pIndex):
        if (inStrt > inEnd):
            return None
        node = newNode(post[pIndex[0]])
        pIndex[0] -= 1
        if (inStrt == inEnd):
            return node
            
        iIndex = self.search(In, inStrt, inEnd, node.data)
        node.right = self.buildUtil(In, post, iIndex + 1, inEnd, pIndex)
        node.left = self.buildUtil(In, post, inStrt, iIndex - 1, pIndex)
        return node
        
    def search(self, arr, strt, end, value):
        i = 0
        for i in range(strt, end + 1):
            if (arr[i] == value):
                break
        return i
        
    def binaryTree(self, In, post, n):
        pIndex = [n - 1]
        return self.buildUtil(In, post, 0, n - 1, pIndex)    
    
    def preOrder(self, node):
        if node == None:
            return
        print(node.data, end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)
        
# Driver code
if __name__ == '__main__':
    In = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]
    n = len(In)
 
    obj = ConvertToBt()
    root = obj.binaryTree(In, post, n)
 
    print("Preorder of the constructed tree :")
    obj.preOrder(root) 
