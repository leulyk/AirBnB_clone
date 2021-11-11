#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - command line interface implementation
    """

    classes = {
        BaseModel: BaseModel
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
        new = line.partition(" ")
        class_name = new[0]
        class_id = new[1]

        if not class_name:
            print("** class name missing **")
        
        if not class_id:
            print("** instance id missing **")

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")

        #guard aganist trailing whitespace
        if class_id and " " in class_id:
            class_id = class_id.partition(" ")[0]

        class_key = class_name + "." + class_id

        try:
            print(storage.FileStorage.objects[class_key])
        except KeyError:
            print("** no instance found **")
            

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == "__main__":
    HBNBCommand().cmdloop()
