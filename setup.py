from setuptools import setup

setup(
    name='restexec',
    version='0.01',
    author = 'REN yufu',
    url = 'https://github.com/renyufu/restexec',
    packages=['restexec'],
    entry_points={
        'console_scripts': [
            'restexec = restexec:main',
        ],
    },
    install_requires=[
        'Flask',
        'pyOpenSSL'
    ],
    license='GPLv3',
    description='RESTful executor'
)
