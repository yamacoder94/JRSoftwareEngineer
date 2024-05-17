class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Getter methods
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

# Creating an instance of Person
p1 = Person("Bob", 22)

# Calling the getter methods with parentheses
print(p1.getAge())  # Corrected: Call the method with ()
print(p1.getName())  # Corrected: Call the method with ()