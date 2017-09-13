"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# from setuptools import setup, find_packages
from setuptools import find_packages
from cx_Freeze import setup, Executable
from codecs import open
from os import path
import sys


here = path.abspath(path.dirname(__file__))
parent_dir = path.abspath(path.join(here, 'src'))
sys.path.append(parent_dir)

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read().strip()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

build_exe_options = {
    # "icon": r"assets/favicon/favicon.ico",
    "includes": [
        "config",
        "sqlalchemy.sql.default_comparator",
        "faker.providers",
        "jinja2.ext",
    ],
    "include_files": [
        "static",
        "templates",
        "db",
        # "docx",
        "log",
        "upload",
    ],
    # "path": [
    #     path.dirname(__file__),
    # ],
}

base = None
setup(
    name='rpg-helper',
    version=version,
    keywords=[
        
        "flask",
        
        "flask"
    ],
    description="Description of rpg-helper",
    long_description=long_description,
    url='https://github.com/d2emon/rpg-helper#readme',
    executables = [Executable("manage.py", base=base, icon=r"assets/favicon/favicon.ico")],

    author='Dmitry Kutsenko',
    author_email='d2emonium@gmail.com',

    license='GPL-3.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GPL-3.0',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    package_dir={'': 'src'},
    packages=find_packages('./src', exclude=['tests']),
    py_modules=[
        "app",
        "config",
    ],
    install_requires=requirements,

    entry_points={
        'console_scripts': [
            'server=management:run',
        ],
    },

    options = {
        "build_exe": build_exe_options,
    },
)