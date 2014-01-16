## Python (package) installation

Getting started from [PyPI](https://pypi.python.org/pypi/pi/):

    easy_install pi

[Whence easy_install?](#setuptools)


## Commands

* Uninstall package named "pip":

        pi uninstall pip

* Install package named "filesequence":

        pi install filesequence

* List paths that Python searches for imported modules:

        pi paths

* List installed packages:

        pi list


## Testing

Continuous integration:

[![Travis CI Build Status](https://travis-ci.org/chbrown/pi.png?branch=master)](https://travis-ci.org/chbrown/pi)

Or run tests locally:

    nosetests --with-doctest


### Related

* http://guide.python-distribute.org/creation.html
* [distribute/pkg_resources docs](http://pythonhosted.org/distribute/pkg_resources.html)
* standard library [`site`](http://docs.python.org/2/library/site.html)
* standard library [environment variables](http://docs.python.org/2/using/cmdline.html#environment-variables)


### Setuptools

`pi` does not yet completely replace [setuptools](https://pypi.python.org/pypi/setuptools).
You may need to install it first:

| Distro | Package manager command             |
|:-------|:------------------------------------|
| Ubuntu | `apt-get install python-setuptools` |
| Mac    | built-in                            |
| Arch   | `pacman -S python-setuptools`       |
| CentOS | `yum install python-setuptools`     |


## License

Copyright (c) 2013 Christopher Brown. [MIT Licensed](https://raw.github.com/chbrown/pi/master/LICENSE).
