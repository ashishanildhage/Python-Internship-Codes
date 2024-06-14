
''' SOLID Principles'''

def single_responsibility():
    class Journal:
        def __init__(self):
            self.entries = []
            self.count = 0

        def add_entry(self, text):
            self.entries.append(f"{self.count}: {text}")
            self.count += 1

        def remove_entry(self, pos):
            del self.entries[pos]

        def __str__(self):
            return "\n".join(self.entries)

        # break SRP
        def save(self, filename):
            file = open(filename, "w")
            file.write(str(self))
            file.close()

        def load(self, filename):
            pass

        def load_from_web(self, uri):
            pass


    class PersistenceManager:
        def save_to_file(journal, filename):
            file = open(filename, "w")
            file.write(str(journal))
            file.close()


    j = Journal()
    j.add_entry("I cried today.")
    j.add_entry("I ate a bug.")
    print(f"Journal entries:\n{j}\n")

    p = PersistenceManager()
    file = r'c:\temp\journal.txt'
    p.save_to_file(j, file)

    # verify!
    with open(file) as fh:
        print(fh.read())
#   JOURNAL AND MANAGER BELONGS TO

#A class should have one and only one reason to change, meaning that a class should have only one job.
#For example, consider an application that takes a collection of shapes—circles and squares—and calculates 
#  the sum of the area of all the shapes in the collection.

def open_closed():
    from enum import Enum


    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3


    class Size(Enum):
        SMALL = 1
        MEDIUM = 2
        LARGE = 3


    class Product:
        def __init__(self, name, color, size):
            self.name = name
            self.color = color
            self.size = size


    class ProductFilter:
        def filter_by_color(self, products, color):
            for p in products:
                if p.color == color: yield p

        def filter_by_size(self, products, size):
            for p in products:
                if p.size == size: yield p

        def filter_by_size_and_color(self, products, size, color):
            for p in products:
                if p.color == color and p.size == size:
                    yield p

        # state space explosion
        # 3 criteria
        # c s w cs sw cw csw = 7 methods

        # OCP = open for extension, closed for modification


    class Specification:
        def is_satisfied(self, item):
            pass

        # and operator makes life easier
        def __and__(self, other):
            return AndSpecification(self, other)


    class Filter:
        def filter(self, items, spec):
            pass


    class ColorSpecification(Specification):
        def __init__(self, color):
            self.color = color

        def is_satisfied(self, item):
            return item.color == self.color


    class SizeSpecification(Specification):
        def __init__(self, size):
            self.size = size

        def is_satisfied(self, item):
            return item.size == self.size


    # class AndSpecification(Specification):
    #     def __init__(self, spec1, spec2):
    #         self.spec2 = spec2
    #         self.spec1 = spec1
    #
    #     def is_satisfied(self, item):
    #         return self.spec1.is_satisfied(item) and \
    #                self.spec2.is_satisfied(item)

    class AndSpecification(Specification):
        def __init__(self, *args):
            self.args = args

        def is_satisfied(self, item):
            return all(map(
                lambda spec: spec.is_satisfied(item), self.args))


    class BetterFilter(Filter):
        def filter(self, items, spec):
            for item in items:
                if spec.is_satisfied(item):
                    yield item


    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    # ^ BEFORE

    # v AFTER
    bf = BetterFilter()

    print('Green products (new):')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')

    print('Large products:')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    print('Large blue items:')
    # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    large_blue = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')
#  COLOUR SIZE FOR PRODUCT FILTER

#Objects or entities should be open for extension but closed for modification.
#This means that a class should be extendable without modifying the class itself.

def Liskov_Substitution():
    class Rectangle:
        def __init__(self, width, height):
            self._height = height
            self._width = width

        @property
        def area(self):
            return self._width * self._height

        def __str__(self):
            return f'Width: {self.width}, height: {self.height}'

        @property
        def width(self):
            return self._width

        @width.setter
        def width(self, value):
            self._width = value

        @property
        def height(self):
            return self._height

        @height.setter
        def height(self, value):
            self._height = value


    class Square(Rectangle):
        def __init__(self, size):
            Rectangle.__init__(self, size, size)

        @Rectangle.width.setter
        def width(self, value):
            _width = _height = value

        @Rectangle.height.setter
        def height(self, value):
            _width = _height = value


    def use_it(rc):
        w = rc.width
        rc.height = 10  # unpleasant side effect
        expected = int(w * 10)
        print(f'Expected an area of {expected}, got {rc.area}')


    rc = Rectangle(2, 3)
    use_it(rc)

    sq = Square(5)
    use_it(sq)
#  RECTANGLE HEIGHT WIDTH

#Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.
#This means that every subclass or derived class should be substitutable for their base or parent class.


