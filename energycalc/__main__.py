from .energy import *
import sys
import doctest
if __name__=="__main__":
    args=sys.argv
    if len(args)>1:
        if args[1].upper()=="TEST":
            doctest.testfile("test.py",verbose=True)
        else:
            print("Bad Input")
    else:
        print_sign()
        print("Total :"+get_input())
        input()