from setuptools import setup, find_packages

with open('requirements.txt', 'r') as requirements_file:
    requirements = requirements_file.read().split()

setup(
    name='recommender_system_project',
    version='0.1.0',
    description='Template for the recommender system assignment',
    author='Alaa Bakhti',
    author_email='alaa.bakhti@epita.fr',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
    
)

