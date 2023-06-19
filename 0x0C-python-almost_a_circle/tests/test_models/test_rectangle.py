#!/usr/bin/python3

"""
Unittests for Class Rectangle
"""
import unittest
import math
import os
import sys
from models.rectangle import Rectangle
from io import StringIO

class Test_Rectangle(unittest.TestCase):
    def setUp(self):
        # print("\tCreate Rectangle object my_rect")
        self.my_rect = Rectangle(10, 15, 20, 25, 120)
        self.small_rect = Rectangle(2, 2, 2, 2)
        self.my_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.file_name = "Rectangle.json"
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        self.json_str = self.my_rect.to_json_string([self.my_rect.to_dictionary()])
    def tearDown(self):
        pass
        # print("Finished running tests")
    
    """
    Test cases associated with creating instance
    """
    def test_create_instance(self):
        self.assertIsInstance(Rectangle(1, 2), Rectangle)

    def test_create_instance_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
    
    def test_create_instance_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_create_instance_negatives_dims(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, -2)
    
    def test_create_instance_negatives_offs(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1, -2)

    def test_create_instance_zero_dims(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 0)

    def test_create_instance_nonints_dims(self):
        with self.assertRaises(TypeError):
            Rectangle([1, 2], [1, 3, 5])
    
    def test_create_instance_nonints_offs(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "one", "two")

    # def test_create_instance_nonints_id(self):
    #     with self.assertRaises(TypeError):
    #         Rectangle(1, 2, 3, 4, "five")

    def test_create_instance_excess_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
    
    """
    Test cases associated with setters and getters
    """
    def test_set_attr_width(self):
        self.my_rect.width = 121
        self.assertEqual(self.my_rect.width, 121)

    def test_set_attr_height(self):
        self.my_rect.height = 1738
        self.assertEqual(self.my_rect.height, 1738)

    def test_set_attr_x(self):
        self.my_rect.x = 10
        self.assertEqual(self.my_rect.x, 10)

    def test_set_attr_y(self):
        self.my_rect.y = 15
        self.assertEqual(self.my_rect.y, 15)

    def test_set_attr_id(self):
        self.my_rect.id = 99
        self.assertEqual(self.my_rect.id, 99)

    def test_set_attr_width_zero(self):
        with self.assertRaises(ValueError):
            self.my_rect.width = 0

    def test_set_attr_height_zero(self):
        with self.assertRaises(ValueError):
            self.my_rect.height = 0

    def test_set_attr_x_negative(self):
        with self.assertRaises(ValueError):
            self.my_rect.x = -10

    def test_set_attr_y_negative(self):
        with self.assertRaises(ValueError):
            self.my_rect.y = -15

    def test_set_attr_width_negative(self):
        with self.assertRaises(ValueError):
            self.my_rect.width = -5

    def test_set_attr_height_negative(self):
        with self.assertRaises(ValueError):
            self.my_rect.height = -5

    def test_set_attr_x_nonints(self):
        with self.assertRaises(TypeError):
            self.my_rect.x = "String"

    def test_set_attr_y_nonints(self):
        with self.assertRaises(TypeError):
            self.my_rect.y = [11]

    def test_set_attr_width_nonints(self):
        with self.assertRaises(TypeError):
            self.my_rect.width = {}

    def test_set_attr_height_nonints(self):
        with self.assertRaises(TypeError):
            self.my_rect.height = (1,)

    """
    Cases associated with area() method
    """
    def test_area(self):
        self.assertEqual(self.my_rect.area(), 150)
    
    def test_area_with_args(self):
        with self.assertRaises(TypeError):
            self.my_rect.area(10)
    
    """
    Cases associated with display() method
    """
    def test_display(self):
        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        self.small_rect.display()

        # Get the value of the printed output
        printed_output = captured_output.getvalue().strip()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Assert on the expected output
        expected_output = '\n  ##\n  ##\n'.strip()
        self.assertEqual(printed_output, expected_output)
    
    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            self.my_rect.display(10, 43)
    
    """
    Cases associated with __str__()
    """
    def test_str(self):
        self.assertEqual(str(self.my_rect), "[Rectangle] (120) 20/25 - 10/15")

    """
    Cases associated with update()
    """
    def test_update_no_args(self):
        self.my_rect.update()
        self.assertEqual(str(self.my_rect), "[Rectangle] (120) 20/25 - 10/15")
    
    def test_update_args(self):
        self.my_rect.update(66, 77, 88, 99, 55)
        self.assertEqual(str(self.my_rect), "[Rectangle] (66) 99/55 - 77/88")
    
    def test_update_kwargs(self):
        self.my_rect.update(x=27, y=19)
        self.assertEqual(str(self.my_rect), "[Rectangle] (120) 27/19 - 10/15")
    
    def test_update_args_and_kwargs(self):
        self.my_rect.update(65, x=27, y=19)
        self.assertEqual(str(self.my_rect), "[Rectangle] (65) 20/25 - 10/15")
    
    def test_update_kwargs_nonattrs(self):
        self.my_rect.update(z=27, q=19)
        self.assertEqual(str(self.my_rect), "[Rectangle] (120) 20/25 - 10/15")
    
    def test_update_excess_args(self):
        """To be looked into"""
        self.my_rect.update(66, 77, 88, 99, 55, 44, 22, 11, 33)
        self.assertEqual(str(self.my_rect), "[Rectangle] (66) 99/55 - 77/88")

    def test_update_args_nonints_args(self):
        with self.assertRaises(TypeError):
            self.my_rect.update("k", "j", "ls")
    
    def test_update_dims_negative_args(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(1, -1, -2)

    def test_update_dims_zero_args(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(1, 0, 0)

    def test_update_offs_negative_args(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(1, 1, 1, -2, -2)
    
    def test_update_args_nonints_kwargs(self):
        with self.assertRaises(TypeError):
            self.my_rect.update(x=27, y=19, height=[1], width=[2])
    
    def test_update_dims_negative_kwargs(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(x=27, y=19, height=-1, width=-2)

    def test_update_dims_zero_kwargs(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(x=27, y=19, height=0, width=0)

    def test_update_offs_negative_kwargs(self):
        with self.assertRaises(ValueError):
            self.my_rect.update(x=-27, y=-19, height=1, width=1)

    """
    Cases associated with to_dictionary()
    """
    def test_to_dictionary(self):
        self.assertIsInstance(self.my_rect.to_dictionary(), dict)
        
    def test_to_dictionary_attrs_prsnt(self):
        self.assertIn("width", self.my_rect.to_dictionary())
        self.assertIn("height", self.my_rect.to_dictionary())
        self.assertIn("x", self.my_rect.to_dictionary())
        self.assertIn("y", self.my_rect.to_dictionary())
        self.assertIn("id", self.my_rect.to_dictionary())

        # self.my_rect = Rectangle(10, 15, 20, 25, 120)
        self.assertEqual(self.my_rect.width, self.my_rect.to_dictionary()["width"])
        self.assertEqual(self.my_rect.height, self.my_rect.to_dictionary()["height"])
        self.assertEqual(self.my_rect.x, self.my_rect.to_dictionary()["x"])
        self.assertEqual(self.my_rect.y, self.my_rect.to_dictionary()["y"])
        self.assertEqual(self.my_rect.id, self.my_rect.to_dictionary()["id"])

    def test_to_dictionary_with_args(self):
        with self.assertRaises(TypeError):
            self.my_rect.to_dictionary("string")

    """
    Cases associated with to_json_string
    """
    def test_to_json_string(self):
        self.assertIsInstance(self.my_rect.to_json_string(self.my_dict), str)

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            self.my_rect.to_json_string()
    
    def test_to_json_string_nondict(self):
        self.assertIsInstance(self.my_rect.to_json_string([1, 2, 3]), str)
    """
    JSON string to file test cases
    """
    def test_save_to_file(self):
        self.my_rect.save_to_file(self.json_str)
        self.assertTrue(os.path.exist(self.file_name)

if __name__ == '__main__':
    unittest.main()