def interface_segregation():
    from abc import abstractmethod
    class Machine:
        def print(self, document):
            raise NotImplementedError()

        def fax(self, document):
            raise NotImplementedError()

        def scan(self, document):
            raise NotImplementedError()


    # ok if you need a multifunction device
    class MultiFunctionPrinter(Machine):
        def print(self, document):
            pass

        def fax(self, document):
            pass

        def scan(self, document):
            pass


    class OldFashionedPrinter(Machine):
        def print(self, document):
            # ok - print stuff
            pass

        def fax(self, document):
            pass  # do-nothing

        def scan(self, document):
            """Not supported!"""
            raise NotImplementedError('Printer cannot scan!')


    class Printer:
        @abstractmethod
        def print(self, document): pass


    class Scanner:
        @abstractmethod
        def scan(self, document): pass


    # same for Fax, etc.

    class MyPrinter(Printer):
        def print(self, document):
            print(document)


    class Photocopier(Printer, Scanner):
        def print(self, document):
            print(document)

        def scan(self, document):
            pass  # something meaningful


    class MultiFunctionDevice(Printer, Scanner):  # , Fax, etc
        @abstractmethod
        def print(self, document):
            pass

        @abstractmethod
        def scan(self, document):
            pass


    class MultiFunctionMachine(MultiFunctionDevice):
        def __init__(self, printer, scanner):
            self.printer = printer
            self.scanner = scanner

        def print(self, document):
            self.printer.print(document)

        def scan(self, document):
            self.scanner.scan(document)


    printer = OldFashionedPrinter()
    printer.fax(123)  # nothing happens
    printer.scan(123)  # oops!
#  PRINTER SCANNER FAX FOR MULTIPLE MACHINES

#A client should never be forced to implement an interface that it doesn’t use, or clients shouldn’t be forced to depend on methods they do not use.
#Still building from the previous ShapeInterface example, you will need to support the new three-dimensional shapes of Cuboid and Spheroid,
#  and these shapes will need to also calculate volume.


def dependency_inversion():
    from abc import abstractmethod
    from enum import Enum


    class Relationship(Enum):
        PARENT = 0
        CHILD = 1
        SIBLING = 2


    class Person:
        def __init__(self, name):
            self.name = name


    class RelationshipBrowser:
        @abstractmethod
        def find_all_children_of(self, name): pass


    class Relationships(RelationshipBrowser):  # low-level
        relations = []

        def add_parent_and_child(self, parent, child):
            self.relations.append((parent, Relationship.PARENT, child))
            self.relations.append((child, Relationship.PARENT, parent))
                
        def find_all_children_of(self, name):
            for r in self.relations:
                if r[0].name == name and r[1] == Relationship.PARENT:
                    yield r[2].name


    class Research:
        # dependency on a low-level module directly
        # bad because strongly dependent on e.g. storage type

        # def __init__(self, relationships):
        #     # high-level: find all of john's children
        #     relations = relationships.relations
        #     for r in relations:
        #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
        #             print(f'John has a child called {r[2].name}.')

        def __init__(self, browser):
            for p in browser.find_all_children_of("John"):
                print(f'John has a child called {p}')


    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    # low-level module
    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)
#   PARENT CHILD RELATIONSHIP MAPPING BOTH WAYS (PARENT, RELATIONSHIP, CHILD)

#Entities must depend on abstractions, not on concretions. 
#  It states that the high-level module must not depend on the low-level module, but they should depend on abstractions.
#This principle allows for decoupling.



''' Design Patterns'''

def abstract_class():
    from abc import ABC, abstractmethod

    class Animal(ABC):
        @abstractmethod
        def sound(self):
            """This method should be overridden in subclasses to define the animal's sound"""
            pass
        
        def move(self):
            """Concrete method that can be used directly or overridden in subclasses"""
            print("This animal moves")

    class Dog(Animal):
        def sound(self):
            print("Woof! Woof!")
        
        # Inherits and uses the move method from Animal

    class Cat(Animal):
        def sound(self):
            print("Meow! Meow!")
        
        # Overrides the move method
        def move(self):
            print("This cat prowls")

    # Example usage
    dog = Dog()
    dog.sound()  # Outputs: Woof! Woof!
    dog.move()   # Outputs: This animal moves

    cat = Cat()
    cat.sound()  # Outputs: Meow! Meow!
    cat.move()   # Outputs: This cat prowls

# Importing ABC and abstractmethod: 
#      The ABC class (Abstract Base Class) and abstractmethod decorator from the abc module are used to define abstract classes and methods.
# Defining the Abstract Class Animal:
#      Animal inherits from ABC, making it an abstract class.
#      The sound method is decorated with @abstractmethod, meaning any subclass must provide an implementation for this method.
#      The move method is a concrete method, which means it has an implementation and can be used directly or overridden in subclasses.
# Defining Subclasses Dog and Cat:
#      Both Dog and Cat inherit from Animal and provide their own implementation of the sound method.
#      Dog uses the inherited move method from Animal, while Cat overrides it with its own implementation.
# Polymorphism: You can call the sound and move methods on instances of Dog and Cat, demonstrating polymorphic behavior

