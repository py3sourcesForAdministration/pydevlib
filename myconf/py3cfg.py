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
#print("in py3cfg")
#############################################################################
def try_import_rx(filename,parentdict,*items,tp='ro'):
  from __main__ import dbg
  importdict = type(parentdict)()
  foundlist  = []
  if not len(items):
    return "itemlist must not be empty"
  try:
    readobj = open(filename).read()
    if tp == 'rx':
      exec( readobj, importdict )
  except Exception as e:
    del importdict    
    return(e)
  
  for it in items:
    if tp == 'ro':
      parentdict[it] = readobj      
    else:
      if it in importdict:
        ### Check and print if overwriting
        if it in parentdict:
          dbg.dprint(256,type(parentdict),'[',it,']',parentdict[it])
        ###  
        foundlist.append(it)
        if isinstance(importdict[it],dict) :
          parentdict[it] = type(parentdict)(importdict.get(it))
        else:
          parentdict[it] = importdict.get(it) 
  del importdict    
  return foundlist
 
#############################################################################
def init_cfg(prgname,prgdir,libdir,dbg):
  """  This procedure returns a dictionary containing the important parts of
  configuration
  """
  #dbg.dprint(256, "in init_cfg")
  cfg = aDict() 
  cfg.prgname = prgname
  cfg.prgdir  = prgdir
  if prgdir not in sys.path:
    sys.path.insert(0, prgdir)
  files  = [ os.path.join(prgdir, prgname+'_imp.py'),
             os.path.join(prgdir, prgname+"_cfg.py"), 
             os.path.join(prgdir, prgname+"_usg.py")]
  for f in files:
    res = None
    if f.endswith("imp.py"):
      res = try_import_rx(f,cfg,'imports')
    elif f.endswith("cfg.py"):
      res = try_import_rx(f,cfg,'data','argdefaults','guidefs',tp='rx')
    elif f.endswith("usg.py"):
      res = try_import_rx(f,cfg,'usage')
    
    if not isinstance(res,list):
      dbg.exitf(res,"in",f)
  return(cfg) 
