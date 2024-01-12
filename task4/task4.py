import time

##################################################

# TASK 4

##################################################
# Sample table data
table = [
    {"category_id": 1, "name": "ELECTRONICS", "parent": None},
    {"category_id": 2, "name": "TELEVISIONS", "parent": 1},
    {"category_id": 3, "name": "TUBE", "parent": 2},
    {"category_id": 4, "name": "LCD", "parent": 2},
    {"category_id": 5, "name": "PLASMA", "parent": 2},
    {"category_id": 6, "name": "PORTABLE ELECTRONICS", "parent": 1},
    {"category_id": 7, "name": "MP3 PLAYERS", "parent": 6},
    {"category_id": 8, "name": "FLASH", "parent": 7},
    {"category_id": 9, "name": "CD PLAYERS", "parent": 6},
    {"category_id": 10, "name": "2 WAY RADIOS", "parent": 6},
    {"category_id": 11, "name": "SMARTPHONES", "parent": 1},
    {"category_id": 12, "name": "ANDROID", "parent": 11},
    {"category_id": 13, "name": "iOS", "parent": 11},
    {"category_id": 14, "name": "TABLETS", "parent": 1},
    {"category_id": 15, "name": "IPADS", "parent": 14},
    {"category_id": 16, "name": "ANDROID TABLETS", "parent": 14},
    {"category_id": 17, "name": "HEADPHONES", "parent": 1},
    {"category_id": 18, "name": "OVER-EAR", "parent": 17},
    {"category_id": 19, "name": "IN-EAR", "parent": 17},
    {"category_id": 20, "name": "ACCESSORIES", "parent": 1},
    {"category_id": 21, "name": "PHONE CASES", "parent": 20},
    {"category_id": 22, "name": "CHARGERS", "parent": 20},
    {"category_id": 23, "name": "LAPTOPS", "parent": 1},
    {"category_id": 24, "name": "WINDOWS", "parent": 23},
    {"category_id": 25, "name": "MACBOOKS", "parent": 23},
    {"category_id": 26, "name": "KEYBOARDS", "parent": 1},
    {"category_id": 27, "name": "WIRELESS", "parent": 26},
    {"category_id": 28, "name": "WIRED", "parent": 26},
    { "category_id": 29, "name": "GAMING CONSOLES", "parent": 1 },
    { "category_id": 30, "name": "PlayStation", "parent": 29 },
    { "category_id": 31, "name": "Xbox", "parent": 29 },
    { "category_id": 32, "name": "Nintendo Switch", "parent": 29 },
    { "category_id": 33, "name": "CAMERAS", "parent": 1 },
    { "category_id": 34, "name": "DSLR", "parent": 33 },
    { "category_id": 35, "name": "Mirrorless", "parent": 33 },
    { "category_id": 36, "name": "Point-and-Shoot", "parent": 33 },
    { "category_id": 37, "name": "SMART HOME", "parent": 1 },
    { "category_id": 38, "name": "Smart Speakers", "parent": 37 },
    { "category_id": 39, "name": "Smart Lights", "parent": 37 },
    { "category_id": 40, "name": "Smart Thermostats", "parent": 37 },
    { "category_id": 41, "name": "WEARABLES", "parent": 1 },
    { "category_id": 42, "name": "Smartwatches", "parent": 41 },
    { "category_id": 43, "name": "Fitness Trackers", "parent": 41 },
    { "category_id": 44, "name": "Wireless Earbuds", "parent": 41 },
    { "category_id": 45, "name": "PRINTERS", "parent": 1 },
    { "category_id": 46, "name": "Inkjet", "parent": 45 },
    { "category_id": 47, "name": "Laser", "parent": 45 },
    { "category_id": 48, "name": "All-in-One", "parent": 45 }
]


# Define the tree class to represent the category hierarchy
class TreeNode:
    def __init__(self, category_id, name, parent=None):
        # Initialize a node with category_id, name, and an optional parent
        self.category_id = category_id
        self.name = name
        self.parent = parent
        self.children = []  # List to store child nodes

    def add_child(self, child_node):
        # Add a child node to the current node
        self.children.append(child_node)

    def __repr__(self, level=0):
        # Represent the node and its children in a readable format
        ret = "\t" * level + f"{self.name} (ID: {self.category_id})\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, category_id, name, parent_id=None):
        # Add a new node to the tree
        new_node = TreeNode(category_id, name)
        if parent_id is None:
            # If no parent_id specified, the new node becomes the root
            self.root = new_node
        else:
            # Add the new node as a child to the specified parent node
            parent_node = self.find_node(self.root, parent_id)
            if parent_node:
                parent_node.add_child(new_node)
            else:
                print(f"Parent with ID {parent_id} not found. Node {name} (ID: {category_id}) not added.")

    def is_leaf(self, node):
        # Check if a node is a leaf node (has no children)
        return len(node.children) == 0

    def find_node(self, node, category_id):
        # Find and return a node with the specified category_id
        if node.category_id == category_id:
            return node
        for child in node.children:
            found_node = self.find_node(child, category_id)
            if found_node:
                return found_node
        return None

    def __repr__(self):
        # Represent the entire tree
        return self.root.__repr__()

# Define the Nested Set Model class
class NestedSetNode:
    def __init__(self, category_id, name, parent=None, left=None, right=None):
        # Initialize a node with category_id, name, parent, left, and right attributes
        self.category_id = category_id
        self.name = name
        self.parent = parent
        self.left = left
        self.right = right
        self.children = []  # List to store child nodes

    def __repr__(self, level=0):
        # Represent the node and its children in a readable format
        ret = "\t" * level + f"{self.name} (ID: {self.category_id}, Left: {self.left}, Right: {self.right})\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

class NestedSet:
    def __init__(self):
        self.nodes = []  # List to store NestedSetNodes
        self.current_left = 1

    def transform_tree_to_nested_set(self, tree):
        # Transform a tree to a Nested Set Model
        self.current_left = 1
        self.nodes = []  # Reset the nodes list
        self._populate_nested_set(tree.root)

    def _populate_nested_set(self, node, parent=None):
        # Recursively populate the Nested Set Model from a tree node
        if node:
            current_node = NestedSetNode(
                category_id=node.category_id,
                name=node.name,
                parent=parent,
                left=self.current_left
            )
            self.current_left += 1

            for child in node.children:
                self._populate_nested_set(child, parent=current_node)

            current_node.right = self.current_left
            self.current_left += 1

            self.nodes.append(current_node)

    def _sort_nodes_by_category_id(self):
        # Sort nodes by category_id
        return sorted(self.nodes, key=lambda node: node.category_id)

    def __repr__(self):
        # Represent the entire Nested Set Model
        sorted_nodes = self._sort_nodes_by_category_id()

        ret = "Nested Set Model :\n"
        for node in sorted_nodes:
            ret += node.__repr__()

        return ret

# Create and populate the tree
tree = Tree()
for entry in table:
    tree.add_node(entry["category_id"], entry["name"], entry["parent"])
# Display the tree
print("Category hierarchy:")
print(tree)
# Transform the tree to Nested Set Model
start_time = time.time()
nested_set = NestedSet()
nested_set.transform_tree_to_nested_set(tree)
conversion_time = time.time()
conversion_time -= start_time
# Display the Nested Set Model
print(nested_set)
print(f"Conversion Time: {conversion_time:.6f} seconds")
        
        

    



