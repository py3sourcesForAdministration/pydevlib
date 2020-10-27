#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Docstring: replace
"""
import os, os.path, sys, checkenv
libdir         = checkenv.chk_sufficient()
prgname,prgdir = checkenv.get_names(__file__)

###########   M A I N   #######################################################
def main():
  """ Main part for doing the work
  """
  dbg.entersub()
  dbg.leavesub()

###########   D E F A U L T   I N I T   #######################################
if __name__ == "__main__":
  from mydebug.py3dbg import dbg
  from myconf.py3cfg  import init_cfg
  cfg = init_cfg(prgname,prgdir,libdir,dbg)
  exec(cfg.imports)
  exec(cfg.usage)
  main()
