# i have hippopotomonstrosesquippedaliophobia

"""
REMINDER: after creating every primitive function, remove these comments which bloat everything!
"""


from types import MappingProxyType # the only thing its good for

import sys
sys.tracebacklimit = 0 # might actually turn this into a from import later

temp_objects = {
    "environment": {
        "sky": ["sun", "moon-closest", "moon-middle", "moon-farthest"],
        "land": {
            "mountain": ["all", {"range": ["clawsOfTheClouds", "darkstalkersTeeth"]}, {"single": ["jadeMountain", "agateMountain", "borderlandMountain"]}],
            "kingdom": ["all", "iceKingdom", "nightKingdom", "kingdomOfSand", "skyKingdom", "mudKingdom", "rainforestKingdom"]
        },
        "water": {
            "kingdom": "kingdomOfTheSea"
        }
    },
    "creature": {
        "animal": ["all", "sloth", "unknown"],
        "dragon": ["all", "icewing", "sandwing", "skywing", "mudwing", "rainwing", "nightwing", "seawing"],
        "scavenger": ["all"]
        }
}
objects = MappingProxyType(temp_objects)
temp_objects = None

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
        if debug: print(f"Created object: {self.objectName}")
        if self.livestat in objects:
            if self.a != None and self.a in objects[self.livestat]:
                if self.b != None and self.b in objects[self.livestat][self.a]:
                    if self.c != None and self.c in objects[self.livestat][self.a][self.b]:
                        pass
                    else:
                        if self.c != None: raise Exception(f"Unknown subtype: \"{self.c}\" for object: \"{self.livestat}\"")
                else:
                    if self.b != None: raise Exception(f"Unknown subtype: \"{self.b}\" for object: \"{self.livestat}\"")
            else:
                if self.a != None: raise Exception(f"Unknown subtype: \"{self.a}\" for object: \"{self.livestat}\"")
        else:
            raise Exception(f"Unknown object type: \"{self.livestat}\"")
        # detect if the last option given is a key and not a list item
        if self.a != None:
            if self.b == None:
                if isinstance(objects[self.livestat][self.a], (dict, list)):
                    print(f"Warning! \"{self.a}\" has no further specifiers. This will select a subtype at random!")
            else:
                if self.c == None:
                    if isinstance(objects[self.livestat][self.a][self.b], (dict, list)):
                        print(f"Warning! \"{self.b}\" has no further specifiers. This will select a subtype at random!")
        else:
            if isinstance(objects[self.livestat], (dict, list)):
                print(f"Warning! \"{self.livestat}\" has no further specifiers. This will select a subtype at random!")
    
    # i feel like this is a good place to stop and reflect on my life choices
    # ...
    # ok back to work

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
    def multicommand(self, *args, cmd, autoprint=False):
        se = []
        for ar in args:
            if isinstance(ar, object):
                if ar.isEnchanted:
                    se.append(ar)
            else:
                print(f"Non-object ignored by multiselect: {ar}") # no i wont change it to multicommand
        if autoprint or debug: print(f"Selected objects ({se}) executed command: {cmd}")
        return se

#deltarunetomorrow

a = input("Enable debug mode? (true/false): ")
debug = ifelse(a.lower() == "true")
print(debug)
a = object("creature", "dragon")
a.enchant()
a.command("fly to the SOUTH!! ha ha")
print(type(a))