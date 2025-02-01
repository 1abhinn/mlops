from setuptools import find_packages,setup
from typing import List

def get_reqs(file_path:str)->List[str]:
    '''
    Returns list of requirements
    '''
    reqs = []
    with open(file_path) as file_obj:
        reqs = file_obj.readlines()
        reqs = [x.replace("\n",'') for x in reqs]
        if '-e .' in reqs:
            reqs.remove('-e .')
    return reqs

setup(
    name ='mlproject',
    version = '0.0.0',
    author = 'Abhinn',
    author_email = 'abhinn33@gmail.com',
    packages = find_packages(),
    install_requires =get_reqs('requirements.txt')
)