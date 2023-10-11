#!/usr/bin/python3
"""
The User module
This inherits from BaseModel
"""


from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize user attributes"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
