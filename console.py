#!/usr/bin/python3
""" class HBNBCommand """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """ to exit the program """
        sys.exit()

    def help_quit(self):
        print('Quit command to exit the program')
        
    def do_EOF(self, line):
        """ to quit the program """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
