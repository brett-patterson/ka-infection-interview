from setuptools import setup, find_packages

setup(
    name='ka_infection',
    version='0.1',
    author='Brett Patterson',
    description='A solution to the Khan Academy Infection interview project',
    packages=find_packages(),
    install_requires=['graphviz']
)
