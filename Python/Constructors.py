class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move ( self ):
        print("Move")
    
    def draw ( self ):
        print("Draw")

point = Point(10, 20)
print(point.x)
print(point.y)
point.y = 30
print(point.y)


# exasice :
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        print(f"My name is {self.name}.")

    def talk(self):
        print(f"{self.name},I am talking.")
    def age(self):
        print(f"My age is {self.age}.")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
person = Person(name, age)
person.talk()