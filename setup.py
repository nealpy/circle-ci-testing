from setuptools import *
#from distutils.core import *
NAME = 'mypackage'
about = {'__version__':1.0}
AUTHOR = 'Nilanjan Ray'
EMAIL = 'nilanjan.ray@cognizant.com'
DESCRIPTION = 'Package description'
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    #long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    #python_requires=REQUIRES_PYTHON,
    #url=URL,
    package_dir={'': 'mypackge'},
    packages=find_packages('mypackge'),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    #install_requires=REQUIRED,
    include_package_data=True,
)
