"""Setup the project."""
from setuptools import setup, find_packages


setup(
    name='Finnr',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy>=1.11.1', 'opencv-python>=3.4.1.15', 'imutils>=0.4.6'],
    tests_require=['coverage>=4.4.2', 'coveralls'],
    author='Mario Nitchev',
    author_email='mail@mail.com',
    description='A wandering robot looking for his friend - a tennis ball.',
    license='MIT',
    keywords='simulation, raspberry pi, image recognision, opencv, robotics',
    url='https://github.com/mnitchev/Finnr',
    test_suite='tests'
)
