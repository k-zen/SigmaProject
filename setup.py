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
        "wradlib >= 0.9",
        "haversine >= 0.4.5",
        "numpy >= 1.6.1",
        "matplotlib	>= 1.1.0",
        "scipy >= 0.9",
        "h5py >= 2.0.1",
        "netCDF4 >= 1.0",
        "gdal >= 1.9",
        "watchdog >= 0.8.3",
        "requests >= 2.13.0",
        "geopy",
        "scikit-learn",
        "shapely",
        "pandas"
    ]
)
