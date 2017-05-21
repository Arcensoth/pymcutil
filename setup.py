from setuptools import setup, find_packages

with open('VERSION.txt') as fp:
    version = fp.read().strip()

with open('README.md') as fp:
    readme = fp.read()

with open('requirements.txt') as fp:
    requirements = fp.read().splitlines()

setup(
    name='pymcutil',
    version=version,
    author='Arcensoth',
    author_email='arcensoth@gmail.com',
    url='https://github.com/Arcensoth/pymcutil',
    license='MIT',
    description='An expressive Minecraft utility library revolving around data manipulation and generation.',
    long_description=readme,
    packages=find_packages(),
    install_requires=requirements)
