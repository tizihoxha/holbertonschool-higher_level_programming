#!/usr/bin/python3
"""Task 0"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square created"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.size)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return (F"[Square] ({self.id}) {self.x}/{self.y} - "
                F"{self.width}")
