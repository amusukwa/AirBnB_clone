#!/usr/bin/python3
"""
The Amenity  module
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize amenity attributes"""
        super().__init__(*args, **kwargs)
        self.name = ""
