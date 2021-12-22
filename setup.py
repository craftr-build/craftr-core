# This file was auto-generated by Shut. DO NOT EDIT
# For more information about Shut, check out https://pypi.org/project/shut/

from __future__ import print_function
import io
import os
import setuptools
import sys

readme_file = 'readme.md'
if os.path.isfile(readme_file):
  with io.open(readme_file, encoding='utf8') as fp:
    long_description = fp.read()
else:
  print("warning: file \"{}\" does not exist.".format(readme_file), file=sys.stderr)
  long_description = None

requirements = [
  'astor >=0.8.1,<1.0.0',
  'dataclasses >=0.6.0,<1.0.0',
  'nr.caching >=0.3.2,<1.0.0',
  'nr.functional >=0.1.0,<1.0.0',
  'nr.parsing.core >=2.0.2,<3.0.0',
  'nr.preconditions >=0.0.4,<1.0.0',
  'nr.pylang.ast >=0.0.5,<0.1.0',
  'termcolor >=1.1.0,<2.0.0',
  'typing-extensions >=3.10.0.0,<4.0.0',
  'nr.pylang.utils >=0.1.3,<1.0.0',
  'beartype >=0.9.1,<1.0.0',
]
test_requirements = [
  'types-termcolor',
]
extras_require = {}
extras_require['test'] = test_requirements

setuptools.setup(
  name = 'craftr-build',
  version = '5.0.0',
  author = 'Niklas Rosenstein',
  author_email = 'rosensteinniklas@gmail.com',
  description = 'General purpose build system with an easy to use API and DSL.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/craftr-build/craftr',
  license = 'MIT',
  packages = setuptools.find_packages('src', ['test', 'test.*', 'tests', 'tests.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = True,
  install_requires = requirements,
  extras_require = extras_require,
  tests_require = test_requirements,
  python_requires = '>=3.8.0,<4.0.0',
  data_files = [],
  entry_points = {
    'console_scripts': [
      'craftr = craftr.__main__:main',
    ]
  },
  cmdclass = {},
  keywords = [],
  classifiers = [],
  zip_safe = False,
)
