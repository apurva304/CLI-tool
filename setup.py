from setuptools import setup

setup(
    name='mytool',
    version='1.0',
    py_modules=['toolmain'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        mytool=toolmain:cli
    ''',
)