from setuptools import setup

setup(
    name='SigmaProject',
    version='0.1',
    author='Andreas P. Koenzen',
    author_email='akc@apkc.net',
    packages=['sigmaproject'],
    url='https://github.com/k-zen/SigmaProject',
    license='LICENSE.txt',
    description='Statistics library.',
    long_description=open('README.txt').read(),
    entry_points={'console_scripts': ['sigmaproject = sigmaproject.__main__:main']},
    install_requires=[
        "matplotlib",
        "numpy",
        "scipy",
        "seaborn"
    ]
)
