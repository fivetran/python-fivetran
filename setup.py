import setuptools
import sys
sys.path.insert(1, 'fivetran/')
print(sys.path)
import __init__

version = __init__.__version__

with open("README.md", "r", encoding="utf-8") as rm:
  long_description = rm.read()

setuptools.setup(
  name='python-fivetran',
  version='1.0.0',
  description='Python SDK for the Fivetran REST API',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Connor Brereton, Angel Hernandez',
  url='https://github.com/fivetran-connorbrereton/python-fivetran',
  author_email='connor.brereton@fivetran.com, angel.hernandez@fivetran.com',
  license='MIT',
  packages=setuptools.find_packages(),
  zip_safe=False,
  install_requires=['requests'],
  keywords=['fivetran', 'REST API', 'sdk'],
  classifiers= [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ]
)