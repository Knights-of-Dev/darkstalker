# i have hippopotomonstrosesquippedaliophobia

import math
# this may be useful later.

class object:
    def __init__(self, livestat=None, a=None, b=None, c=None):
        self.livestat = livestat
        self.a = a
        self.b = b
        self.c = c
        self.isEnchanted = False
    def getData(self):
        return (self.livestat, self.a, self.b, self.c)
    def enchant(self):
        self.isEnchanted = True
    def disenchant(self):
        self.isEnchanted = False
    def command(self, cmd):
        if self.isEnchanted:
            return "The object shimmers with a magical aura."
        else:
            return "Error: Object is not enchanted."