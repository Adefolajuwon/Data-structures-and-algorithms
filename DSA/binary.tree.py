class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


node0 = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(5)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(4)
node7 = TreeNode(6)
node8 = TreeNode(8)

node0.left = node1
node1.left = node2
node0.right = node3
node3.left = node4
node3.right = node5
print(node3.key)


# node0 = TreeNode(3)
# node1 = TreeNode(4)
# node2 = TreeNode(5)
# # print(node0.key)
# node0.left = node1
# node0.right = node2
# tree = node0
