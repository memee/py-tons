import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='py-tons',
    version='0.1',
    packages=['pytons'],
    include_package_data=True,
    license='MIT License',
    description='Tons of Py: utils library for Python.',
    long_description=README,
    url='https://github.com/memee/py-tons',
    author='Maciej Maciaszek',
    author_email='maciej.maciaszek@gmail.com',
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python:: 2.6',
        'Programming Language :: Python:: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
    requires=['six'],
    tests_require=['pytest'],
)
