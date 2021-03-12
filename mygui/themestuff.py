#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This is a module with classe to set up a default gui
"""
import os, sys
import tkinter as tk
import tkinter.ttk as ttk 
from addict import Dict as aDict
from PIL import ImageTk
# PhotoImage = ImageTk.PhotoImage

themepaths = {
  'black' : '/home/ap/Downloads/ttkblack/' ,
  'scid'  : '/home/ap/Downloads/scidthemes/' ,
  'aw'    : '/home/ap/Downloads/awthemes-10.2.1/',
  'tksvg' : '/home/ap/Downloads/tksvg0.7/',
}
try:
  from __main__ import prgdir,prgname
  exec(open(os.path.join(prgdir,prgname+"_imp.py")).read())
except:
  if sys.argv[0].find('pydoc'):
    pass # we are running from pydoc3

try:
  from __main__ import dbg,cfg
  pydevprog = True
except:
  pydevprog = False 
  print(__file__,"is not a pydevprog") 
  sys.exit(1)

##### ------------------------------------------------------------------------
def load_all_themes(root):
  style = ttk.Style(root)
  tkversion = tk.TkVersion 
  if tkversion >= 8.5: 
    blacktheme = os.path.join(themepaths['black'],'black.tcl')
    #print(blacktheme)
    root.tk.call('source', blacktheme )
  if tkversion == 8.6:  
    try: 
      #print(themepaths['tksvg'])
      root.tk.call('lappend', 'auto_path', themepaths['tksvg'])
      root.tk.call('package', 'require', 'tksvg')
    except Exception as e:
      if pydevprog:
        dbg.dprint(0,"Could not load tksvg:",e)
  if tkversion >= 8.6:    
    try:
      #print( themepaths['aw'])
      root.tk.call('lappend', 'auto_path', themepaths['aw'] ) 
      root.tk.call('package', 'require','colorutils')
      root.tk.call('package', 'require','awthemes')       
      root.tk.call("package", "require", 'awdark') 
      root.tk.call("package", "require", 'awlight')
      root.tk.call("package", "require", 'awarc')
      root.tk.call("package", "require", 'awbreeze')
      root.tk.call("package", "require", 'awclearlooks')
      root.tk.call("package", "require", 'awwinxpblue')
    except Exception as e:
      if pydevprog:
        dbg.dprint(0,"Could not load awthemes:",e)  
    #try:
    #  #print( themepaths['scid'])
    #  scidthemes = os.path.join(themepaths['scid'],'scidthemes.tcl')
    #  root.tk.call('source', scidthemes )
    #except Exception as e:
    #  dbg.dprint(0,"Could not load scidthemes:",e) 
  if pydevprog:
    cfg.guidefs.loaded = True 
  return style.theme_names()

##### ------------------------------------------------------------------------
def use_theme(root,*args):
  style = ttk.Style(root)
  themes = style.theme_names()
  for arg in args:
    #print(type(arg))
    if isinstance(arg,list) or isinstance(arg,tuple):
      for theme in arg:
        if theme in themes:
          break
    elif isinstance(arg,str):
      theme = arg
  #print("____",theme)    
  if theme not in themes:
    cfg.guidefs.theme = 'default'
  else:
    cfg.guidefs.theme = theme

  if theme in ['black', 'awdark']:
    cfg.guidefs.mode = 'dark'
  else :
    cfg.guidefs.mode = 'normal'
    #cfg.tkcols.bg = style.lookup('TFrame', 'background')

  style.theme_use(theme)
  if theme.startswith('aw'):
    if 'HiCol' in cfg.guidefs:   
      hicol = cfg.guidefs.HiCol
      cfg.tkcols.activebackground = hicol
      root.tk.call('::themeutils::setHighlightColor',theme,hicol)
    if 'BgCol' in cfg.guidefs:
      change_color = 0
      menu = tk.Menu(root)
      try:
        menu.winfo_rgb(cfg.guidefs.BgCol)
        change_color = 1
      except: 
        dbg.dprint(256,"could not use", cfg.guidefs.BgCol, "as background" )
      menu.delete()  
      if change_color:
        bgcol = cfg.guidefs.BgCol
        cfg.tkcols.bg = bgcol
        root.tk.call('::themeutils::setBackgroundColor',theme,bgcol)
    if 'Scroll' in cfg.guidefs and theme.startswith('aw'): 
      root.tk.call('::themeutils::setThemeColors',theme, 
                  'style.progressbar rounded-linetk.TkVersion',
                  'style.scale circle-rev',
                  'style.scrollbar-grip none',
                  'scrollbar.has.arrows false')
  return style.theme_use()      
          