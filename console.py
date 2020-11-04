#!/usr/bin/python3
import cmd
from models.engine.file_storage import FileStorage
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.places import Place
from models.review import Review
""" HBNB command 2"""


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to hbnb shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None

    # ----- basic hbnb commands -----

    def emptyline(self):
        """empty spaces"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program.\n"""
        return True

    def do_EOF(self, arg):
        """eof quit command"""
        print()
        return True

    def do_create(self, arg):
        """Create command"""

        if len(arg) == 0:
            print("** class name missing **")
            return
        try:
            args = split(arg)
            newObj = eval(args[0])()
            newObj.save()
            print(newObj.id)
        except BaseException:
            print("** class doesn't exist **")

    def do_show(self, line):
        """show command """

        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        objDict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        try:
            value = objDict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """ Destroy command """

        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        clsName = args[0]
        clsId = args[1]
        storage = FileStorage()
        storage.reload()
        objDict = storage.all()

        try:
            eval(clsName)

        except NameError:
            print("** class doesn't exist **")
            return

        key = clsName + "." + clsId

        try:
            del objDict[key]

        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_all(self, line):
        """ all command """

        objList = []
        storage = FileStorage()
        storage.reload()
        objs = storage.all()

        try:
            if len(line) != 0:
                eval(line)

        except NameError:
            print("** class doesn't exist **")
            return
        for _, value in objs.items():
            if len(line) != 0:
                if isinstance(value, eval(line)):
                    objList.append(value)
            else:
                objList.append(value)
        for i in objList:
            print(i)
        print(objList)

    def do_update(self, line):
        """ update command """

        storage = FileStorage()
        storage.reload()
        args = split(line)

        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        try:
            eval(args[0])

        except NameError:
            print("** class doesn't exist **")
            return

        key = args[0] + "." + args[1]
        objDict = storage.all()

        try:
            objVal = objDict[key]

        except KeyError:
            print("** no instance found **")
            return

        try:
            attrType = type(getattr(objVal, args[2]))
            args[3] = attrType(args[3])

        except AttributeError:
            pass

        setattr(objVal, args[2], args[3])
        objVal.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
