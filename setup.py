#!/usr/bin/env python3

from setuptools import setup


setup(
    name = 'plover_osnos',
    version = '0.0.1',
    description = 'Template system for Plover',
    author = 'Noelia Ruiz',
    author_email = 'nrm1977@gmail.com',
    license =  'GNU General Public License v2 or later (GPLv2+)',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires = [
        'plover>=4.0.0.dev0',
        'plover-python-dictionary>=0.5.9',
    ],
    packages = [
        'plover_osnos',
    ],
    entry_points = '''

    [plover.system]
    Osnos = plover_osnos.system

    ''',
    include_package_data = True,
    zip_safe = True,
)
