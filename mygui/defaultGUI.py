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
try:
  from __main__ import prgdir,prgname
  exec(open(os.path.join(prgdir,prgname+"_imp.py")).read())
except:
  if sys.argv[0].find('pydoc'):
    pass # we are running from pydoc3

try:
  from __main__ import dbg,cfg
  pydevprog = True
  #print(__file__,"is a pydevprog") 
except:
  pydevprog = False 
  print(__file__,"is not a pydevprog") 
  sys.exit(1)

##### ------------------------------------------------------------------------
class MenubBar(ttk.Frame):
  def __init__(self,master=None, **kw):
    self.myname = type(self).__name__
    dbg.dprint(4,self.myname, "is pydevprog") 
    cfg.widgets[self.myname] = self
    super().__init__(master, **kw)
    self.File = ttk.Menubutton(self)
    dropF = tk.Menu(self.File)
    dropF.add_command(label='Quit', command=self.quit())
    self.File['menu'] = dropF
    self.File.configure(state='normal', takefocus=False, text='File', width='4')
    self.File.grid(column='0', row='0', sticky='w')
    self.Edit = ttk.Menubutton(self)
    self.Edit.configure(compound='bottom', cursor='arrow', takefocus=False, text='Edit')
    self.Edit.configure(width='4')
    self.Edit.grid(column='1', row='0', sticky='w')
    self.Help = ttk.Menubutton(self)
    self.Help.configure(text='Help', width='4')
    self.Help.grid(column='10', row='0', sticky='e')
    self.frame2_2 = ttk.Frame(self)
    self.frame2_2.configure(height='20', width='4')
    self.frame2_2.grid(column='3', columnspan='6', row='0', sticky='ew')
    self.frame2_2.columnconfigure('3', weight='1')
  
#  def toc_menu(self, text):
#        "Create table of contents as drop-down menu."
#        toc = Menubutton(self, text='TOC')
#        drop = Menu(toc, tearoff=False)
#        for lbl, dex in text.parser.toc:
#            drop.add_command(label=lbl, command=lambda dex=dex:text.yview(dex))
#        toc['menu'] = drop
#        return toc 
##### ------------------------------------------------------------------------

##### ------------------------------------------------------------------------
class MenuBar(ttk.Frame):
  def __init__(self,master=None, **kw):
    self.myname = type(self).__name__
    dbg.dprint(4,self.myname, "is pydevprog") 
    cfg.widgets[self.myname] = self
    if master is not None:
      super().__init__(master, **kw)
      # colorlist = dict(cfg.tkcols)
      #colorlist = dict()
      #colorlist['bg'] = '#d9d9d9'
      #colorlist['fg'] = '#000000'
      #colorlist['activebackground'] = '#8FA876'
      #dbg.dprint(0,'Colorlist',colorlist)
      #self.mainmenu = tk.Menu(master,tearoff=0,fg='#000000',bg='#d9d9d9')
      self.mainmenu = tk.Menu(master,tearoff=0,)
      self.master.config(menu=self.mainmenu)
      
      filemenu = tk.Menu(self.mainmenu, tearoff=0,)
      filemenu.add_command(label='Open',command=self.showc)
      filemenu.add_command(label='Save',command=self.showc)
      filemenu.add_separator()
      filemenu.add_command(label='Exit',command=self.Exit)
      self.mainmenu.add_cascade(label='File',menu=filemenu)
      helpmenu = tk.Menu(self.mainmenu, tearoff=0,)
      helpmenu.add_command(label='About',command=self.showc)
      self.mainmenu.add_cascade(label='Help',menu=helpmenu)

  def showc(self):
    dbg.dprint(0,self.myname,dbg.myname(),"command not yet done")

  def Exit(self):
    self.quit()
  
  def About(self):
    dbg.dprint(0,self.myname,dbg.myname(),"command not yet done")

