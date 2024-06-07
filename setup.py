from setuptools import find_packages,setup
from typing import List


def get_requirements()->list[str]:
    requirements_list = list[str] = []
    return requirements_list

setup(
    name='sensor',
    version='0.0.1',
    author='ritam rakshit',
    author_email='ritamrakshit33@gmail.com',
    install_requires=get_requirements,#["pymongo"]
    packages=find_packages()
)