""" Hi everone, welcome to VSCode
VSCode is a lightweight IDE where you can write code, run code, organize ur code
Let's learn how to run Python code in VSCode. 
BTW we assume you have followed the setup instructions and installed Python interpreter, VSCode, and Plug-in in VSCode
If not, let's do it now!
"""

"""VSCode provide interactive way to run Python code. We will go over 2 ways
First thing is definitely have a python file, so create a python file by file_name_you_luv.py
Have some code in file_name_you_luv.py you just created. 
In case u have no idea on what to write: `print("Hello World")` """

""" Method 1: use Run button
1. go into the file in VSCode
2. u can run python file by clicking the Run button on the top right of the window. it looks like ▷ 
    Now on the terminal, your program runs
3. pull out more options by clicking the pull-out button on the right of the run button.
4. click "Run Current File in Interactive Window"
5. now you should find another window appeared -- interactive window
    you can code and press 'Enter' in the prompt box in the interactive window
"""

"""Method 2: run code in a cell
1. write "# %%" in the file you create
    VSCode automatically know it's a Python cell
2. write code in the Python cell
3. click "Run Cell" on the block
    or "Shift + Enter" to run the cell
"""
# like this:
# %%


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
    def  __init__(self, name, age):
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

import pygame
import sys
pygame.init()
window = pygame.display.set_mode((100, 200))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False

pygame.quit()
# %%
