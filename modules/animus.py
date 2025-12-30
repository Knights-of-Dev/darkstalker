# i have hippopotomonstrosesquippedaliophobia

"""
REMINDER: after creating every primitive function, remove these comments which bloat everything!
"""

import math
# this may be useful later.

global debug; debug = False
# i didnt know you could put a semicolon IN PYTHON

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
    def getData(self):
        return (self.livestat, self.a, self.b, self.c)
    def enchant(self):
        self.isEnchanted = True
        if debug: print(f"Object {self.objectName} has been enchanted.")
    def disenchant(self):
        self.isEnchanted = False
        if debug: print(f"Object {self.objectName} has been disenchanted.")
    def command(self, cmd):
        if self.isEnchanted:
            return f"Object {self.objectName} executed command: {cmd}"
        else:
            return "Error: Object is not enchanted."
        

debug = bool(input("Debug?"))
# ask it because yes
a = object("dragon", "icewing")
a.enchant()
print(a.command("fly to the north"))