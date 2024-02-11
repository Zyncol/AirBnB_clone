#!/usr/bin/python3
"""
Base model for all classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        initialises classes with an ID
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        updates in accordance with time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        for dictitionary representation if this functio
        """
        inst_pre = self.__dict__.copy()
        inst_pre["__class__"] = self.__class__.__name__
        inst_pre["updated_at"] = self.updated_at.isoformat()
        inst_pre["created_at"] = self.created_at.isoformat()

        return inst_pre

    def __str__(self):
        """
        for string presentation
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

