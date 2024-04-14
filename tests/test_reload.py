import unittest
from models.engine.file_storage import FileStorage

class TestFileStorageReload(unittest.TestCase):

    def test_reload(self):
        """Test reload method of FileStorage"""
        storage = FileStorage()
        # Populate storage with some objects
        obj1 = MyModel()
        obj2 = MyOtherModel()
        storage.new(obj1)
        storage.new(obj2)

        # Reload from file
        storage.reload()

        # Check reloaded objects
        all_objects = storage.all()
        self.assertIn(obj1, all_objects.values())
        self.assertIn(obj2, all_objects.values())

if __name__ == '__main__':
    unittest.main()