import os
from setuptools import setup, find_packages


def read(filepath):
    # don't die on files that may go missing due to zipping
    if os.path.exists(filepath):
        return open(filepath).read()
    return ''


setup(
    name='pi',
    version='0.1.2',
    description='Simpler python package installation',
    url='https://github.com/chbrown/pi',
    author='Christopher Brown',
    author_email='io@henrian.com',
    long_description=read('README.rst'),
    license=read('LICENSE'),
    packages=find_packages(),
    entry_points=dict(console_scripts=[
        'pi = pi.cli:main',
        'easy_uninstall = pi.commands.uninstall:easy_uninstall',
    ]),
    # https://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        # 'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Filesystems',
    ],
    tests_require=['nose'],
    test_suite='nose.collector',
)
