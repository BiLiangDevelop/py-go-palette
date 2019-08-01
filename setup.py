# -*- coding: utf-8 -*-
from setuptools import setup

# version info
NAME = "pypalette"
VERSION = "0.1.5"
DESC = "Extract prominent colors from images! Python wrapper for `https://github.com/dayvonjersen/vibrant`."

# requirements
install_requires = []
with open('requirements.txt', "r") as fp:
    for line in fp:
        if len(line.strip()) > 2:
            install_requires.append(line.strip())

# setup config
setup(
    name=NAME,
    version=VERSION,
    description=DESC,
    long_description=DESC,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    install_requires=install_requires,
    author="BiLiangDevelop && frkhit",
    url="https://github.com/BiLiangDevelop/py-go-palette",
    author_email="frkhit@gmail.com",
    license="MIT",
    packages=["pypalette", ],
    package_data={
        "": ["LICENSE", "README.md", "MANIFEST.in"],
        "pypalette": ["go-palette-*.so", ]
    },
    include_package_data=True,
)
