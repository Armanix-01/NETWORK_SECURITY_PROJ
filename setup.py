from setuptools import setup, find_packages
import os
import sys
from typing import List

hyphen_dot_e = "-e ."
def get_req(file_path:str)->List[str]:
    requirements = []



    try:
        with open(file_path) as obj:
            requirements = obj.readlines()
            requirements = [each.strip() for each in requirements if each.strip()]
            if hyphen_dot_e in requirements:
                requirements.remove(hyphen_dot_e)

        return requirements
    except FileNotFoundError:
        print("requirements.txt file not found")


setup(
    name= "NETWORK_SECURITY_PROJ", 
    ##✅ YES — in setup.py, the name is the package name by which 
    # your project is installed and referred to on another machine.
    # ❌ It is NOT necessarily the same as your Python
    # module/folder name
    version= "1.0",
    author= "Arman Singh",
    author_email= "armanixofficial01@gmail.com",
    packages= find_packages(),
    install_requires = get_req(os.path.join(os.path.dirname(__file__), "requirements.txt"))

)

##The special variable __file__ in Python contains the 
# path of the current script or module file from which it
# is accessed