##### ------------------------------------------------------------------------
class StatusBar(ttk.Frame):
  def __init__(self,master=None, **kw):
    self.myname = type(self).__name__
    dbg.dprint(4,self.myname, "is pydevprog") 
    cfg.widgets[self.myname] = self
    super().__init__(master, **kw)
    self.stat_msg = tk.StringVar()
    self.stat_inp = tk.IntVar(0)
    self.stat_msg.set('nix')
    self.status   = ttk.Label(self) 
    self.status.configure(textvariable=self.stat_inp,
                          width=1)
    self.message  = ttk.Label(self,
                      textvariable=self.stat_msg,
                      relief='sunken',
                      width=25)
    ### setup expand    
    self.status.grid(row=0,column=0,sticky='w',padx=2)
    self.message.grid(row=0,column=1,sticky='ew',padx=0,pady=2)
    self.grid_columnconfigure(1,weight=1)
  
  def toggle_status(self):
    print("in toggle, current state", self.stat_inp.get())
    if self.stat_inp.get() == 0:
      self.stat_inp.set(1)
    else:
      self.stat_inp.set(0)

  def display(self,msg):
    print(msg)
    self.stat_msg.set(msg) 
    print(self.message, type(self.message)) 
    self.message.after(10000,self.clear)
  
  def clear(self):
    print("in clear") 
    self.stat_msg.set('')

##### ------------------------------------------------------------------------
class TestContent(ttk.Frame):
  def __init__(self,master=None, **kw):
    self.myname = type(self).__name__
    dbg.dprint(4,self.myname, "is pydevprog") 
    cfg.widgets[self.myname] = self
    super().__init__(master,**kw)
    self.l1 = ttk.Label(self, text="   F2-L1\ncentered",relief='ridge',anchor='center')
    self.l2 = ttk.Label(self, text="F2-L2",relief='ridge',anchor='center')
    self.l3 = ttk.Label(self, text="F2-L3",relief='ridge',anchor='center')
    self.l1.grid(row=0,column=0,sticky='nsew')
    self.l2.grid(row=0,column=1,sticky='nsew')
    self.l3.grid(row=0,column=2,sticky='nsew')
    self.grid_columnconfigure(0,weight=1)
    self.grid_columnconfigure(1,weight=1)
    self.grid_columnconfigure(2,weight=1)
    self.grid_rowconfigure(0,weight=1)

##### ------------------------------------------------------------------------
class ThemeSelect(ttk.Frame):
  def __init__(self,master=None, **kw):
    self.myname = type(self).__name__
    dbg.dprint(4,self.myname, "is pydevprog") 
    cfg.widgets[self.myname] = self
    super().__init__(master, **kw)
    if master is not None:
      self.style = ttk.Style(master)
    else:   
      self.style = ttk.Style()
    self.theme_autochange = tk.IntVar(self, 0)

    self._setup_widgets()

  def _change_theme(self):
    self.style.theme_use(self.themes_combo.get())


  def _theme_sel_changed(self, widget):
    if self.theme_autochange.get():
      self._change_theme()

  def _setup_widgets(self):
    themes_lbl = ttk.Label(self, text="Themes")
    themes = sorted(self.style.theme_names())
    self.themes_combo = ttk.Combobox(self, values=themes, state="readonly")
    self.themes_combo.set(themes[0])
    self.themes_combo.bind("<<ComboboxSelected>>", self._theme_sel_changed)
    change_btn = ttk.Button(self, text='Change Theme',
            command=self._change_theme)
    theme_change_checkbtn = ttk.Checkbutton(self,
            text="Change themes when combobox item is activated",
            variable=self.theme_autochange)
    mb = ttk.Menubutton(self,
            text="Menubutton to see effects")
    mb.menu =  tk.Menu( mb, tearoff = 0 )
    mb["menu"] =  mb.menu        
    mb.menu.add_cascade(label='Test')        
    mb.menu.add_command(label='Test1')        
    mb.menu.add_command(label='Test2')        
    
    themes_lbl.grid(           row=0, column=0,ipadx=6, sticky="w")
    self.themes_combo.grid(    row=0, column=1, padx=6, sticky="ew")
    change_btn.grid(           row=0, column=2, padx=6, sticky="e")
    theme_change_checkbtn.grid(row=1, column=0, pady=6, columnspan=3, sticky="w")
    mb.grid(row=2, column=0, pady=6, columnspan=3, sticky="w")
    self.columnconfigure(1, weight=1)


