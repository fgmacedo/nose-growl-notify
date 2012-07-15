#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='NoseGrowlNotify',
    author='Fernando Macedo',
    author_email='fgmacedo@gmail.com',
    description='nose plugin for Growl notifications',
    install_requires=['nose>=0.10', 'gntp'],
    url="http://github.org/fgmacedo/nose-growl-notify",
    version='0.1',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={
        '': ['*.png'],
    },
    entry_points={
        'nose.plugins.0.10': [
            'nosegrowl = nosegrowl:NoseGrowlNotify']
    }
)
