from model.node import TreeNException


class TreeN:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, person, parent_id=None):

        if self.root is None:

            self.root = NodeN(person)
            self.size += 1
        else:
            parent = self.root.find_parent_by_id(parent_id)
            if parent is None:
                raise TreeNException(f"Parent with ID {parent_id} not found.")


            self.root.validate_person_exist(person.identification)


            parent.children.append(NodeN(person))
            self.size += 1

    def print_level(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.data.name, end=' ')
        elif level > 1:
            for child in node.children:
                self.print_level(child, level - 1)

    def print_by_level(self):
        h = self.height(self.root)
        for i in range(1, h + 1):
            self.print_level(self.root, i)
            print()

    def height(self, node):
        if node is None:
            return 0
        if not node.children:
            return 1
        return 1 + max(self.height(child) for child in node.children)



class Person:
    def __init__(self, identification, name):
        self.identification = identification
        self.name = name


class NodeN:
    def __init__(self, data):
        self.data = data  # Person object
        self.children = []

    def find_parent_by_id(self, id):
        if self.data.identification == id:
            return self
        for child in self.children:
            try:
                return child.find_parent_by_id(id)
            except TreeNException:
                continue
        raise TreeNException(f"Parent with ID {id} not found.")

    def validate_person_exist(self, id):
        if self.data.identification == id:
            raise TreeNException("The person already exists in the tree.")
        for child in self.children:
            child.validate_person_exist(id)

try:
    tree = TreeN()
    root_person = Person("1", "Root Person")
    tree.add(root_person)

    child_person = Person("2", "Child Person")
    tree.add(child_person, "1")

    print(f"Tamaño del árbol: {tree.size}")
except TreeNException as e:
    print(f"Error: {e}")
if __name__ == '__main__':
    tree = TreeN()
    tree.add(Person(1, "Root"))
    tree.add(Person(2, "Child 1"), parent_id=1)
    tree.add(Person(3, "Child 2"), parent_id=1)
    tree.add(Person(4, "Grandchild 1"), parent_id=2)
    tree.add(Person(5, "Grandchild 2"), parent_id=2)

    print("Nodes by level: ")
    tree.print_by_level()

