
# Structure of a Binary Tree Node
class Node:
	def __init__(self, v):
		self.data = v
		self.left = None
		self.right = None

# Function to print inorder traversal
def print_inorder(node):
	if node is None:
		return

	print_inorder(node.left)
	print(str(node.data)+ ' ')
	print_inorder(node.right)
	
def print_preorder(node):
    if node is None:
	    return
	print(str(node.data)+ ' ')
	print_preorder(node.left)
	print_preorder(node.right)

def print_postorder(node):
	if node is None:
		return
	print_postorder(node.left)
	print_postorder(node.right)
	print(str(node.data)+ ' ')
	
	

# Driver code
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(6)

	print("preorder traversal of binary tree is:")
	print_preorder(root)
	print("inorder")
	print_inorder(root)
	print("postorder")
	print_postorder(root)
