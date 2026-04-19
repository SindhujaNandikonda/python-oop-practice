# Object-Oriented Programming (OOP) Concepts

## Table of Contents
1. [Classes and Objects](#classes-and-objects)
2. [Encapsulation](#encapsulation)
3. [Inheritance](#inheritance)
4. [Polymorphism](#polymorphism)
5. [Abstraction](#abstraction)
6. [Special Methods](#special-methods)

## Classes and Objects

### What is a Class?
A class is a blueprint for creating objects. It defines the structure (attributes) and behavior (methods) that objects will have.

### What is an Object?
An object is an instance of a class. It contains actual data and can perform actions defined in the class.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"

# Creating an object (instance)
my_dog = Dog("Buddy", "Golden Retriever")
```

## Encapsulation

Encapsulation is the bundling of data (attributes) and methods (functions) into a single unit (class) and hiding internal details.

### Access Modifiers:
- **Public**: Accessible everywhere (no prefix)
- **Protected**: Intended for internal use (prefix with `_`)
- **Private**: Accessible only within the class (prefix with `__`)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
```

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class (parent/base class).

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Dog inherits from Animal and overrides speak()
```

### Types of Inheritance:
- **Single**: One child, one parent
- **Multiple**: One child, multiple parents
- **Multilevel**: Parent → Child → Grandchild
- **Hierarchical**: Multiple children from one parent

## Polymorphism

Polymorphism means "many forms". The same method can behave differently depending on the object calling it.

```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

def animal_sound(animal):
    print(animal.speak())

# Same function, different outputs
animal_sound(Cat())  # Meow
animal_sound(Dog())  # Woof
```

## Abstraction

Abstraction hides complex implementation details and shows only the necessary features.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine starts"

# car = Vehicle()  # Error: Cannot instantiate abstract class
car = Car()  # OK
```

## Special Methods

Special methods (also called dunder methods or magic methods) have double underscores on both sides.

| Method | Purpose |
|--------|---------|
| `__init__` | Constructor, initializes object |
| `__str__` | String representation for users |
| `__repr__` | Official string representation |
| `__len__` | Returns length |
| `__eq__` | Equality comparison |
| `__lt__` | Less than comparison |
| `__add__` | Addition operator |
| `__call__` | Makes object callable |
| `__del__` | Destructor |

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

---

**Resources**: These concepts form the foundation of object-oriented design. Practice implementing them with real-world examples to strengthen your understanding.
