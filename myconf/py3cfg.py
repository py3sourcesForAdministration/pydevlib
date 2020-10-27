#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" function for storing program data in a addict
    Will only work if the calling main program already
    offers the globals prgname, prgdir, 
    libdir (from the env var "PYDEVLIB") 
    and another singleton dbg
    Import only once ! 
    This module is indispensable part of "pydevlib" project
"""

import sys, os , os.path
from addict import Dict as aDict

def init_cfg(prgname,prgdir,libdir,dbg):
  """  This procedure returns a dictionary containing the important parts of
  configuration
  """
  cfg = aDict() 
  cfg.prgname = prgname
  cfg.prgdir  = prgdir
#  cfg.libdir  = libdir
  if prgdir not in sys.path:
    sys.path.insert(0, prgdir)
  files  = [ os.path.join(prgdir, prgname+'_imp.py'),
             os.path.join(prgdir, prgname+"_cfg.py"), 
             os.path.join(prgdir, prgname+"_usg.py")]
  try:
    for f in files:
      confdict = {}
      ### read importfile
      if f.endswith("imp.py"):
        cfg.imports = open(f).read()
        exec(cfg.imports,confdict)  
      ### read config, evaluate and extract vars  
      elif f.endswith("cfg.py"):
        exec(open(f).read(),confdict)
        cfg.data = aDict(confdict['data'])
      ### read usagefile     
      elif f.endswith("usg.py"): 
        cfg.usage   = open(f).read()
    del confdict
  ### These are the usual errors       
  except KeyError as message:
      dbg.exitf("Keyerror "+message)
  except IOError as e:
      #print("Unable to read: {0} {1}".format(f, e.strerror)) 
      dbg.exitf("Unable to read: "+f+" "+e.strerror) 
  except sys.exc_info()[0]:
    if not ( repr(sys.exc_info()[1]) == "SystemExit(0,)" or \
             repr(sys.exc_info()[1]) == "SystemExit(0)" ):     # py3.9 
      dbg.exitf("Error exit: "+sys.exc_info()[1]+" in "+f)
  except: 
      dbg.exitf("Some unknown error in loading file "+f)
#      print("Init: Some unknown error in loading file ",f); sys.exit(1)
  return(cfg) 
