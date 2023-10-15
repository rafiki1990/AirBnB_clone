#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
    
        return True

    def do_EOF(self, arg):

        print()
        return True

    def do_emptyline(self, help):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
