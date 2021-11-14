#!/usr/bin/python3

""" Unit test module to test the console """

from console import HBNBCommand
import unittest
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """ Tests the hbnb console """
    def test_help(self):
        """ tests the help command """
        with patch('sys.stdout', new=StringIO()) as f:
            expected = "List available commands with \"help\" "
            expected += "or detailed help with \"help cmd\".\n"
            HBNBCommand().onecmd("help help")
            output = f.getvalue()
            self.assertTrue(output == expected)
        with patch('sys.stdout', new=StringIO()) as f:
            expected = "Shows string representation of an object instance\n"
            HBNBCommand().onecmd("help show")
            output = f.getvalue()
            self.assertTrue(output == expected)
        with patch('sys.stdout', new=StringIO()) as f:
            expected = "Creates an object of any available class\n"
            HBNBCommand().onecmd("help create")
            output = f.getvalue()
            self.assertTrue(output == expected)
        with patch('sys.stdout', new=StringIO()) as f:
            expected = "Updates an instance based on class name and id by"
            expected += "\n        adding or updating attribute\n"
            HBNBCommand().onecmd("help update")
            output = f.getvalue()
            self.assertTrue(output == expected)
        with patch('sys.stdout', new=StringIO()) as f:
            expected = "Deletes an instance based on class name or id\n"
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue()
            self.assertTrue(output == expected)
        with patch('sys.stdout', new=StringIO()) as f:
            expected = "Prints all instances created or all "
            expected += "instances of a certain class\n"
            HBNBCommand().onecmd("help all")
            output = f.getvalue()
            self.assertTrue(output == expected)
        with patch('sys.stdout', new=StringIO()) as f:
            expected = "Handle End-of-File\n"
            HBNBCommand().onecmd("help EOF\n")
            output = f.getvalue()
            self.assertTrue(output == expected)
        with patch('sys.stdout', new=StringIO()) as f:
            expected = "Counts number of instances of a class\n"
            HBNBCommand().onecmd("help count")
            output = f.getvalue()
            self.assertTrue(output == expected)
        with patch('sys.stdout', new=StringIO()) as f:
            expected = "Quit command to exit the program\n"
            HBNBCommand().onecmd("help quit")
            output = f.getvalue()
            self.assertTrue(output == expected)
