# coding: utf-8 -*-
#
# Setup file for geocluster
#

import os

from setuptools import setup, find_packages

# Get the description file
here = os.path.dirname(os.path.abspath(__file__))
long_description = open(os.path.join(here, "DESCRIPTION.rst"), 'r').read()

setup(
    name='geocluster',
    author=u'Régis FLORET',
    author_email='regis@regisblog.fr',
    version='1.0.1',
    url='http://www.regisblog.fr/geocluster/',
    download_url='https://github.com/regisf/geocluster',
    platforms=['any', ],
    description='GeoCluster is a framework agnostic library to help map clusterization',
    long_description=long_description,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization'
    ],
    keywords='Geocoding map cluster',
    packages=find_packages('.', exclude=['CModule', 'tests'])
)
