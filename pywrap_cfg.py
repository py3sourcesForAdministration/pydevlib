#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" --- This is only the configuration file ---"""
import os,sys
if sys.argv[0].find('pydoc') > 0 :
  print(__doc__); sys.exit(0)

from datetime import date
data = {
  'today' : date.today().strftime("%Y-%m-%d"),
  'pythons' : [ 
    os.path.realpath(sys.executable),
    '/usr/bin/python3.6',
    '/usr/bin/python3.8','/usr/bin/python3.9' 
  ], 
}
argdefaults = { 
  'debug' : 3 
} 
