#!/usr/bin/python3
"""moudle"""

from models.rectangle import Rectangle

"""class"""


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}".format(__class__.__name__,
                self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
