import os

from setuptools import setup

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'README')) as fp:
    long_description = fp.read()

setup(
    name='gibberish',
    description="A pseudo-word generator",
    version='0.3.1',
    author='Gregory Haskins',
    author_email='greg@greghaskins.com',
    maintainer='YPlan',
    maintainer_email='alex.damian@yplanapp.com',
    url='https://github.com/YPlan/gibberish',
    py_modules=('gibberish',),
    license='MIT License',
    long_description=long_description,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': 'gibberish = gibberish:console_main',
    }
)
