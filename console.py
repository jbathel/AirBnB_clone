#!/usr/bin/python3
"""
Module for console
"""
from models.base_model import BaseModel
from models.review import Review
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """..."""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """..."""
        exit()

    def do_EOF(self, line):
        """..."""
        return True

    def do_create(self, line):
        """Creates new instance of class called"""
        command = line.split(' ')
        if command[0] is '':
            print("** class name missing **")
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")
        print(obj.id)
        storage.new(obj)
        storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        command = line.split(' ')
        if command[0] is '':
            print("** class name missing **")
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")

        if command[1] is '':
           print("** instance id is missing **")

        key = command[0] + '.' + command[1]
        if key not in storage.all():
            print("** no instance found **")
        print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        command = line.split(' ')
        if command[0] is '':
            print("** class name missing **")
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")

        if command[1] is '':
           print("** instance id is missing **")

        key = command[0] + '.' + command[1]
        if key not in storage.all():
            print("** no instance found **")
        del(storage.all()[key])

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name."""
        command = line.split(' ')
        objects = list(storage.all().values())
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")
        if command[0]:
            for obj in objects:
                if command[0] == obj.__class__.__name__:
                    print(obj)
        else:
            for obj in objects:
                print(obj)

    def do_update(self, line):
        """..."""
        command = line.split(' ')
        datatype = ''
        if command[0] is '':
            print("** class name missing **")
        try:
            obj = eval(command[0] + '()')
        except:
            print("** class doesn't exist **")

        if command[1] is '':
           print("** instance id is missing **")

        key = command[0] + '.' + command[1]
        if key not in storage.all():
            print("** no instance found **")
        if command[2] is '':
            print("** attribute name missing **")
        if command[3] is '':
            print("** value missing **")
        try:
            command[3] = int(command[3])
            datatype = 'int'
        except:
            try:
                command[3] = float(command[3])
                datatype = 'float'
            except:
                datatype = 'string'
        if datatype == 'string':
            if (command[3][0] == '"' or command[3][-1] == '"') or\
            (command[3][0] == "'" or command[3][-1] == "'"):
                command[3] = command[3].replace('"', '')
                command[3] = command[3].replace("'", '')
        key = command[0] + '.' + command[1]
        setattr(storage.all()[key], command[2], command[3])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
