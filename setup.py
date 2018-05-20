import os
try:
    # use setuptools if available
    from setuptools import setup
    kwargs = {
        'entry_points': {'console_scripts':
            'gibberish = gibberish:console_main',
        }
    }
except ImportError:
    # fall back to distutils
    from distutils import setup
    kwargs = {}


base_dir = os.path.dirname(os.path.abspath(__file__))

setup(
    name='Gibberish',
    description="A pseudo-word generator",
    version='0.3',
    author='Gregory Haskins',
    author_email='greg@greghaskins.com',
    url='https://github.com/greghaskins/gibberish',
    packages=('gibberish',),
    license='MIT License',
    long_description=open(os.path.join(base_dir, 'README.rst')).read(),
    install_requires=['PyYAML'],
    package_data={
        'gibberish': ['database/*'],
    },
    # include_package_data=True,
    extras_require={
        'dev': ['nltk']
                   },
    **kwargs
)
