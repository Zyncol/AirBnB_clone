#!/usr/bin/python3
"""
the entry point of the command interprete
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    where it starts
    """
    prompt = "(hbnb)"

    def help_quit(self, arg):
        """
        for quit
        """
        print("To exit program please quit")

    def do_quit(self, arg):
        """
        on quit
        """
        return True

    def do_EOF(self, arg):
        """
        exit
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
