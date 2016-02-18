# -*- coding: utf-8 -*-
from codecs import open as codecs_open
from setuptools import setup, find_packages


src_dir = 'src'

with codecs_open('README.rst', encoding='utf-8') as file:
    long_description = file.read()

with codecs_open('{0}/frogsay/version.py'.format(src_dir), encoding='utf-8') as file:
    exec(file.read())

requirements = [
    'click',
    'python-RIBBIT',
]

setup(name='frogsay',
      version=__version__,
      description='An ASCII FROG reads you a tip',
      long_description=long_description,
      classifiers=[],
      keywords='FROG CROAK',
      author='Charlie Liban',
      author_email='charlie@clib.ca',
      url='https://github.com/clibc/frogsay',
      license='MIT',
      packages=find_packages(src_dir, exclude=['tests', 'examples']),
      package_dir={'': src_dir},
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
      entry_points={
        'console_scripts': [
            'frogsay=frogsay:cli'
        ]
      })
