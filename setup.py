import os

from setuptools import setup

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'README.rst')) as fp:
    long_description = fp.read()

setup(
    name='gibberish',
    description="A pseudo-word generator",
    version='0.4.0',
    author='Gregory Haskins',
    author_email='greg@greghaskins.com',
    url='https://github.com/greghaskins/gibberish',
    packages=('gibberish',),
    license='MIT License',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    install_requires=['PyYAML'],
    package_data={
        'gibberish': ['database/*'],
    },
    extras_require={
        'dev': ['nltk']
    },
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
