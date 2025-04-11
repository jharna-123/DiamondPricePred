from setuptools import find_packages, setup
from typing import List
Hyphen_e_dot = '-e .'

def get_requiremets(file_path:str)->List[str]:
    requirements =[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("/n", " ") for req in requirements]
        
        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)
        return requirements





setup(
    name = "DiamondPricePRed",
    version="0.0.1",
    author_email="jharnayadav009@gmail.com",
    author="JharnaYadav",
    install_requires=get_requiremets("requirements.txt"),
    packages= find_packages(),
)