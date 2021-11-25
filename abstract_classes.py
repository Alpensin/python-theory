from abc import ABC, abstractmethod
# abc is a builtin module, we have to import ABC and abstractmethod

class Animal: # Inherit from ABC(Abstract base class)
    @abstractmethod  # Decorator to define an abstract method
    def feed(self):
        pass

# WRONG - TypeError: Can't instantiate abstract class Dog with abstract methods feed
class Dog(Animal): 
    def to_feed(self):
        print("aa")

# CORRECT
class Dog(Animal): 
    def feed(self):
        print("aca")

# Writing abstract methods with parameters
# What happens when an abstract method has parameters? When the subclass implements the method, it must contain all the parameters as well. The subclass' implementation can also add extra parameters if required.

from abc import ABC,abstractmethod 

class Animal(ABC):
    @abstractmethod  
    def do(self, action): # Renamed it to "do", and it has "action" parameter
        pass

class Lion(Animal): 
    def do(self, action, time): # It's still mandatory to implement action. "time" is our other parameter
        print(f"{action} a lion! At {time}") 

class Panda(Animal): 
    def do(self, action, time): 
        print(f"{action} a panda! At {time}") 

class Snake(Animal): 
    def do(self, action, time): 
        print(f"{action} a snake! At {time}")


if __name__ == '__main__':
    d = Dog()
    d.feed()
    zoo = [Lion(), Panda(), Snake()]
    for animal in zoo:
        animal.do(action="feeding", time="10:10 PM")