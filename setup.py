from distutils.core import setup

setup(
    name='lsdo_atmos',
    version='0',
    packages=[
        'lsdo_atmos',
    ],
    install_requires=[
        'openmdao',
        'csdl',
        'csdl_om',
    ],
)