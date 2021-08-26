from setuptools import setup, find_packages
import os


def get_version_from_file(filepath):
    with open(filepath) as version_file:
        return version_file.read().strip()


def take_package_name(name):
    if name.startswith("-e"):
        egg_name = '_'.join(name.split('#egg=')[1:])
        url = name.split('#egg=')[0].split(' ')[1]

        version_split = egg_name.split('-')
        if len(version_split) == 1:
            pkg_name = egg_name.replace('\n', '')
        else:
            pkg_name = '_'.join(version_split[:len(version_split) - 1])

        return pkg_name + " @ " + url
    else:
        return name.strip()


def load_requires_from_file(filepath):
    with open(filepath) as fp:
        return [take_package_name(pkg_name) for pkg_name in fp.readlines()]


setup(
    name='sample_module',
    version="0.0.0.1",
    install_requires=load_requires_from_file("requirements.txt"),
    description="sample_module",
    long_description="hogehoge",
    author='Ryo Kabutan',
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    license='',
    classifiers=[
        "Development Status :: 1 - Planning"
    ]
)
