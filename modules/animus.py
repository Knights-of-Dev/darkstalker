# i have hippopotomonstrosesquippedaliophobia

"""
REMINDER: after creating every primitive function, remove these comments which bloat everything!
"""

import math
# this may be useful later.

global debug; debug = False
# i didnt know you could put a semicolon IN PYTHON

def ifelse(con, tru=True, fal=False):
    if con:
        return tru
    else:
        return fal

class object:
    def __init__(self, livestat=None, a=None, b=None, c=None):
        self.livestat = livestat
        self.a = a
        self.b = b
        self.c = c
        self.isEnchanted = False
        self.objectName = f"{self.livestat}"
        if self.a != None: self.objectName = f"{self.objectName}.{self.a}"
        if self.b != None: self.objectName = f"{self.objectName}.{self.b}"
        if self.c != None: self.objectName = f"{self.objectName}.{self.c}"
    # i feel like this is a good place to stop and reflect on my life choices
    def getData(self, autoprint=False):
        if autoprint or debug: print((self.livestat, self.a, self.b, self.c))
        return (self.livestat, self.a, self.b, self.c)
    def enchant(self, autoprint=False):
        self.isEnchanted = True
        if debug or autoprint: print(f"Object {self.objectName} has been enchanted.")
    def disenchant(self, autoprint=False):
        self.isEnchanted = False
        # debug and autoprint are pretty good together :3
        if debug or autoprint: print(f"Object {self.objectName} has been disenchanted.")
    def command(self, cmd, autoprint=False):
        if self.isEnchanted:
            result = f"Object {self.objectName} executed command: {cmd}"
            if autoprint or debug: print(result)
            return result
        else:
            error_msg = "Error: Object is not enchanted."
            if autoprint or debug: print(error_msg)
            return error_msg
        
a = input("Enable debug mode? (true/false): ")
debug = ifelse(a.lower() == "true")
print(debug)
a = object("dragon", "icewing", "all")
a.enchant()
a.command("fly to the north")