##### ------------------------------------------------------------------------
#def load_theme(root,theme='default'):  
#  style = ttk.Style(root)
#  if pydevprog:
#    from __main__ import dbg,cfg 
#    cfg.widgets['root'] = root
#    dbg.dprint(4,"Tcl Version:",tk.TkVersion)
#    if 'theme' in cfg.guidefs:
#      theme = cfg.guidefs.theme
#    if tk.TkVersion == 8.6:  
#      if 'tksvgpath' in cfg.guidefs and tk.TkVersion == 8.6:
#        try: 
#          root.tk.call('lappend', 'auto_path', cfg.guidefs.tksvgpath)
#          root.tk.call('package', 'require', 'tksvg')
#        except Exception as e:
#          dbg.dprint(0,"Could not load tksvg:",e)
#    elif tk.TkVersion == 8.5:
#      try:
#        root.tk.call('lappend', 'auto_path', cfg.guidefs.tksvgpath)
#        root.tk.call('source', cfg.guidefs.tksvgpath+'/try.tcl')
#        root.tk.call('source', cfg.guidefs.tksvgpath+'/throw.tcl')
#        dbg.dprint(4,'try loaded')
#      except: 
#        dbg.dprint(0,'could not load try')
#
#    if theme.startswith('aw'):
#      try:  
#        root.tk.call('lappend', 'auto_path', cfg.guidefs.awthemespath)
#        root.tk.call('package', 'require','colorutils')
#        root.tk.call('package', 'require','awthemes')
#        if 'HiCol' in cfg.guidefs:   
#          hicol = cfg.guidefs.HiCol
#          root.tk.call('::themeutils::setHighlightColor',theme,hicol)
#        if 'BgCol' in cfg.guidefs: 
#          bgcol = cfg.guidefs.BgCol
#          root.tk.call('::themeutils::setBackgroundColor',theme,bgcol)
#        if 'Scroll' in cfg.guidefs: 
#          root.tk.call('::themeutils::setThemeColors',theme, 
#                       'style.progressbar rounded-linetk.TkVersion',
#                       'style.scale circle-rev',
#                       'style.scrollbar-grip none',
#                       'scrollbar.has.arrows false')
#        ### call theme               
#        root.tk.call("package", "require", theme)
#        dbg.dprint(4,"awthemes done") 
#      except Exception as e:
#        dbg.dprint(0,"Could not load awthemes:",e)
#  #print(style.theme_names()) 
#  if theme in style.theme_names():
#    ttk.Style().theme_use(theme)    
##### ------------------------------------------------------------------------
#def startinit(*args):
#  try:
#    from __main__ import dbg,cfg
#    pydevprog = True
#  except:
#    pydevprog = False
#  return pydevprog
    #if startinit() and 'tksvgpath' in cfg.guidefs and tk.TkVersion == 8.6:
    #  print(cfg.guidefs.tksvgpath)  
    #  try: 
    #    master.tk.call('lappend', 'auto_path', cfg.guidefs.tksvgpath)
    #    master.tk.call('package', 'require', 'tksvg')
    #  except Exception as e:
    #    dbg.dprint(0,"Could not load tksvg:",e)
    #  print(cfg.guidefs.awthemespath)  
    #  try:
    #    master.tk.call('lappend', 'auto_path', cfg.guidefs.awthemespath)
    #    master.tk.call('package', 'require','awthemes')
    #    master.tk.call("package", "require", 'awdark') 
    #    master.tk.call("package", "require", 'awlight')
    #    master.tk.call("package", "require", 'awarc')
    #    master.tk.call("package", "require", 'awbreeze')
    #    master.tk.call("package", "require", 'awclearlooks')
    #    master.tk.call("package", "require", 'awwinxpblue')
    #  except Exception as e:
    #    if startinit():
    #      dbg.dprint(0,"Could not load awthemes:",e)
    #    else:
    #      print("Could not load awthemes:",e) #