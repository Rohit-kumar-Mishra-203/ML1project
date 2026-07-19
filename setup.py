from setuptools import setup, find_packages
from typing import List

E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        
        if E_DOT in requirements:
            requirements.remove(E_DOT)
        
        
        return  requirements
    




setup(
    name='ML1project',
    version='0.0.1',
    author='rohit mishra',
    author_email='mishrarohitkumar2003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')   
)