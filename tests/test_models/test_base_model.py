#!/usr/bin/python3
"""
for tests
"""
import os
import unittest
import uuid
from ..models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    the class for testing
    """

    def for_testing_init(self):
        """
        for testing the init
        """
        mine = BaseModel()
        self.assertIsNotNone(mine.id)
        self.assertIsNotNone(mine.created_at)
        self.assertIsNotNone(mine.updated_at)

    def for_testing_save(self):
        """
        for testing the save
        """
        mine = BaseModel()
        i_updated_at = mine.updated_at
        c_updated_at = mine.save()
        self.assertNotEqual(i_updated_at, c_updated_at)

    def for_testing_to_dict(self):
        """
        for testing to_dict
        """
        mine = BaseModel()
        model_dicto = mine.to_dict()
        self.assertIsInstance(model_dicto, dict)
        self.assertEqual(model_dicto["__class__"], 'BaseModel')
        self.assertEqual(model_dicto['id'], mine.id)
        self.assertEqual(model_dicto['created_at'], mine.created_at.isoformat())
        self.assertEqual(model_dicto["updated_at"], mine.created_at.isoformat())

    def for_testing_str(self):
        """
        for testing str
        """
        mine = BaseModel()
        self.assertTrue(str(mine).startswith('[BaseModel]'))
        self.assertIn(mine.id, str(mine))
        self.assertIn(str(mine.__dict__), str(mine))

if __name__ == "__main__":
        unittest.main()
