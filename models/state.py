#!/usr/bin/python3
"""
The State module
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize state attributes"""
        super().__init__(*args, **kwargs)
        self.name = ""
