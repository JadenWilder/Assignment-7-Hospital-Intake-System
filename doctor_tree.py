
class DoctorNode:
    """A doctor in the hospital's reporting structure."""

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    """A binary tree representing doctor reporting relationships."""

    def __init__(self):
        self.root = None

    def _find(self, node, name):
        """Find a doctor by name within a subtree."""
        if node is None:
            return None

        if node.name == name:
            return node

        found = self._find(node.left, name)
        if found is not None:
            return found

        return self._find(node.right, name)

    def insert(self, parent_name, doctor_name, side):
        """Insert a doctor under an existing parent on the left or right."""
        if side not in ("left", "right"):
            raise ValueError("Side must be 'left' or 'right'.")

        if self.root is None:
            raise ValueError("Create the root doctor before inserting.")

        parent = self._find(self.root, parent_name)

        if parent is None:
            raise ValueError(f"Parent doctor '{parent_name}' was not found.")

        if getattr(parent, side) is not None:
            raise ValueError(f"The {side} position is already occupied.")

        setattr(parent, side, DoctorNode(doctor_name))

    def preorder(self, node):
        """Visit root, left subtree, then right subtree."""
        if node is None:
            return []

        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        """Visit left subtree, root, then right subtree."""
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        """Visit left subtree, right subtree, then root."""
        if node is None:
            return []

        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
