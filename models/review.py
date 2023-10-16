#!/usr/bin/python3
"""
The Review  module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize review attributes"""

        place_id = ""
        user_id = ""
        text = ""
