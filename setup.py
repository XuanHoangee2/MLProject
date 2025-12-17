from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirement(file_path:str)->List[str]:
    """
    This function will return list of requirements
    """
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name= 'mlproject',
    version='0.0.1',
    author='Hoangee2',
    author_email='tranxuanhoang14062004@gmail.com',
    packages= find_packages(),
    install_requires = get_requirement('requirements.txt'),
)