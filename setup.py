#!/usr/bin/env python

from distutils.core import setup

readme = open("README.md", "r")

setup(name='pyroute2',
      version='0.3.3',
      description='Python Netlink library',
      author='Peter V. Saveliev',
      author_email='peter@svinota.eu',
      url='https://github.com/svinota/pyroute2',
      license='GPLv2+',
      packages=['pyroute2',
                'pyroute2.ipdb',
                'pyroute2.netlink',
                'pyroute2.netlink.generic',
                'pyroute2.netlink.ipq',
                'pyroute2.netlink.nfnetlink',
                'pyroute2.netlink.rtnl',
                'pyroute2.netlink.taskstats'],
      classifiers=['License :: OSI Approved :: GNU General Public ' +
                   'License v2 or later (GPLv2+)',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: ' +
                   'Python Modules',
                   'Operating System :: POSIX',
                   'Intended Audience :: Developers',
                   'Development Status :: 4 - Beta'],
      long_description=readme.read())
