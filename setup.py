from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='stock_tracking_app',
    version='0.1.0',
    description='tracks stocks real time prices using pandas_datareader library.',
    long_description=readme,
    author='Manuel',
    author_email='manuel@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
