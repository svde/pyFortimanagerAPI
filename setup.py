from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyFortiManagerAPI',
    description='A Python wrapper for the FortiManager REST API',
    version='0.2.3',
    py_modules=["pyFortiManagerAPI"],
    package_dir={'': 'src'},
    keywords=['FortiManager', 'RestAPI', 'API', 'FortiGate', 'Fortinet', "python", "FortiManager API",
              "FortiManager API Python", "Python examples"],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests', 'urllib3'],
    url="https://github.com/akshaymane920/pyFortiManagerAPI",
    author="Akshay Mane",
    author_email="akshaymane920@gmail.com",
)
