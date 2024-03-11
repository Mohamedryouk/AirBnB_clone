#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    TestFileStorage class
    """
    def test_new(self):
        """
        test new method
        """
        filestorage = FileStorage
        self.assertIsInstance(filestorage.__objects, dict)
    
    def test_all(self):
        filestorage = FileStorage
        result = filestorage.all()
        self.assertEqual(result, object)

if __name__ == '__main__':
    unittest.main()