
"""After learning the concept of classes. Let's make a class yourself
In the code below, we want to:
    - create a class Person that takes 2 arguments
        - with attribute: name, age
        - with method: jump
    - create an object of class Person
"""
# %%
class Person:
    def  __init__(self):
        print("a person created")
    
    def jump(self):
        print("jumped")

olivia = Person()
olivia.name = "Olivia"
olivia.age = 10

jenny = Person()
jenny.name = "Jenny Z"
jenny.age = 20

print(olivia.name)


# %%
class Person:
    def  __init__(self, name, age = 0): # HINT: what arguments are mandatory to create an instance of Person?
        self.age = age
        self.name = name
    
    def jump(self):
        # TODO: give an object, print their name + jumped
        """
        >>> olivia.jump()
        "Olivia Y jumped"
        """
        print(f"{self.name} jumped")

olivia.dog = "Ice cream" # define an attribute only this object has
p1 = Person # define a class not an object

# %%
