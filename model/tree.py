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
