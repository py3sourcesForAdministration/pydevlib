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
  'aw'    : '/home/ap/Downloads/awthemes-10.3.0/',
  'tksvg' : '/home/ap/Downloads/tksvg0.7/',
}
try:
  from __main__ import prgdir,prgname
  exec(open(os.path.join(prgdir,prgname+"_imp.py")).read())
  pydevprog = True
except:
  pydevprog = False
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
  already_loaded = style.theme_names()

  tkversion = tk.TkVersion
  themelist = [] 
  if tkversion >= 8.5: 
    blacktheme = os.path.join(themepaths['black'],'black.tcl')
    try:
      if 'black' not in already_loaded:
        root.tk.call('source', blacktheme )
        themelist.append('black')
    except Exception as e:
      if pydevprog:
        dbg.dprint(0,"Could not load theme black:",e)

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
      root.tk.call('package', 'require','awthemes')       
      root.tk.call('package', 'require','colorutils')
      themes = [f for f in os.listdir(themepaths['aw']) if os.path.isfile(os.path.join(themepaths['aw'], f)) and f.startswith('aw') and f.endswith('.tcl')]
      #print(themes)
      for f in themes:
        if f == 'awthemes.tcl' or f == 'awtemplate.tcl':
          continue
        t = f.split('.')[0]
        themelist.append(t)
      #root.tk.call("package", "require", 'awdark') 
      #root.tk.call("package", "require", 'awlight')
      #root.tk.call("package", "require", 'awarc')
      #root.tk.call("package", "require", 'awbreeze')
      #root.tk.call("package", "require", 'awbreezedark')
      #root.tk.call("package", "require", 'awclearlooks')
      #root.tk.call("package", "require", 'awwinxpblue')
    except Exception as e:
      if pydevprog:
        dbg.dprint(0,"Could not load awthemes:",e)  
    try:
    #  #print( themepaths['scid'])
      scidthemes = os.path.join(themepaths['scid'],'scidthemes.tcl')
      if 'scidgrey' not in already_loaded:
        root.tk.call('source', scidthemes )
    except Exception as e:
      dbg.dprint(0,"Could not load scidthemes:",e) 
    themes = [f for f in os.listdir(themepaths['scid']) if os.path.isdir(os.path.join(themepaths['scid'], f))]
    #print(themes)
    for f in themes:
      if f == 'scid':
        continue
      themelist.append(f)
  if pydevprog:
    cfg.guidefs.loaded = True
    
  return themelist

##### ------------------------------------------------------------------------
def use_theme(root,themes,*args,**kwargs):
  reconfig = False  
  if 'reconfigure' in kwargs:
    reconfig = kwargs['reconfigure']
  style = ttk.Style(root)
  for arg in args:
    if isinstance(arg,list) or isinstance(arg,tuple):
      for theme in arg:
        if theme in themes:
          break
    elif isinstance(arg,str):
      theme = arg
  if theme not in themes:
    cfg.guidefs.theme = 'default'
  else:
    cfg.guidefs.theme = theme
  cfg.tkcols.clear()
  
  #style.theme_use(theme)
  #deffg  = str(style.lookup('TMenuButton', 'foreground'))
  #defbg  = str(style.lookup('TMenubutton', 'background'))
  #defafg = str(style.lookup('TMenubutton', 'foreground',state=['active']))
  #defabg = str(style.lookup('TMenubutton', 'background',state=['active']))
   
  if theme in ['black', 'awdark','awbreezedark']:
    cfg.guidefs.mode = 'dark'
  else :
    cfg.guidefs.mode = 'normal'
  #cfg.tkcols.fg = deffg
  #cfg.tkcols.bg = defbg
  #cfg.tkcols.activeforeground = defafg
  #cfg.tkcols.activebackground = defabg
  
  if theme.startswith('aw'):
    root.tk.call('package', 'require','awthemes')       
    root.tk.call('package', 'require','colorutils')       
    if 'BgCol' in cfg.guidefs:
      dbg.dprint(0, "Wanted BG:",cfg.guidefs.BgCol)
      #bgcol = cfg.guidefs.BgCol
      #dbg.dprint(0,"set bgcol",bgcol)  
      #cfg.tkcols.bg = bgcol
      #root.tk.call('package', 'require','awthemes')       
      #root.tk.call('package', 'require','colorutils')       
      root.tk.call('::themeutils::setBackgroundColor',theme,cfg.guidefs.BgCol)
    if 'HiCol' in cfg.guidefs: 
      dbg.dprint(0, "Wanted Hi:",cfg.guidefs.HiCol)
      #hicol = cfg.guidefs.HiCol  
      #dbg.dprint(0,"set hicol",hicol)  
      #cfg.tkcols.activebackground = hicol
      root.tk.call('::themeutils::setHighlightColor',theme,cfg.guidefs.HiCol)
    #else:
    #  cfg.tkcols.bg = defbg    
    if 'Scroll' in cfg.guidefs: 
      root.tk.call('::themeutils::setThemeColors',theme, 
                  'style.progressbar rounded-linetk.TkVersion',
                  'style.scale circle-rev',
                  'style.scrollbar-grip none',
                  'scrollbar.has.arrows false')
    root.tk.call('package', 'require',theme)       
  ### reconfigure menubar
  style.theme_use(theme)
  cfg.tkcols['activebackground'] = root.tk.call( 
         '::ttk::style','lookup','TEntry','-selectbackground','focus')
  cfg.tkcols['bg'] = root.tk.call( 
         '::ttk::style','lookup','TButton','-background')   
  cfg.tkcols['fg'] = root.tk.call( 
         '::ttk::style','lookup','TButton','-foreground')
  cfg.tkcols['activeforeground'] = root.tk.call( 
         '::ttk::style','lookup','TButton','-foreground')

  dbg.dprint(2,theme,cfg.tkcols)
  if 'menubar' in cfg.widgets:
    newdict = cfg.widgets.menubar
    for menu in newdict:
      dbg.dprint(4,menu,newdict[menu])
      newdict[menu].configure(**cfg.tkcols) 
  if 'contentmenu' in cfg.widgets:
    newdict = cfg.widgets.contentmenu
    for menu in newdict:
      dbg.dprint(4,menu,newdict[menu])
      newdict[menu].configure(**cfg.tkcols) 
  return style.theme_use()      
          
