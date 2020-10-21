#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Program to create a new python prog at same directory level as pylibap
    Creates the needed usage, import and config files and also   
"""
import os, os.path, sys
##### check for minimum python version and PYDEVLIB
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
###########   M A I N   ######################################################
def main():
  """ Main wrapper part for module calls
  """
  dbg.entersub()
  newpath = os.path.realpath(os.path.join(libdir,'..',prgargs.name))
  dbg.dprint(0,newpath)
  sys.exit(0)
  #try:
  #  os.makedirs(newpath)
  #except Exception as e:
  #  dbg.exitf(e) 
  templdir = os.path.join(libdir,'template')
  for top, dirs, files in os.walk(templdir):
    for f in files:
      if f.endswith('.py'):
        if f.startswith('main'):
          newf = f.replace('main',prgargs.name)
          shutil.copy2(os.path.join(templdir,f), os.path.join(newpath,newf))
          print(newf)
        else: 
          shutil.copy2(os.path.join(templdir,f), os.path.join(newpath,f)) 
          print(f)
  dbg.leavesub()

###########   D E F A U L T   I N I T   #######################################
if __name__ == "__main__":
  from mydebug.py3dbg import dbg
  from myconf.py3cfg import cfg
  exec(cfg.imports)
  exec(cfg.config)
  exec(cfg.usage)
  main()
