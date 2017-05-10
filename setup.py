# -*- coding: utf-8 -*-
#
# This file is part of sos-remote-ikernel.
# Copyright (C) 2017 Swiss Data Science Center.
#
# sos-remote-ikernel is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# sos-remote-ikernel is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with sos-remote-ikernel; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.

"""SOS Remote IKernel."""

import os

from setuptools import find_packages, setup

readme = ''  # open('README.rst').read()
history = ''  # open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.2.2',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.6.2',
]

install_requires = [
    'sos>=0.9.6.1',
]

packages = find_packages()


# Get the version string. Cannot be done with import!
# g = {}
# with open(os.path.join('ipython_cell_runner', 'version.py'), 'rt') as fp:
#     exec(fp.read(), g)
#     version = g['__version__']
version = '0.0.1'

setup(
    name='sos-remote-ikernel',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='ipython jupyter notebook kernel sos',
    license='GPLv2',
    author='Swiss Data Science Center',
    author_email='info@datascience.ch',
    url='https://github.com/SwissDataScienceCenter/sos-remote-ikernel',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'sos_languages': [
            'python_slurm = sos_remote_ikernel:sos_PythonSlurm',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 1 - Planning',
    ],
)
