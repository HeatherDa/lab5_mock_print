'''Lab 5 group subject 2 mock print( Ryan | Iniebiyo | Jeremy | Heather )'''
import unittest
from unittest.mock import Mock, patch
import Print
import builtins


class unit_test_print(unittest.TestCase):


    @patch('builtins.print')
    def test_returned_print(self, mock_print):

        Print.print_asdfgh()
        mock_print.assert_called_with("asdfgh")


    @patch('builtins.print')
    def test_print_three_lines(self, mock_print):

        Print.print_three_lines()
        self.assertEqual(3, mock_print.call_count)
