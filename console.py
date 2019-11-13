#!/usr/bin/python3
"""
Module for console
"""
import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """Command Line Module Class"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Empty Line"""
        pass

    def do_quit(self, line):
        """
        Quits the command line - type 'quit' to exit command line
        """
        return True

    def do_EOF(self, line):
        """
        EOF - Press C^d to quit command line
        """
        return True

    def do_create(self, line):
        """
        Creates new instance of a class called by user:
        Amenity, City, Place, State, Review, User
        """
        try:
            command = shlex.split(line)
        except:
            return
        if len(command) < 1:
            print("** class name missing **")
            return
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")
            return
        print(obj.id)
        models.storage.new(obj)
        models.storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        try:
            command = shlex.split(line)
        except:
            return
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
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id -
        type destroy <class name>
        """
        try:
            command = shlex.split(line)
        except:
            return
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
        if key not in models.storage.all():
            print("** no instance found **")
        del(models.storage.all()[key])
        models.storage.save()

    def do_all(self, line):
        """
        Prints a string representation of instances
        based on the class name or all instances if not
        specified - type all <class name>.
        """
        try:
            command = shlex.split(line)
        except:
            return
        objects = list(models.storage.all().values())
        if len(command) < 1:
            for obj in objects:
                print(obj)
            return
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")
            return
        for obj in objects:
            if command[0] == obj.__class__.__name__:
                print(obj)

    def do_update(self, line):
        """
        Updates class object based on input - type <attribute, value>
        """
        try:
            command = shlex.split(line)
        except:
            return
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
        setattr(models.storage.all()[key], command[2], command[3])
        setattr(models.storage.all()[key], 'updated_at', datetime.now())
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
