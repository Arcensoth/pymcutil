import argparse
import logging
import unittest

import pymcutil.logging

parser = argparse.ArgumentParser(description='Run pymcutil tests.')
parser.add_argument('--verbosity', default=0, type=int, help='test runner verbosity')
parser.add_argument('--log', default='WARNING', help='log level')

args = parser.parse_args()

verbosity = args.verbosity
log_level = args.log

pymcutil.logging.install(log_level)

log = logging.getLogger(__name__)

unittest.TextTestRunner(verbosity=verbosity).run(unittest.TestLoader().discover('.'))
