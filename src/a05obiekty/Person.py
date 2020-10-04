class Person:
    """A simple class."""  # docstring
    species = "Homo Sapiens"  # class attribute

    def __init__(self, name="Jan", age=18):  # special method
        """This is the initializer. It's a special method (see below).
        """
        self.name = name  # instance attribute
        self.age = age

    def rename(self, renamed):  # regular method
        """Reassign and print the name attribute."""
        self.name = renamed

    def birthday(self):
        self.age += 1