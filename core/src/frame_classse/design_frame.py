# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Azur Lane Paintng Extract", pos = wx.DefaultPosition, size = wx.Size( 1024,576 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 512,288 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetMinSize( wx.Size( 325,-1 ) )
		self.m_panel1.SetMaxSize( wx.Size( 325,-1 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		m_choice_filterChoices = [ u"全部", u"仅原始立绘", u"仅皮肤立绘", u"仅改造立绘", u"仅婚纱立绘", u"仅幼女化立绘" ]
		self.m_choice_filter = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_filterChoices, 0 )
		self.m_choice_filter.SetSelection( 0 )
		bSizer8.Add( self.m_choice_filter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer8.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_searchCtrl1 = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		self.m_searchCtrl1.ShowSearchButton( False )
		self.m_searchCtrl1.ShowCancelButton( True )
		bSizer8.Add( self.m_searchCtrl1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( bSizer8, 0, wx.EXPAND, 5 )

		self.m_treeCtrl_info = wx.TreeCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HAS_BUTTONS|wx.TR_HAS_VARIABLE_ROW_HEIGHT|wx.TR_HIDE_ROOT|wx.TR_ROW_LINES|wx.TR_SINGLE|wx.TR_TWIST_BUTTONS )
		bSizer3.Add( self.m_treeCtrl_info, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_work = wx.Button( self.m_panel1, wx.ID_ANY, u"导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_work, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_change = wx.Button( self.m_panel1, wx.ID_ANY, u"选择对应文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_change, 0, wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer5.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_setting = wx.Button( self.m_panel1, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button_setting, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )

		self.m_gauge_state = wx.Gauge( self.m_panel1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_state.SetValue( 0 )
		bSizer4.Add( self.m_gauge_state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer6.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer6.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_show = wx.StaticBitmap( self.m_scrolledWindow1, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap_show, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer2 )
		self.m_scrolledWindow1.Layout()
		bSizer2.Fit( self.m_scrolledWindow1 )
		bSizer6.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_info.Wrap( -1 )

		bSizer1.Add( self.m_staticText_info, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.exit )
		self.m_choice_filter.Bind( wx.EVT_CHOICE, self.filter_work )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT, self.search )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT_ENTER, self.search )
		self.m_treeCtrl_info.Bind( wx.EVT_TREE_SEL_CHANGED, self.on_info_select )
		self.m_button_work.Bind( wx.EVT_BUTTON, self.work )
		self.m_button_change.Bind( wx.EVT_BUTTON, self.choice_file )
		self.m_button_setting.Bind( wx.EVT_BUTTON, self.setting )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def exit( self, event ):
		event.Skip()

	def filter_work( self, event ):
		event.Skip()

	def search( self, event ):
		event.Skip()


	def on_info_select( self, event ):
		event.Skip()

	def work( self, event ):
		event.Skip()

	def choice_file( self, event ):
		event.Skip()

	def setting( self, event ):
		event.Skip()


###########################################################################
## Class MyDialogSetting
###########################################################################

class MyDialogSetting ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( 544,477 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox_ex_cn = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"使用中文名作为导出文件名（如果可用）", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_ex_cn, 0, wx.ALL, 5 )

		self.m_checkBox_new_dir = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"在导出目标目录下新建导出文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_new_dir, 0, wx.ALL, 5 )

		self.m_staticline8 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_checkBox_open_dir = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"完成后打开导出目标文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_open_dir.SetValue(True)
		bSizer10.Add( self.m_checkBox_open_dir, 0, wx.ALL, 5 )

		self.m_checkBox_skip_exist = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"跳过目标目录中已经存在的同名文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_skip_exist, 0, wx.ALL, 5 )

		self.m_checkBox_clear_list = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"导入时清空原有列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_clear_list, 0, wx.ALL, 5 )

		self.m_checkBox_finish_exit = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"完成任务后退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_finish_exit, 0, wx.ALL, 5 )

		self.m_checkBox_ex_copy = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"导出全部时同时拷贝不可还原", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox_ex_copy, 0, wx.ALL, 5 )

		self.m_staticline10 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_bitmap2 = wx.StaticBitmap( self.m_panel2, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_bitmap2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer10 )
		self.m_panel2.Layout()
		bSizer10.Fit( self.m_panel2 )
		bSizer9.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer9.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		m_radioBox_input_filterChoices = [ u"全部立绘", u"全部初始皮肤", u"全部皮肤", u"全部改造立绘", u"全部誓约立绘", u"全部幼女化立绘" ]
		self.m_radioBox_input_filter = wx.RadioBox( self.m_panel3, wx.ID_ANY, u"导入文件筛选", wx.DefaultPosition, wx.DefaultSize, m_radioBox_input_filterChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_input_filter.SetSelection( 5 )
		bSizer11.Add( self.m_radioBox_input_filter, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline9 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

		m_radioBox_output_groupChoices = [ u"不分类", u"按舰娘名称分类", u"按立绘类型分类" ]
		self.m_radioBox_output_group = wx.RadioBox( self.m_panel3, wx.ID_ANY, u"导出文件分类", wx.DefaultPosition, wx.DefaultSize, m_radioBox_output_groupChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_output_group.SetSelection( 0 )
		bSizer11.Add( self.m_radioBox_output_group, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer11 )
		self.m_panel3.Layout()
		bSizer11.Fit( self.m_panel3 )
		bSizer9.Add( self.m_panel3, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )

		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer8.Add( m_sdbSizer1, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.set_info )
		self.m_sdbSizer1Apply.Bind( wx.EVT_BUTTON, self.apply_press )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.cancel_press )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.ok_press )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def set_info( self, event ):
		event.Skip()

	def apply_press( self, event ):
		event.Skip()

	def cancel_press( self, event ):
		event.Skip()

	def ok_press( self, event ):
		event.Skip()


