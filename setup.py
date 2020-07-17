import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name= "southpy",
    version= "v0.1.0",
    description= "Python Wrapper for Southpine's Player API",
    license= "BSD-3-License",
    long_description= README,
    long_description_content_type= "text/markdown",
    author= "doamatto",
    maintainer= "doamatto",
    maintainer_email= "hello@doamatto.xyz",
    package_data= { "southpy": ["py.typed"] },
    packages= { "southpy" },
    url= "https://github.com/doamatto/southpy",
    install_requires=["requests", "aiohttp"],
    keywords= ["api", "southpine", "southpy"],
    classifiers= [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved",
    ],
    zip_safe= False,
    python_requires=">= 3.6",
    project_urls={
        "Bug Reports": "https://github.com/doamatto/southpy/issues",
        "Source": "https://github.com/doamatto/southpy"
    }
)