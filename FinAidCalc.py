import os


def Main():
    TextParser(input("Enter filename: "))


def TextParser(filename):
    if not os.path.isfile(filename):
        print('File does not exist! Quitting program.')
        quit()
    pfile = open(filename, "r")
    print('test')
    pfile.close()


Main()
