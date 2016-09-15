import os

from setuptools import setup

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'README.rst')) as fp:
    long_description = fp.read()

setup(
    name='Gibberish',
    description="A pseudo-word generator",
    version='0.2',
    author='Gregory Haskins',
    author_email='greg@greghaskins.com',
    url='https://github.com/greghaskins/gibberish',
    py_modules=('gibberish',),
    license='MIT License',
    long_description=long_description,
    entry_points={
        'console_scripts': 'gibberish = gibberish:console_main',
    }
)
