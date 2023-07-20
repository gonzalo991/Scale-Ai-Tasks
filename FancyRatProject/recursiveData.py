class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def traverse_tree(self):
        print(self.value)
        for child in self.children:
            child.traverse_tree()

# Create a recursive structure representing a hierarchical tree
root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")

root.add_child(node_b)
root.add_child(node_c)
node_c.add_child(node_d)
node_c.add_child(node_e)

# Traverse the tree structure recursively
root.traverse_tree()
