import os
from collections import namedtuple
import shutil

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name='Sam')

os.getcwd()  # pwd
os.listdir()  # ls

shutil.move('test.txt', 'C:\\Users\\User')