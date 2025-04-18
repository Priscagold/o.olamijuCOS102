def printinfo(arg1, *vartuple):
    #This is a test """ Regular pattern (*) means 0 or more (+)means 1 or more
    print ("Output is: ")
    print (arg1)
    for var in vartuple:
        print (var)
        return;
printinfo (10)
printinfo (70,60,50);
    