def builder():
    class House:
        def __init__(self):
            self.walls = None
            self.roof = None
            self.doors = None

        def __str__(self):
            return f"House with {self.walls} walls, {self.roof} roof, and {self.doors} doors."

    class HouseBuilder:
        def __init__(self):
            self.house = House()

        def build_walls(self, walls):
            self.house.walls = walls
            return self

        def build_roof(self, roof):
            self.house.roof = roof
            return self

        def build_doors(self, doors):
            self.house.doors = doors
            return self

        def get_house(self):
            return self.house

    class Director:
        def __init__(self, builder):
            self.builder = builder

        def construct_basic_house(self):
            self.builder.build_walls(4).build_roof("flat").build_doors(1)
            return self.builder.get_house()

        def construct_luxury_house(self):
            self.builder.build_walls(10).build_roof("sloped").build_doors(5)
            return self.builder.get_house()

    # Usage
    builder = HouseBuilder()
    director = Director(builder)

    # Construct a basic house
    basic_house = director.construct_basic_house()
    print(basic_house)  # Outputs: House with 4 walls, flat roof, and 1 doors.

    # Construct a luxury house
    luxury_house = director.construct_luxury_house()
    print(luxury_house)  # Outputs: House with 10 walls, sloped roof, and 5 doors.

# Encapsulation of Construction Process: The builder pattern encapsulates the construction process and allows it to be reused for different types of products.
# The Builder pattern is a design pattern used to construct complex objects step by step. 
# It allows you to produce different types and representations of an object using the same construction code. 
# This pattern is especially useful when an object needs to be created with many possible configurations or when the construction process is complex.


def factory():
    from abc import ABC, abstractmethod

    # Product
    class Vehicle(ABC):
        @abstractmethod
        def drive(self):
            pass

    # Concrete Product
    class Car(Vehicle):
        def drive(self):
            return "Driving a car!"

    class Bike(Vehicle):
        def drive(self):
            return "Riding a bike!"

    # Creator
    class VehicleFactory(ABC):
        @abstractmethod
        def create_vehicle(self):
            pass

        def some_operation(self):
            # Call the factory method to create a Product object
            vehicle = self.create_vehicle()
            # Now use the product
            return f"VehicleFactory: The same creator's code has just worked with {vehicle.drive()}"

    # Concrete Creator
    class CarFactory(VehicleFactory):
        def create_vehicle(self):
            return Car()

    class BikeFactory(VehicleFactory):
        def create_vehicle(self):
            return Bike()

    # Usage
    def client_code(factory: VehicleFactory):
        print(factory.some_operation())

    print("App: Launched with the CarFactory.")
    client_code(CarFactory())

    print("\nApp: Launched with the BikeFactory.")
    client_code(BikeFactory())



'''Problems'''

def consecutive_numbers():
    def longest_consecutive(nums):
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in nums:
            # Check if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Count the length of the consecutive sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length

    # Example usage
    nums = [100, 4, 200, 1, 3, 2]
    print("Length of longest consecutive sequence:", longest_consecutive(nums))


def singly_linked_list():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def reverse_list(head):
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Temporarily store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev and current one step forward
            current = next_node
        
        return prev  # prev becomes the new head of the reversed list

    # Helper function to print the linked list
    def print_list(head):
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    # Example usage
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    print("Original list:")
    print_list(head)

    # Reversing the linked list
    reversed_head = reverse_list(head)

    print("Reversed list:")
    print_list(reversed_head)
    from collections import deque

    # Function to find the maximum element in each sliding window of size k


    def maxSlidingWindow(arr, k):
        ans = []
        deq = deque()

        # Initialize the deque with the first k elements
        for i in range(k):
            while deq and arr[i] >= arr[deq[-1]]:
                deq.pop()
            deq.append(i)

        # The maximum element in the first window
        ans.append(arr[deq[0]])

        # Process the remaining elements
        for i in range(k, len(arr)):
            # Remove elements that are out of the current window
            while deq and deq[0] <= i - k:
                deq.popleft()

            # Remove elements that are less than the current element
            while deq and arr[i] >= arr[deq[-1]]:
                deq.pop()

            deq.append(i)

            # The maximum element in the current window
            ans.append(arr[deq[0]])

        return ans


    # Main function
    if __name__ == "__main__":
        arr = [2, 3, 7, 9, 5, 1, 6, 4, 3]
        k = 3

        # Find the maximum element in each sliding window of size k
        result = maxSlidingWindow(arr, k)

        # Print the results
        print(result)




