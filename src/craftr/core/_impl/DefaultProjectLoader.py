
"""
Implements the default project loader which loads `build.craftr.py` files and executes them as a
plain Python script providing the current #Project in the global scope.
"""

import typing as t
from pathlib import Path

from .._project import Project, ProjectLoader, UnableToLoadProjectError

if t.TYPE_CHECKING:
  from .._context import Context

BUILD_SCRIPT_FILENAME = Path('build.craftr.py')


class DefaultProjectLoader(ProjectLoader):

  def __repr__(self) -> str:
    return f'{type(self).__name__}()'

  def load_project(self, context: 'Context', parent: t.Optional[Project], path: Path) -> Project:
    print(path, path /BUILD_SCRIPT_FILENAME)
    if (filename := path / BUILD_SCRIPT_FILENAME).exists():
      project = Project(context, parent, path)
      context.init_project(project)
      scope = {'project': project, '__file__': str(filename), '__name__': '__main__'}
      exec(compile(filename.read_text(), str(filename), 'exec'), scope, scope)
      return project
    raise UnableToLoadProjectError(self, context, parent, path)
