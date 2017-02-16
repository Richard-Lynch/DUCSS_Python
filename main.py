"""
#     Created by Richard Lynch 
# 
# python -v will check python type
# from x import y

"""
import sys

some_var = "abc"
some_string = "anna"
some_string2 = "abc 123"
some_int = 10
some_float = 1.23
some_bool = True
some_bool2 = False
some_null = None

print (some_var)

if __name__ == "__main__": #treats this as main? maybe i think
    
    sys.stdout.write('ehhh\n')
    print ("testing")
    print ("ah this is handy")

    print (some_string)
    print ("some_string[0]: " + some_string[0])
    print (some_string * 3)
    print ("somte_string: ", some_string)
    print ("split some_string2: ", some_string2.split())
    print ("some string[2:]", some_string2[2:])
    print ("some string[-1]", some_string2[-1])
    print ("some string[-2]", some_string2[-2])
    print ("some string[::-1]", some_string2[::-1]) #-1 is step

    
    print (some_int)
    print (some_float)
    print (some_bool)
    print (some_null)