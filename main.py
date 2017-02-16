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

    aint = 11
    print ("number: ", aint)
    print ("adding 2: ", aint + 2)
    print ("subing 2: ", aint -2)
    print ("mult 2: ", aint * 2)
    print ("div 2: ", aint /2)
    print ("pow 2: ", aint ** 2)

    print ("checking int: {}", format(type(aint) is int) )
    print ("checking int: {}".format(type(aint) is int) )

    aint += 2
    print ("+= 2:", aint )

    print ("some_bool", some_bool)
    print ("not_some_bool", not some_bool)

    try:
        print("a/b: ",some_int/aint)
    except:
        print("issues")
    
    aint = 0
    
    try:
        print("a/b: ",some_int/aint)
    except Exception as e:              #Exception is the default error, saved as e, and then printed
        print("issues: ", e)
        # raise  # will crash 
    else:                               #if no error
        print ("no issues")
    finally:                            #either way 
        print ("moving on")             #this is for when youve dealt with soemthing, and jsut want to tidy up? I think

    

