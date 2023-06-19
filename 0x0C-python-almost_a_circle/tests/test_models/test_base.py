#!/usr/bin/python3

"""
Unittests for Class Base
"""
import unittest
from models.base import Base

class Test_Base(unittest.TestCase):
    def test_create_instance(self):
        self.assertIsInstance(Base(), Base)

    # def test_create_instance_fail(self):
    #     """This test will fail"""
    #     self.assertNotIsInstance(Base(), Base)

if __name__ == '__main__':
    unittest.main()
