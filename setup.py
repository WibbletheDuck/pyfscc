import os
from distutils.core import setup

if os.name == 'nt':
    requirements = ['serial', 'win32']
    data_files=[('fscc', ['cfscc.dll'])]
else:
    requirements = ['serial']
    data_files=[('fscc', ['libcfscc.so'])]

setup(name='pyfscc',
      version='1.0.0',
      py_modules=['fscc'],
      data_files=data_files,
      requires=requirements,
      )