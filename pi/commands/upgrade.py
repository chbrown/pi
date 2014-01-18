import os
import sys
from subprocess import check_call

import logging
logger = logging.getLogger(__name__)


def local_packages():
    for filepath in sys.path:
        # only do site-packages
        if 'site-packages' in filepath:
            yield os.path.basename(filepath).split('-')[0]


def upgrade(package, execute=True):
    args = ['easy_install', '--upgrade', package]
    logger.debug(' '.join(args))
    if execute:
        check_call(args)


def cli(parser):
    '''
    Simply calls out to easy_install --upgrade
    '''
    parser.add_argument('-n', '--dry-run', action='store_true', help='Print uninstall actions without running')
    opts = parser.parse_args()

    for package in local_packages():
        upgrade(package, execute=not opts.dry_run)
