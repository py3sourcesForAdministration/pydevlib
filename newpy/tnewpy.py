#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Program to create a new python prog at same directory level as pylibap
    Creates the needed usage, import and config files and also   
"""
import os, os.path, sys,checkenv
###### check for minimum python version and PYDEVLIB
#if sys.version_info < (3,6):
#  print("python should be at least version 3.6") ; sys.exit(1)  
#if 'PYDEVLIB' not in os.environ:
#  print("you need to set os.environ['PYDEVLIB']") ; sys.exit(1)
#else:
#  libdir = os.environ['PYDEVLIB']
#  if libdir not in sys.path: sys.path.insert(0, libdir ) 
##### Set global vars needed for init
#(prgdir,fname) = os.path.split(os.path.realpath(__file__))
#(prgname,ext) = os.path.splitext(fname)
libdir         = checkenv.chk_sufficient()
prgname,prgdir = checkenv.get_names(__file__)
###########   M A I N   ######################################################
def main():
  """ Main wrapper part for module calls
  """
  dbg.entersub()
  #dbg.dprint(cfg.config)
  if '/' in prgargs.name:
    requestname = os.path.basename(prgargs.name) 
  newpath = os.path.realpath(os.path.join(libdir,'..',prgargs.name))
  templdir = os.path.join(libdir,'template')
  dbg.dprint(2,"New Dir:", newpath,"from templates in",templdir)
  #sys.exit(0)
  try:
    os.makedirs(newpath)
  except Exception as e:
    dbg.exitf(e) 
  for top, dirs, files in os.walk(templdir):
    for f in files:
      if f.endswith('.py'):
        if f.startswith('main'):
          newf = f.replace('main',requestname)
          shutil.copy2(os.path.join(templdir,f), os.path.join(newpath,newf))
          dbg.dprint(2,"File:", newf)
        else: 
          shutil.copy2(os.path.join(templdir,f), os.path.join(newpath,f)) 
          dbg.dprint(2,"File:", f)
  dbg.leavesub()

###########   D E F A U L T   I N I T   #######################################
if __name__ == "__main__":
  from mydebug.py3dbg import dbg
  from myconf.py3cfg import init_cfg
  cfg = init_cfg(prgname,prgdir,libdir,dbg)
  exec(cfg.imports)
  exec(cfg.usage)
  main()
