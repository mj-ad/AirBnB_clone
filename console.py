#!/usr/bin/python3
""" class HBNBCommand """
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {'BaseModel',
                 'User',
                 'State',
                 'City',
                 'Amenity',
                 'Place',
                 'Review'
                 }

    def do_quit(self, arg):
        """ to exit the program """
        sys.exit()

    def help_quit(self):
        print('Quit command to exit the program')

    def do_create(self, line):
        if len(line) == 0:
            print('** class name missing **')
        else:
            try:
                self.obj = eval(line + '()')
                storage.save()
                print(self.obj.id)
            except NameError:
                print("** class doesn't exist **")

    def help_create(self):
        print('Creates a new instance of BaseModel, \
saves it (to the JSON file) and prints the id')

    def do_show(self, line):
        args = line.split()
        obj = storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        elif '{}.{}'.format(args[0], args[1]) not in obj:
            print('** no instance found **')
        else:
            print(obj['{}.{}'.format(args[0], args[1])])

    def help_show(self):
        print('Prints the string representation \
of an instance based on the class name and id')

    def do_destroy(self, line):
        args = line.split()
        obj = storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        elif '{}.{}'.format(args[0], args[1]) not in obj:
            print('** no instance found **')
        else:
            del obj['{}.{}'.format(args[0], args[1])]
            storage.save()

    def help_destroy(self):
        print('Deletes an instance based on the class name and id')

    def do_all(self, line):
        new_obj = []
        args = line.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    new_obj.append(obj.__str__())
                elif len(args) == 0:
                    new_obj.append(obj.__str__())
            print(new_obj)

    def help_all(self):
        print('Prints all string representation of all \
instances based or not on the class name')

    def do_update(self, line):
        pass

    def do_EOF(self, line):
        """ to quit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
