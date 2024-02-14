#!/usr/bin/python3
"""
testing unittests
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestingFileStorage_instantiation(unittest.TestCase):
        """
        testing initiation
        """
    def testing_instantiaon_arg_neg(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def testing__instantiation_Posi_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def testing_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)

class TestingFileStorage(unittest.TestCase):
    """
    for testing file storage
    """

    def setup(self):
        self.test_file = "test_file.json"

    def tdown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def testing_r_dicty(self):
        self.assertEqual(dict. type(models.storage.all()))

    def testing_new(self):
        objct = BaseModel()
        models.storage.new(objct)
        self.assertIn("BaseModel.{}".format(objct.id). models.storage.all())

    def testing_new_arg_pos(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def testing_new_args_neg(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def testing_savin_and_reloading(self):
        Tk = BaseModel()
        wz = BaseModel()
        models.storage.new(Tk)
        models.storage.new(wz)
        models.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertTrue(new_storage.all().get("BaseModel.{}".formart(Tk.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".formart(wz.id)) is not None)

    def testing_saving_to_file(self):
        tenji = BaseModel()
        models.storage.new(tenji)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def testing_reloading_empty_files(self):
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()

if __name__ == "__main__":
        unittest.main()
