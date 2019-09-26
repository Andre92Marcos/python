**import and from**

from urllib import request # access request directly. 
mine = request() 

import urllib.request # used as urllib.request 
mine = urllib.request()


**__name__ == __main__**

Before executing the code, it will define a few special variables. For example, if the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.

One reason for doing this is that sometimes you write a module (a .py file) where it can be executed directly. Alternatively, it can also be imported and used in another module. By doing the main check, you can have that code only execute when you want to run the module as a program and not have it execute when someone just wants to import your module and call your functions themselves.

**pass**

It is used when a statement is required syntactically but you do not want any command or code to execute.

The pass statement is a null operation

**Threads**

t = Thread(target=functionToRun, args=(argsFor the funtion to run))
t.start()

Example

t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
t.start()
