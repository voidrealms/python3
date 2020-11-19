# needed be cause we are in a sub folder
"""
The __init__.py files are required to make 
Python treat directories containing the file as packages. 
This prevents directories with a common name, such as string, 
unintentionally hiding valid modules that occur later on the module search path. 
In the simplest case, __init__.py can just be an empty file, 
but it can also execute initialization code for the package.
"""
from .test import *

# . current
# .. parent