#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Docstring: replace
"""
import os, os.path, sys
##### check for minimum python version and MYPYLIB
if sys.version_info < (3,6):
  print("python should be at least version 3.6") ; sys.exit(1)  
if 'PYDEVLIB' not in os.environ:
  print("you need to set os.environ['PYDEVLIB']") ; sys.exit(1)
else:
  libdir = os.environ['PYDEVLIB']
  if libdir not in sys.path: sys.path.insert(0, libdir )  
##### Set global vars needed for init
(prgdir,fname) = os.path.split(os.path.realpath(__file__))
(prgname,ext) = os.path.splitext(fname)

###########   M A I N   #######################################################
def main():
  """ Main part for doing the work
  """
  dbg.entersub()
  dbg.leavesub()

###########   D E F A U L T   I N I T   #######################################
if __name__ == "__main__":
  from mydebug.py3dbg import dbg
  from myconf.py3cfg import cfg
  exec(cfg.imports)
  exec(cfg.config)
  exec(cfg.usage)
  main()
