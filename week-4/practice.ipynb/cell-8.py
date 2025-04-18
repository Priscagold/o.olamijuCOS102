total = 50; # This isa global variable.
def sum(arg1, arg2):
    #Add boyh the parameters
    total = arg1 + arg2;
    print ("Inside the function local total: ", total)
    return total;
# Now yu can call sum function
sum (10,20);
print (" Outside the function global total: ", total)