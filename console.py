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
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Command Line Module Class"""

    prompt = '(hbnb) '

    def precmd(self, line):
        """Precommand method"""
        try:
            first_split = line.split('.')
            try:
                model = eval(first_split[0] + '()')
                if not isinstance(model, BaseModel):
                    raise Exception
            except Exception:
                return line
            model = first_split[0]
            second_split = first_split[1].split('(')
            command = second_split[0]
            parameters = ' '.join(second_split[1][:-1].split(','))
            return " ".join([command, model, parameters])
        except Exception:
            return line

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
        print('')
        return True

    def do_create(self, line):
        """
        Creates new instance of a class called by user:
        Amenity, City, Place, State, Review, User
        """
        try:
            command = shlex.split(line)
        except Exception:
            return
        if len(command) < 1:
            print("** class name missing **")
            return
        try:
            obj = eval(command[0] + '()')
            if not isinstance(obj, BaseModel):
                raise Exception
        except Exception:
            print("** class doesn't exist **")
            return
        print(obj.id)
        storage.new(obj)
        storage.save()
        return

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        try:
            command = shlex.split(line)
        except Exception:
            return
        if len(command) < 1:
            print("** class name missing **")
            return
        try:
            obj = eval(command[0] + '()')
            if not isinstance(obj, BaseModel):
                raise Exception
        except Exception:
            print("** class doesn't exist **")
            return
        if len(command) < 2:
            print("** instance id missing **")
            return

        key = command[0] + '.' + command[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])
        return

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id -
        type destroy <class name>
        """
        try:
            command = shlex.split(line)
        except Exception:
            return
        if len(command) < 1:
            print("** class name missing **")
            return
        try:
            obj = eval(command[0] + '()')
            if not isinstance(obj, BaseModel):
                raise Exception
        except Exception:
            print("** class doesn't exist **")
            return
        if len(command) < 2:
            print("** instance id missing **")
            return

        key = command[0] + '.' + command[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del(storage.all()[key])
        storage.save()
        return

    def do_all(self, line):
        """
        Prints a string representation of instances
        based on the class name or all instances if not
        specified - type all <class name>.
        """
        try:
            command = shlex.split(line)
        except Exception:
            return
        objects = list(storage.all().values())
        if len(command) < 1:
            print([str(obj) for obj in objects])
            return
        try:
            try_obj = eval(command[0] + '()')
            if not isinstance(try_obj, BaseModel):
                raise Exception
        except Exception:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objects
               if command[0] == obj.__class__.__name__])
        return

    def do_update(self, line):
        """
        Updates class object based on input - type <attribute, value>
        """
        try:
            command = shlex.split(line)
        except Exception:
            return
        if len(command) < 1:
            print("** class name missing **")
            return
        try:
            obj = eval(command[0] + '()')
            if not isinstance(obj, BaseModel):
                raise Exception
        except Exception:
            print("** class doesn't exist **")
            return
        if len(command) < 2:
            print("** instance id missing **")
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
        except Exception:
            try:
                command[3] = float(command[3])
            except Exception:
                pass
        key = command[0] + '.' + command[1]
        setattr(storage.all()[key], command[2], command[3])
        setattr(storage.all()[key], 'updated_at', datetime.now())
        storage.save()
        return

    def do_count(self, line):
        """Count method for the Console"""
        try:
            command = shlex.split(line)
        except Exception:
            return
        count = 0
        for key, obj in storage.all().items():
            if obj.__class__.__name__ == str(command[0]):
                count += 1
        print(count)
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
