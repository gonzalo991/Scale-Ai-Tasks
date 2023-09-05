class TreeNode:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None

class FlyweightFactory:
    def __init__(self):
        self.cache = {}

    def create_node(self, id, tree_type):
        if tree_type == "binary":
            if id not in self.cache:
                self.cache[id] = TreeNode(id)
            return self.cache[id]
        elif tree_type == "ternary":
            if id not in self.cache:
                self.cache[id] = TreeNode(id)
            middle = self.create_node("D", "binary")
            self.cache[id].left = middle
            self.cache[id].right = middle
            return self.cache[id]
        else:
            raise ValueError("Invalid tree type")

class Client:
    def __init__(self):
        self.factory = FlyweightFactory()

    def create_tree(self, type, optional=False):
        if type == "binary":
            root = self.factory.create_node("A", type)
            root.left = self.factory.create_node("B", type)
            root.right = self.factory.create_node("C", type)
            return root
        elif type == "ternary" and optional:
            root = self.factory.create_node("A", type)
            root.left = self.factory.create_node("B", type)
            root.right = self.factory.create_node("C", type)
            middle = self.factory.create_node("D", "binary")
            root.left.left = middle
            root.right.right = middle
            return root
        elif type == "ternary":
            raise ValueError("Ternary trees are not optional")
        else:
            raise ValueError("Invalid tree type")

# Example usage
tree = Client().create_tree("ternary", optional=True)
print(tree.left.left.id)  # Output: D