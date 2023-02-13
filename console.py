#!/usr/bin/python3
""" class HBNBCommand """
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

    def emptyline(self):
        """ Do nothing """
        pass

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
        args = line.split()
        objdict = storage.all()
        if len(args) == 0:
            print('** class name missing **')
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print('** instance id missing **')
            return False
        if '{}.{}'.format(args[0], args[1]) not in objdict.keys():
            print('** no instance found **')
            return False
        if len(args) == 2:
            print('** attribute name missing **')
            return False
        if len(args) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and\
                    type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_EOF(self, line):
        """ to quit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
