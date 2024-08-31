#!/usr/bin/python3
"""
the entry point of the command interprete
"""

import json
import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    where it starts
    """
    prompt = "(hbnb) "
    class_check = ["BaseModel"]

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

    def emptyline(self):
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        lamulo = shlex.split(arg)
        if len(lamulo) == 0:
            print("** class name missing **")
        elif lamulo[0] not in self.class_check:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        lamulo = shlex.split(arg)
        if len(lamulo) == 0:
            print("** class name missing **")
        elif lamulo[0] not in self.class_check:
            print("** class doesn't exist **")
        elif len(lamulo) < 2:
            print("** instance id missing **")
        else:
            store = storage.all()
            key = "{}.{}".format(lamulo[0], lamulo[1])
            if key in store:
                print(store[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        lamulo = shlex.split(arg)
        if len(lamulo) == 0:
            print("** class name missing **")
        elif lamulo[0] not in self.class_check:
            print("** class doesn't exist **")
        elif len(lamulo) < 2:
            print("** instance id missing **")
        else:
            store = storage.all()
            key = f"{lamulo[0]}.{lamulo[1]}"
            if key in store:
                del store[key]
                storage.save()
            else:
                print("** no instance found **")

    """
    def do_all(self, arg):
        Prints all string representation of all instances
        based or not on the class name
        store = storage.all()
        lamulo = shlex.split(arg)

        if len(lamulo) == 0:
            for key, Value in store.items():
                if key.split(',')[0] == lamulo[0]:
                    print(str(value))
    """

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        lamulo = shlex.split(arg)
        if len(lamulo) == 0:
            print("** class name missing **")
        elif lamulo[0] not in self.class_check:
            print("** class doesn't exist **")
        else:
            store = storage.all()
            instances = [
                str(obj)
                for key, obj in store.items()
                if key.split('.')[0] == lamulo[0]
            ]
            print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """

        lamulo = shlex.split(arg)
        if len(lamulo) == 0:
            print("** class name missing **")
        elif lamulo[0] not in self.class_check:
            print("** class doesn't exist **")
        elif len(lamulo) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(lamulo[0], lamulo[1])
            if key not in objects:
                print("** no instance found **")
            elif len(lamulo) < 3:
                print("** attribute name missing **")
            elif len(lamulo) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attri_name = lamulo[2]
                attri_value = lamulo[3]

            try:
                attri_value = eval(attri_value)
            except Exception:
                pass
            setattr(obj, attri_name, attri_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
