#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - command line interface implementation
    """

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Review": Review,
        "Amenity": Amenity
    }
    # intro = "Welcome to the hbnb console"
    prompt = "(hbnb) "
    file = None

    def do_quit(self, line):
        # print("Thankyou for using hbnb console")
        self.close()
        quit()

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """ handle EOF """
        return True

    def help_quit(self):
        print('\n'.join(['Quit command to exit the program\n']))

    def do_create(self, line):
        """Creates an object of any available class"""
        if not line:
            print("** class name missing **")
            return
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.classes[line]()
        storage.save()
        print(new_instance.id)

    def do_show(self, line):
        """show string representation of an object instance"""
        result = self.test_arguments(line)

        if result[0]:
            class_key = result[1] + "." + result[2]
            try:
                print(storage._FileStorage__objects[class_key])
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """
            prints all instances created or all instances of a
            certain class
        """
        if line and line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        lst = []
        for key, value in storage._FileStorage__objects.items():
            if line:
                if key.partition('.')[0] == line:
                    lst.append(str(storage._FileStorage__objects[key]))
            else:
                lst.append(str(storage._FileStorage__objects[key]))
        print(lst)

    def do_destroy(self, line):
        """ deletes an instance based on class name or id """
        result = self.test_arguments(line)

        if result[0]:
            class_key = result[1] + "." + result[2]
            if class_key in storage._FileStorage__objects.keys():
                del storage._FileStorage__objects[class_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, line):
        """
            updates an instance based on class name and id by adding or
            updating attribute
        """
        result = self.test_arguments(line)
        if result[0]:
            tokens = line.split()
            if len(tokens) < 4:
                if len(tokens) == 2:
                    print("** attribute name missing **")
                    return
                elif len(tokens) == 3:
                    print("** value missing **")
                    return
            class_key = result[1] + "." + result[2]
            if class_key in storage._FileStorage__objects.keys():
                setattr(storage._FileStorage__objects[class_key],
                        tokens[2], tokens[3])
                storage.save()
            else:
                print("** no instance found **")

    def test_arguments(self, line):
        """ test class existence, class name and instance id """
        new = line.partition(" ")
        class_name = new[0]
        class_id = new[2]
        success = 1

        if not class_name:
            print("** class name missing **")
            success = 0

        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            success = 0

        elif not class_id:
            print("** instance id missing **")
            success = 0

        # guard aganist trailing whitespace
        if class_id and " " in class_id:
            class_id = class_id.partition(" ")[0]

        return (success, class_name, class_id)

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == "__main__":
    HBNBCommand().cmdloop()
