#!/usr/bin/python3
"""
Module for console
"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Command Line Module Class"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Method to quit command line"""
        exit()

    def do_EOF(self, line):
        """Method for End Of File"""
        return True

    def do_create(self, line):
        """Creates new instance of class called"""
        command = shlex.split(line)
        if len(command) < 1:
            print("** class name missing **")
            return
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")
            return
        print(obj.id)
        storage.new(obj)
        storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        command = shlex.split(line)
        if len(command) < 1:
            print("** class name missing **")
            return
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")
            return
        if len(command) < 2:
            print("** instance id is missing **")
            return

        key = command[0] + '.' + command[1]
        if key not in storage.all():
            print("** no instance found **")
        print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        command = shlex.split(line)
        if len(command) < 1:
            print("** class name missing **")
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")
            return
        if len(command) < 2:
            print("** instance id is missing **")
            return

        key = command[0] + '.' + command[1]
        if key not in storage.all():
            print("** no instance found **")
        del(storage.all()[key])

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name."""
        command = shlex.split(line)
        objects = list(storage.all().values())
        if len(command) < 1:
            for obj in objects:
                print(obj)
            return
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")
            return
        if command[0]:
            for obj in objects:
                if command[0] == obj.__class__.__name__:
                    print(obj)

    def do_update(self, line):
        """Method for updating class object"""
        command = shlex.split(line)
        if len(command) < 1:
            print("** class name missing **")
            return
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")
            return
        if len(command) < 2:
            print("** instance id is missing **")
            return
        key = command[0] + '.' + command[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(command) < 3:
            print("** attribute name missing **")
            return
        if len(command) < 4:
            print("** value missing **")
            return
        try:
            command[3] = int(command[3])
        except:
            try:
                command[3] = float(command[3])
            except:
                pass
        key = command[0] + '.' + command[1]
        setattr(storage.all()[key], command[2], command[3])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
