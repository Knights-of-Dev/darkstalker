# animus.py

from types import MappingProxyType
import sys
sys.tracebacklimit = 0

temp_objects = {
    "environment": {
        "weather": None,
        "sky": {"sun": None, "moon-closest": None, "moon-middle": None, "moon-farthest": None},
        "land": {
            "mountain": {"all": None, "range": {"clawsOfTheClouds": None, "darkstalkersTeeth": None}, "single": {"jadeMountain": None, "agateMountain": None, "borderlandMountain": None}},
            "kingdom": {"all": None, "iceKingdom": None, "nightKingdom": None, "kingdomOfSand": None, "skyKingdom": None, "mudKingdom": None, "rainforestKingdom": None}
        },
        "water": {
            "kingdom": {"kingdomOfTheSea": None}
        }
    },
    "creature": {
        "animal": {"all": None, "sloth": None, "unknown": None},
        "dragon": {"all": None, "icewing": None, "sandwing": None, "skywing": None, "mudwing": None, "rainwing": None, "nightwing": None, "seawing": None},
        "scavenger": {"all": None}
        }
}

objects = MappingProxyType(temp_objects)
del temp_objects

global debug; debug = False

class world_object:
    def __init__(self, livestat=None, a=None, b=None, c=None, d=None):
        self.livestat = livestat
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.isEnchanted = False
        self.objectName = f"{self.livestat}"
        if self.a != None: self.objectName = f"{self.objectName}.{self.a}"
        if self.b != None: self.objectName = f"{self.objectName}.{self.b}"
        if self.c != None: self.objectName = f"{self.objectName}.{self.c}"
        if self.d != None: self.objectName = f"{self.objectName}.{self.d}"
        if debug: print(f"Created object: {self.objectName}")
        if self.livestat in objects:
            if self.a != None and self.a in objects[self.livestat]:
                if self.b != None and self.b in objects[self.livestat][self.a]:
                    if self.c != None and self.c in objects[self.livestat][self.a][self.b]:
                        if self.d != None and self.d in objects[self.livestat][self.a][self.b][self.c]:
                            pass
                        else:
                            if self.d != None: raise Exception(f"Unknown subtype: \"{self.d}\" for object: \"{self.livestat}.{self.a}.{self.b}.{self.c}\"")
                    else:
                        if self.c != None: raise Exception(f"Unknown subtype: \"{self.c}\" for object: \"{self.livestat}.{self.a}.{self.b}\"")
                else:
                    if self.b != None: raise Exception(f"Unknown subtype: \"{self.b}\" for object: \"{self.livestat}.{self.a}\"")
            else:
                if self.a != None: raise Exception(f"Unknown subtype: \"{self.a}\" for object: \"{self.livestat}\"")
        else:
            raise Exception(f"Unknown object type: \"{self.livestat}\"")
        if self.a != None:
            if self.b == None:
                if isinstance(objects[self.livestat][self.a], (dict, list)):
                    print(f"Warning! \"{self.a}\" has no further specifiers. This will select a subtype at random!")
            elif self.c == None:
                if isinstance(objects[self.livestat][self.a][self.b], (dict, list)):
                    print(f"Warning! \"{self.b}\" has no further specifiers. This will select a subtype at random!")
            elif self.d == None:
                if type(objects[self.livestat][self.a][self.b][self.c]) != str:
                    if isinstance(objects[self.livestat][self.a][self.b][self.c], (dict, list)):
                        print(f"Warning! \"{self.c}\" has no further specifiers. This will select a subtype at random!")
        else:
            if isinstance(objects[self.livestat], (dict, list)):
                print(f"Warning! \"{self.livestat}\" has no further specifiers. This will select a subtype at random!")
    
    def getData(self, autoprint=False):
        tup = tuple(self.objectName.split("."))
        if autoprint or debug: print(tup)
        return (tup)
    def enchant(self, autoprint=False):
        self.isEnchanted = True
        if debug or autoprint: print(f"Object {self.objectName} has been enchanted.")
        return True
    def disenchant(self, autoprint=False):
        self.isEnchanted = False
        if debug or autoprint: print(f"Object {self.objectName} has been disenchanted.")
        return False
    def command(self, cmd, autoprint=False):
        if self.isEnchanted:
            result = f"Object {self.objectName} executed command: {cmd}"
            if autoprint or debug: print(result)
            return result
        else:
            error_msg = "Error: Object is not enchanted."
            if autoprint or debug: print(error_msg)
            return error_msg
    
def multicommand(*args, cmd, autoprint=False):
    se = []
    for ar in args:
        if isinstance(ar, world_object):
            if ar.isEnchanted:
                se.append(ar.objectName)
                if autoprint or debug: print(f"Object {ar.objectName} added to the selection.")
            else:
                if autoprint or debug: print(f"Object {ar.objectName} is not enchanted and was ignored.")
        else:
            print(f"Non-world object ignored by multiselect: {ar}")
    if autoprint or debug: print(f"Selected objects ({se}) executed command: {cmd}")
    return se