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


# Writing (abstract) properties
# We may also want to create abstract properties and force our subclass to implement those properties. This could be done by using @property decorator along with @absctractmethod.

# Since animals often have different diets, we'll need to define a diet in our animal classes. Since all the animals are inheriting from Animal, we can define diet to be an abstract property. Besides diet, we'll make food_eaten property and it's setter will check if we are trying to feed the animal something that's not on it's diet.

# Take a look at the code of Animal, Lion and Snake:

class Animal(ABC):
    @property                 
    def food_eaten(self):     
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}.")

    @property
    @abstractmethod
    def diet(self):
        pass

    @abstractmethod 
    def feed(self, time):
        pass

class Lion(Animal):
    @property                 
    def diet(self):     
        return ["antelope", "cheetah", "buffaloe"]

    def feed(self, time):
        print(f"Feeding a lion with {self._food} meat! At {time}") 

class Snake(Animal):
    @property                 
    def diet(self):     
        return ["frog", "rabbit"]

    def feed(self, time): 
        print(f"Feeding a snake with {self._food} meat! At {time}") 


if __name__ == '__main__':
    d = Dog()
    d.feed()
    zoo = [Lion(), Panda(), Snake()]
    for animal in zoo:
        animal.do(action="feeding", time="10:10 PM")