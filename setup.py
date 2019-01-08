from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import ultra

setup(
    name = "ultra",
    version = ultra.__version__,
    url = 'https://github.com/ocakgun/u96base',
    license = 'All rights reserved.',
    author = "Omer Can Akgun",
    author_email = "oca@ocakgun.com",
    packages = ['ultra'],
    package_data = {
    '' : ['*.bit','*.tcl','*.py','*.so', '*.hwh'],
    },
    install_requires=[
        'pynq',
    ],
    dependency_links=['http://github.com/xilinx/PYNQ'],
    description = "Base overlay for ultra96"
)
