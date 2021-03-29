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
  if pydevprog:
    dbg.entersub()
    if dbg.key_exists(cfg,'.guidefs.available_themes'):
      dbg.leavesub()
      return cfg.guidefs.available_themes

  style = ttk.Style(root)
  tkversion = tk.TkVersion
  themelist = list(style.theme_names()) 
  if tkversion >= 8.5: 
    blacktheme = os.path.join(themepaths['black'],'black.tcl')
    try:
      if 'black' not in themelist:
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
      themes = [f for f in os.listdir(themepaths['aw']) \
                if os.path.isfile(os.path.join(themepaths['aw'], f)) \
                and f.startswith('aw') and f.endswith('.tcl')]
      for f in themes:
        if f == 'awthemes.tcl' or f == 'awtemplate.tcl':
          continue
        t = f.split('.')[0]
        if t not in themelist:
          themelist.append(t)
    except Exception as e:
      if pydevprog:
        dbg.dprint(0,"Could not load awthemes:",e)  
    
    try:
    #  #print( themepaths['scid'])
      scidthemes = os.path.join(themepaths['scid'],'scidthemes.tcl')
      if 'scidgrey' not in themelist:
        root.tk.call('source', scidthemes )
      themes = [f for f in os.listdir(themepaths['scid']) \
               if os.path.isdir(os.path.join(themepaths['scid'], f))]
      for f in themes:
        if f == 'scid':
          continue
        if f not in themelist:
          themelist.append(f)

    except Exception as e:
      if pydevprog:
        dbg.dprint(0,"Could not load scidthemes:",e) 

  if pydevprog:
    cfg.guidefs.loaded = True  
    cfg.guidefs.available_themes = themelist
    dbg.dprint(4,dbg.myname(),"Loaded Themes:",themelist)
    dbg.leavesub()
    
  return themelist

##### ------------------------------------------------------------------------
def use_theme(root,wanted,**kwargs):
  """ This function expects:
  1. the top widget
  2. a single theme name or a list of wanted themes (first match is selected)
  3. optionally the keyword reconfigure=True|False
  Selects the wanted theme or default if wanted is not available
  Sets the colors of known (pydevprog) menus 
  """   
  style = ttk.Style(root)
  if pydevprog:
    dbg.entersub()
    cfg.tkcols.clear()
  themes = load_all_themes(root)    
  if isinstance(wanted,list) or isinstance(wanted,tuple):
    for theme in wanted:
        if theme in themes:
          break
  elif isinstance(wanted,str):
    theme = wanted
  if theme not in themes:
    theme = 'default'

  #print("Selected",theme) 
  if theme.startswith('aw'):
    if pydevprog and theme not in style.theme_names():
      root.tk.call('package', 'require','awthemes')       
      root.tk.call('package', 'require','colorutils')       
      if 'BgCol' in cfg.guidefs:
        #dbg.dprint(0, "Wanted BG:",cfg.guidefs.BgCol)
        root.tk.call('::themeutils::setBackgroundColor',theme,cfg.guidefs.BgCol)
      if 'HiCol' in cfg.guidefs: 
        #dbg.dprint(0, "Wanted Hi:",cfg.guidefs.HiCol)
        root.tk.call('::themeutils::setHighlightColor',theme,cfg.guidefs.HiCol)
      if 'Scroll' in cfg.guidefs: 
        root.tk.call('::themeutils::setThemeColors',theme, 
                  'style.progressbar rounded-linetk.TkVersion',
                  'style.scale circle-rev',
                  'style.scrollbar-grip none',
                  'scrollbar.has.arrows false')
      root.tk.call('package', 'require',theme)

  style.theme_use(theme)
  ### get colors for menubar
  tkcols = {}
  tkcols['activebackground'] = root.tk.call( 
         '::ttk::style','lookup','TEntry','-selectbackground','focus')
  tkcols['bg']               = root.tk.call( 
         '::ttk::style','lookup','TButton','-background')   
  tkcols['fg']               = root.tk.call( 
         '::ttk::style','lookup','TButton','-foreground')
  tkcols['activeforeground'] = root.tk.call( 
         '::ttk::style','lookup','TButton','-foreground')
  ### reconfigure menubar
  if pydevprog:
    cfg.tkcols = tkcols
    dbg.dprint(2,"Selected Theme:",theme,", Colors:",cfg.tkcols)
    if 'menubar' in cfg.widgets:
      newdict = cfg.widgets.menubar
      for menu in newdict:
        dbg.dprint(8,"ColorConfig:",menu,newdict[menu])
        newdict[menu].configure(**tkcols) 
    if 'contentmenu' in cfg.widgets:
      newdict = cfg.widgets.contentmenu
      for menu in newdict:
        dbg.dprint(8,"ColorConfig:",menu,newdict[menu])
        newdict[menu].configure(**tkcols) 
    dbg.leavesub()    
  
  return style.theme_use()      
          
