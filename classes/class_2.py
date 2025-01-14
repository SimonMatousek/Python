

empty_list_1= []
empty_list_2 = list()

emty_tuple_1 = ()
emty_tuple_2 = tuple()


emty_set_1 = ()
empty_set_2 = set()

set_example = {1,2,3,4,5,5,5,5,5,6}

print(f"{set_example=}")

print(f"{type(empty_list_1)=}")
print(f"{type(empty_list_2)=}")

print(f"{empty_list_1=}")
print(f"{empty_list_2=}")

print(f"{emty_tuple_1=}")
print(f"{emty_tuple_2=}")

# one Line Command

""" sdfds
sdfdsf
sdfds
dsf 
crtl + shift + A multi line command
"""


def number_square(numer):
    """Gives power of number

    Args:
        numer (integer)

    Returns:
        integer 
    """
    return number ** 2

#print(help(number_square))
#print(number_square._doc_)
class Creature:
    def __init__(self, height, weight, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.height = height
        self.weight = weight
        
    def breath(self) -> None:
        print("I can breath")
        
class Employe:
    def __init__ (self, salary, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.salary = salary 
        
    def working(self) -> None:
        print("im working")
class Person(Creature, Employe):
    
    """
    name -> public
    _name -> protected
    __name -> private
    """
    
    def __init__ (self, name, weight, height, salary) -> None: # self instat of this
        super().__init__(height=height, weight=weight, salary= salary)
        self.name = name
        
    def walk(self) -> None:
        print("I walk")

    
class B:
    ...
    
class C:
    pass
def add(*args):
    return args

from pathlib import Path

PATH_ROOT_DIR = Path(__file__).parent
PATH_TXT = PATH_ROOT_DIR / "text.txt"

with open(PATH_TXT , "r") as txt_file:
    lines = txt_file.readlines()
    for index, line in enumerate(lines):
        print(f"{index + 1}. {line}")

print(type(3))
word = input("Give me a Word: ")
print(f"{word=}")

numbers = [1,2,3,4,4,5,]
print(f"{max(numbers)=}")
print(f"{min(numbers)=}")
print(f"{sum(numbers)=}")

sorted_numbers = sorted(numbers)
print(sorted_numbers)

names = ["aa", "AA", "bbb", "B"]
sorted_names = sorted(names)
print(sorted_numbers)
#zip, filter, map, eval
exec("x = 5")
print(f"{x=}")

from math import floor
"""

sys
os
math
datetime
time
string

PIP
"""
if __name__ == "__main__":
    michalis = Person(name= "Michalis", height=185, weight=83, salary=1_000)
    """ michalis.walk()
    michalis.breath
"""


        