##find packages will find __init__ files and consider the folder as packages
from setuptools import setup, find_packages


#we are giving source file
setup(
    name="src", 
    version="0.0.1",
    description="its a wineq q package",
    author="sid",
    packages = find_packages(),
    license="MIT",

)
#find_packages() will find