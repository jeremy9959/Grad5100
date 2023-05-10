# %% [markdown]
# # Jupyter Lab Project Walkthrough
#
# 1. Use the 'text editor' feature in Jupyter Lab to create your README.md file.
# 2. **RENAME YOUR NOTEBOOK FILE IMMEDIATELY** to something relevant
# 3. CTRL-ENTER executes a cell.

# %% [markdown]
# ## Markdown cells
#
# This is a markdown cell:
#
# - Headings are \#, \#\#, etc.
# - Bold is marked \*\*make me bold\*\* like **this**.
# - Italics are marked \*make me italic\* like *this*.
# - Math can be typeset with \LaTeX if you know it:  $$f(x)=e^{-x}\cos(x)$$
# - Bulleted lists are marked with \-.
#

# %%
# code cells
## Code cells contain python code that gets executed.
# indicates a comment that is ignored.
print("Hello World!")

# %% [markdown]
# In this walkthrough we will look at the following elements of Python in a jupyter notebook.
#
# The print statement
#

# %%
print("hello world!")


# %% [markdown]
#
# Variables, variable names, and assignment/datatypes

# %%
count = 5  # an integer
name = "Jeremy Teitelbaum"  # a string
paragraph = """This is how you enter a multiline string
in python. It is enclosed in triple quotes."""
pi = 3.14159  # a float
epsilon = 1.0e-6  # a float
students = ["Jeremy", "Phillip", "Sara", "Molly"]  # a list
HotDog = True


# %%
print(students)

# %% [markdown]
# Compare `print` for multiline strings with the string value. (\\n means newline)
#
#

# %%
print(paragraph)

# %%
paragraph

# %% [markdown]
# Arithmetic operations
#

# %%
print(count)
count = count + 1
print(count)

# %%
1 / pi

# %%
print(2**3)  # exponent
print(1 / 2)  # division (converts integer to float)
print(1 / (1 / 2))  # 2 becomes 2.0

# %%
quotient = 5 // 3  # integer division
remainder = 5 % 3  # remainder
print(quotient, remainder)

# %% [markdown]
#
# Operations on strings and lists
#

# %%
"Jeremy" + " Teitelbaum"

# %%
["a", "b", "c"] + ["d"]

# %%
len("Jeremy")

# %%
len(["Jeremy", "Teitelbaum"])

# %%
firstName = "Jeremy"
lastName = "Teitelbaum"
fullName = firstName + " " + lastName


# %% [markdown]
# Some fancier printing

# %%
print(f"The first name is {firstName}")
print(f"The last name is {lastName}")
print(f"The full name is {firstName} {lastName}")
print(firstName, lastName, sep=",")
print(firstName, lastName, sep=":")

# %% [markdown]
# Slicing
#
# In python, we **always count from zero**!!!

# %%
firstName[0]

# %%
lastName[1]

# %%
# [a:b] means from a to b-1 inclusive

print(firstName[0:3])
print(firstName[3:])
print(firstName[3:5])


# %%
# negative indices count from the end
print(firstName[-1])  # the last element
print(firstName[-3:-1])  # elements -3 and -2, but not -1

# %%
# [a:b:c] means from a to b-1 in steps of c
# missing numbers mean (beginnging):(end)
print(firstName[:5:2])
print(firstName[::2])
print(firstName[::-1])  # reverse the string
print(firstName[3::-1])  # 3,2,1,0
print(firstName[3:0:-1])  # 3,2,1

# %% [markdown]
# Slices work the same on list elements

# %%
print(students[0])
print(students[-1])
every_other_student = students[::2]
print(every_other_student)


# %% [markdown]
# Libraries
#

# %%
import math

# %%
math.log(23)

# %%
math.pi

# %%
math.cos(math.pi / 2)  # should be zero

# %%
math.cos(math.pi / 2) == 0

# %%
abs(math.cos(math.pi / 2)) < 1e-6

# %%
math.pi == pi

# %%
import numpy as np

# %%
np.pia

# %%
print(np.random.randint(0, 10))

# %%
print(np.__version__)

# %%
from numpy.random import randint

# %%
randint(1, 10)

# %%
