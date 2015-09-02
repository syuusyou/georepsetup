# -*- coding: utf-8 -*-
"""
    georepsetup.setup.py
    :copyright: (c) 2015 by Aravinda VK
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup


setup(
    name="Gluster Geo-replication Setup Helper",
    version="0.1",
    packages=["georepsetup"],
    include_package_data=True,
    install_requires=['argparse', 'paramiko'],
    entry_points={
        "console_scripts": [
            "georepsetup = georepsetup.cli:main",
        ]
    },
    platforms="linux",
    zip_safe=False,
    author="Aravinda VK",
    author_email="mail@aravindavk.in",
    description="CLI tool to handle Gluster Geo-replication setup",
    license="MIT",
    keywords="gluster, tool, geo-replication",
    url="https://github.com/aravindavk/georepsetup",
    long_description="""
    A CLI tool to simplify the difficulties in setting up Gluster
    Geo-replication
    """,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only"
    ],
)
