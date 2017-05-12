## Animal is_a object (yes , sort of confusing) look at the extra credit
class Animal(object):
    pass

## it_a object of the class Animal
class Dog(Animal):

    def __init__(self,name):
        ## define the object Dog appartien to the class Animal
        self.name = name

## is_a object of the class Animal
class Cat(Animal):

    def __init__(self, name):
        ##define the object Cat appartient to the class Animal
        self.name = name

## Person is a object
class Person(object):

    def __init__(self, name):
        ## person is_a object of the class Persons
        self.name = name

        ## Person has_a prt of some kind
        self.pet = None

##Employee has_a object of the class Person
class Employee(Person):

    def __init__(self, name, salary):
        ## has_a object of the class Employee=salary
        super(Employee, self). __init__(name)
        ##has_a object of the class Employee
        self.salary = salary

##IS-A class named Fish
class Fish(object):
    pass

## has_a object of the class Fish=Solmon
class Salmon(Fish):
    pass

## Has_a object of the class Fish = Halibut
class Halibut(Fish):
    pass


## rover is_a Dog
rover = Dog ("Rover")

## satan is_a Cat
satan = Cat("Satan")

## Mary is_a Person
mary = Person("Mary")

## mary has_a pet
mary.pet = satan

##Frank has-a employee whit a salary 120000
frank = Employee("Frank", 120000)

## Frank has_a pet
frank.pet = rover

##is_a a kind of Fhish
flipper = Fish()

## remplace salmon whit crouse
crouse = Salmon()

## remplace Halibut whit harry
harry= Halibut()
