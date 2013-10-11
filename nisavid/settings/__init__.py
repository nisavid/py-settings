"""Application settings.

Some applications require certain settings to exist before they are
launched.  Some applications require the ability to save certain
settings so that they persist after termination.  It is desirable to
access both persistent and runtime settings via a uniform interface.
This package provides objects that satisfy these requirements.

Settings may be stored in a variety of ways.  Windows uses a system
registry.  OS X uses XML preferences files.  Many Unix applications use
INI-style configuration (:term:`!conf`) files.  It is desirable to store
some settings in a database.  For now, this module implements only the
conf file method, but it provides enough abstraction to allow for other
methods to be implemented as needed.


Scopes
------
Settings may be specified for the entire system or per user.  This scope
is called the :term:`!search scope`.

Settings are specific to organizations, applications, or subsystems,
which are collectively called :term:`!component scopes`.  Subsystems are
grouped by the applications to which they belong.  Applications are
grouped by the organizations that produce them.


Settings
--------
Each setting is a *(key, value)* pair.  A key is a non-empty string that
identifies the setting uniquely per application.  A value is any string
(or any object that can be represented as a string).

Keys are case-sensitive.


Groups
------
Keys can be grouped; for example, ``Book/Color`` and ``Book/PageCount``
are both part of the ``Book`` group, and some storage formats (such as
conf) may reflect this by writing ``Color`` and ``PageCount`` settings
under a ``Book`` section.  Groups can be nested.


Locations
---------
The primary location is the unique location determined by the
combination of format, base scope, organization, application, and
subsystem specified when creating a persistent settings object.

When settings are written, they are always written to the primary
location.

When a setting is queried, the primary location is searched first.  If
it is not found there, the fallback mechanism is triggered.  First,
greater component scopes are searched.  If the setting is not found
there and the base scope is ``user``, then the original component scope
is searched in the ``system`` base scope, followed by the greater
component scopes in ``system``.


Formats
-------
Settings formats specify where and how settings are stored.  Each format
defines the file path at which settings are stored for a given scope and
how to read and write settings in those files.

"""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__credits__ = ["Ivan D Vasin"]
__maintainer__ = "Ivan D Vasin"
__email__ = "nisavid@gmail.com"
__docformat__ = "restructuredtext"

from ._conf import *
from ._core import *
from ._exc import *
from ._inmemory import *
