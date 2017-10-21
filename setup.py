#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

import notetags

setup(
    name=notetags.__name__,
    packages=['notetags'],
    version=notetags.__vers__,
    url='https://github.com/komish/notetags',
    description=notetags.__desc__,
    author='Jose R. Gonzalez',
    author_email='jose gonzalez eight nine at gmail dot com',
    license='MIT License',
    long_description='Tagging System for personal notes',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'nt=notetags.main:main',
        ],
    },
)
