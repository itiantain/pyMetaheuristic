from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name='pyMetaheuristic',
    version='1.1.0',
    license='GNU',
    author='Valdecy Pereira',
    author_email='valdecy.pereira@gmail.com',
    url='https://github.com/Valdecy/pyMetaheuristic',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
