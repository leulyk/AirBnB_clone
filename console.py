#!/usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - command line interface implementation
    """

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
        return True


    def help_quit(self):
        print('\n'.join(['Quit command to exit the program\n']))

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == "__main__":
    HBNBCommand().cmdloop()

