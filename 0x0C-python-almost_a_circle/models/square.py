#!/usr/bin/python3
"""class square moudle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """__init__."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """size."""
        return ("[{}] ({}) {}/{} - {}".format(__class__.__name__,
                self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """__init__."""
        return self.width

    @size.setter
    def size(self, value):
        """__init__."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """__init__."""
        if args is not None and len(args) > 0:
            for i in range(0, len(args)):
                if (i == 0):
                    self.id = args[i]
                elif (i == 1):
                    self.size = args[i]
                elif (i == 2):
                    self.x = args[i]
                elif (i == 3):
                    self.y = args[i]
        else:
            for i in kwargs.keys():
                setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """__init__."""
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
