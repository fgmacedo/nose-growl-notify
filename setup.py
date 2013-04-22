#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='NoseGrowlNotify',
    author='Fernando Macedo',
    author_email='fgmacedo@gmail.com',
    description='Nose plugin for Growl notifications',
    long_description=long_description,
    license='Creative Commons Attribution license (CC BY)',
    install_requires=['nose>=0.10', 'gntp'],
    url="http://github.org/fgmacedo/nose-growl-notify",
    version='0.1',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={
        'NoseGrowlNotify': ['nosegrowlnotify/*.png'],
    },
    entry_points={
        'nose.plugins.0.10': [
            'nosegrowlnotify = nosegrowlnotify:NoseGrowlNotify']
    }
)
