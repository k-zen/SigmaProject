from setuptools import setup

setup(
    name='SigmaProject',
    version='0.1',
    author='Andreas Koenzen',
    author_email='akoenzen | uvic.ca',
    packages=['sigmaproject'],
    url='https://github.com/k-zen/SigmaProject',
    license='LICENSE.txt',
    description='Statistics library.',
    long_description=open('README.txt').read(),
    entry_points={'console_scripts': ['sigmaproject = sigmaproject.__main__:main']},
    install_requires=[
        'absl-py',
        'astor',
        'certifi',
        'chardet',
        'cycler',
        'gast',
        'grpcio',
        'idna',
        'kiwisolver',
        'Markdown',
        'matplotlib',
        'numpy',
        'paho-mqtt',
        'pandas',
        'protobuf',
        'pyparsing',
        'python-dateutil',
        'pytz',
        'requests',
        'scipy',
        'seaborn',
        'six',
        'tensorboard',
        'tensorflow',
        'termcolor',
        'urllib3',
        'Werkzeug'
    ]
)
