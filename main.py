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
    print ("some string[-2:]", some_string2[-2:])
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

    if 2 > 1:
        print ("2 is greater than 1!")
    
    if 2 < 1:
        print ("the fuck")
    elif 3 < 1:
        print ("seriosuly")
    else:
        print ("fair")
    
    var_a = 1

    for var_a in range(1, 3):
        print (var_a)

    print ("working")

    # while var_A <= 10:
    #     print (var_a)
    #     var_a += 2

    def add(a,b):
        addition_result = a+b
        return addition_result
    print ("add (1,2): ", add (1,2))

    def div_mod(a,b):
        bigger = max(a,b)
        smaller = min(a,b)
        div_result = bigger // smaller #just returns coeffeicnt with truncation
        mod_results = bigger % smaller #returns mod
        return div_result, mod_results

    print ("mod, div", div_mod(1,2))

    number_squared = lambda x: x * x        #declare a function inline

    print ("lambda x*x of 2: ", number_squared(2))  #then call the function as normal

    def func_default(a=1, b=2):
        return a+b
    
    print("func defuault: ", func_default())

    def func_var_args(*args, **kwargs):
        print ("args: ", args)
        print ("kwargs: ", kwargs)

        print ("1st arg: ", args[0])
        print ("b Value: ", kwargs['b'])

    func_var_args(1,2,3, a=10, b=12)

    def key_test (a, b, split = False):
        if split:
            return a,b
        return a-b
    
    print("key_test(1,2): ", key_test(1,2))
    print("key_test(1,2, True): ", key_test(1,2,True))


#data struts
    #dictionary
    data = {
        'key': 'value'
    }
    print ("data[key]",data['key'])

    data['key2'] = 'value2'

    print ("data['key2']",data['key2'])

    print("data: ", data)

    print ("data.get['key']",data.get('key', None))

    # print ("data.")

    # list
    dat = [1, 2, '1', 'a']
    print ("dat: ",dat)
    print ("len(dat): ",len(dat))

    print ("dat.append", dat.append([11,21]))

    print ("data pop",dat.pop(0))
    dat.pop() #pops end

    dat.insert(0,11) #at first

    dat.extend([11,21])

    dat[1:5] 
    # sorted(dat)

    # classes

    class Stack:
        def __init__(self):     #any intneral methods needs to start with self or it will be complelty public
            self.items = []
        
        def __str__(self):
            return str(self.items)
        
        def pop(self, position):
            if position != -1:
                return self.items.pop(position)
        
        def push(self, item):
            self.items.insert(0,item)

        def flush(self):
            self.items = []

        def length(self):
            return len(self.items)

        def peek(self):
            return self.items[0]


    obj = Stack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)

    print("Stack", obj)
    print("Stack.items", obj.items)
    print("Top Value", obj.peek())
    print("Stack.length", obj.length())
    print("pop(1)", obj.pop(1))
    print("Stack.items", obj.items)  
    print("Stack.flush", obj.flush())  
    print("Stack", obj)