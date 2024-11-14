class TreeNException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NodeN:
    def __init__(self, data):
        self.data = data  # Person object
        self.children = []

    def find_parent_by_id(self, id):
        if self.data.identification == id:
            return self
        for child in self.children:
            try:
                found = child.find_parent_by_id(id)
                return found
            except TreeNException:
                continue
        raise TreeNException(f"the parent with  {id} doesn't exist")

    def validate_person_exist(self, id):
        if self.data.identification == id:
            raise TreeNException("La persona ya existe")
        for child in self.children:
            child.validate_person_exist(id)


class Person:
    def __init__(self, identification, name):
        self.identification = identification
        self.name = name
