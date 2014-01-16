Python (package) installation
-----------------------------

Getting started from `PyPI <https://pypi.python.org/pypi/pi/>`__:

::

    easy_install pi

`Whence easy\_install? <#setuptools>`__

Commands
--------

-  Uninstall package named "pip":

   ::

       pi uninstall pip

-  Install package named "filesequence":

   ::

       pi install filesequence

-  List paths that Python searches for imported modules:

   ::

       pi paths

-  List installed packages:

   ::

       pi list

Testing
-------

Continuous integration:

|Travis CI Build Status|

Or run tests locally:

::

    nosetests --with-doctest

Related
~~~~~~~

-  http://guide.python-distribute.org/creation.html
-  `distribute/pkg\_resources
   docs <http://pythonhosted.org/distribute/pkg_resources.html>`__
-  standard library
   ```site`` <http://docs.python.org/2/library/site.html>`__
-  standard library `environment
   variables <http://docs.python.org/2/using/cmdline.html#environment-variables>`__

Setuptools
~~~~~~~~~~

``pi`` does not yet completely replace
`setuptools <https://pypi.python.org/pypi/setuptools>`__. You may need
to install it first:

+----------+-----------------------------------------+
| Distro   | Package manager command                 |
+==========+=========================================+
| Ubuntu   | ``apt-get install python-setuptools``   |
+----------+-----------------------------------------+
| Mac      | built-in                                |
+----------+-----------------------------------------+
| Arch     | ``pacman -S python-setuptools``         |
+----------+-----------------------------------------+
| CentOS   | ``yum install python-setuptools``       |
+----------+-----------------------------------------+

License
-------

Copyright (c) 2013 Christopher Brown. `MIT
Licensed <https://raw.github.com/chbrown/pi/master/LICENSE>`__.

.. |Travis CI Build Status| image:: https://travis-ci.org/chbrown/pi.png?branch=master
   :target: https://travis-ci.org/chbrown/pi
