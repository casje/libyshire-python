"""Packaging logic for LibYshire"""
from setuptools import find_packages, setup

setup(
    name='libyshire',
    packages=find_packages(include=['src/libyshire']),
    version='0.0.1',
    description='Pacote de funcionalidades utéis para a construção de software',
    long_description='file: README.md',
    long_description_content_type='text/markdown',
    author='Claudio Alves Jr',
    maintainer='Claudio Alves Jr',
    url='https://github.com/casje/libyshire-python',
    license='Apache License',
    keywords=["calendário", "anbima", "calendar", "brazil", "brasil"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
    ],
    requires_python='>=3.9',
    install_requires=[
        'numpy'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)
