import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

if __name__ == "__main__":
  
   install_requires = [
       'numpy',
       'sympy',
       'scipy',
       'matplotlib'
       ]
   setup(
       name = "pysde",
       version = "1.0.5",
       author = "chu-ching huang, Lars Ericson",
       author_email = "cchuang2009@gmail.com, erxnmedia@hotmail.com",
       description = ("Python Solver via Sympy + SciPy/NumPy for Stochastic Differential Equations!"),
       license = "BSD",
       keywords = "Stochastic differential equations",
       url = "https://github.com/cchuang2009/PySDE",
       packages=['pysde'],
       long_description=read('README.md'),
       classifiers=[
        "Development Status :: 3 - beta",
        "Topic :: Math, Computer",
        "License :: OSI Approved :: BSD License",
       ],
    )

