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

		m_choice_filterChoices = [ u"全部", u"仅原始立绘", u"仅皮肤立绘", u"仅改造立绘", u"仅婚纱立绘", u"仅幼女化立绘", u"仅μ兵装立绘", u"其他立绘" ]
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

		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_show = wx.StaticBitmap( self.m_scrolledWindow2, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_MISSING_IMAGE, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_bitmap_show, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_scrolledWindow2.SetSizer( bSizer12 )
		self.m_scrolledWindow2.Layout()
		bSizer12.Fit( self.m_scrolledWindow2 )
		bSizer6.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )


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
		self.Bind( wx.EVT_KEY_DOWN, self.on_key_Down )
		self.Bind( wx.EVT_MOVE_END, self.resize )
		self.m_choice_filter.Bind( wx.EVT_CHOICE, self.filter_work )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT, self.search )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT_ENTER, self.search )
		self.m_treeCtrl_info.Bind( wx.EVT_TREE_SEL_CHANGED, self.on_info_select )
		self.m_button_work.Bind( wx.EVT_BUTTON, self.work )
		self.m_button_change.Bind( wx.EVT_BUTTON, self.choice_file )
		self.m_button_setting.Bind( wx.EVT_BUTTON, self.setting )
		self.m_scrolledWindow2.Bind( wx.EVT_KEY_DOWN, self.on_key_dwon )
		self.m_scrolledWindow2.Bind( wx.EVT_KEY_UP, self.on_key_dwon )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def exit( self, event ):
		event.Skip()

	def on_key_Down( self, event ):
		event.Skip()

	def resize( self, event ):
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

	def on_key_dwon( self, event ):
		event.Skip()



###########################################################################
## Class MyDialogAtlasSpilt
###########################################################################

class MyDialogAtlasSpilt ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"atlas切割工具", pos = wx.DefaultPosition, size = wx.Size( 512,256 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_target_name = wx.StaticText( self.m_panel8, wx.ID_ANY, u"目标名称：None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_target_name.Wrap( -1 )

		bSizer33.Add( self.m_staticText_target_name, 0, wx.ALL, 5 )

		self.m_filePicker_target_atlas = wx.FilePickerCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, u"Select a file", u"atlas切割信息文件(*.atlas;*.atlas.txt)|*.atlas;*.atlas.txt", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL|wx.FLP_USE_TEXTCTRL )
		bSizer33.Add( self.m_filePicker_target_atlas, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox_spilt_itemsChoices = []
		self.m_listBox_spilt_items = wx.ListBox( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_spilt_itemsChoices, 0 )
		bSizer33.Add( self.m_listBox_spilt_items, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel8.SetSizer( bSizer33 )
		self.m_panel8.Layout()
		bSizer33.Fit( self.m_panel8 )
		bSizer32.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline27 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer32.Add( self.m_staticline27, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_bitmap_show = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_bitmap_show, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer31.Add( bSizer32, 1, wx.EXPAND, 5 )

		self.m_staticline28 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer31.Add( self.m_staticline28, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2Save = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Save )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();

		bSizer34.Add( m_sdbSizer2, 0, 0, 5 )

		self.m_staticline29 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer34.Add( self.m_staticline29, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, u"就绪", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_END )
		self.m_staticText_info.Wrap( -1 )

		bSizer34.Add( self.m_staticText_info, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer31.Add( bSizer34, 0, wx.EXPAND, 5 )


		bSizer30.Add( bSizer31, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer30 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_KEY_DOWN, self.on_key_down )
		self.m_filePicker_target_atlas.Bind( wx.EVT_FILEPICKER_CHANGED, self.load_atlas )
		self.m_listBox_spilt_items.Bind( wx.EVT_LISTBOX, self.view_item )
		self.m_listBox_spilt_items.Bind( wx.EVT_LISTBOX_DCLICK, self.save_item )
		self.m_sdbSizer2Cancel.Bind( wx.EVT_BUTTON, self.exit )
		self.m_sdbSizer2Save.Bind( wx.EVT_BUTTON, self.save_all )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_key_down( self, event ):
		event.Skip()

	def load_atlas( self, event ):
		event.Skip()

	def view_item( self, event ):
		event.Skip()

	def save_item( self, event ):
		event.Skip()

	def exit( self, event ):
		event.Skip()

	def save_all( self, event ):
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

		self.m_staticText13 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"导入文件筛选", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer11.Add( self.m_staticText13, 0, wx.ALL, 5 )

		m_choice_inport_filterChoices = [ u"全部立绘", u"全部初始皮肤", u"全部皮肤", u"全部改造立绘", u"全部誓约立绘", u"全部幼女化立绘", u"全部μ兵装立绘", u"其他立绘" ]
		self.m_choice_inport_filter = wx.Choice( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_inport_filterChoices, 0 )
		self.m_choice_inport_filter.SetSelection( 0 )
		bSizer11.Add( self.m_choice_inport_filter, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline9 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"导出文件分类", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer11.Add( self.m_staticText14, 0, wx.ALL, 5 )

		m_choice_export_divisionChoices = [ u"不分类", u"按舰娘名称分类", u"按立绘类型分类" ]
		self.m_choice_export_division = wx.Choice( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_export_divisionChoices, 0 )
		self.m_choice_export_division.SetSelection( 0 )
		bSizer11.Add( self.m_choice_export_division, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline27 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline27, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_updata_names = wx.Button( self.m_panel3, wx.ID_ANY, u"更新本地化资源", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button_updata_names, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline12 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer12.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_edit_names = wx.Button( self.m_panel3, wx.ID_ANY, u"编辑本地化资源", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button_edit_names, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer11.Add( bSizer12, 0, wx.EXPAND, 5 )

		self.m_staticline271 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline271, 0, wx.EXPAND |wx.ALL, 5 )


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
		self.m_choice_inport_filter.Bind( wx.EVT_CHOICE, self.import_filter )
		self.m_choice_export_division.Bind( wx.EVT_CHOICE, self.output_group )
		self.m_button_updata_names.Bind( wx.EVT_BUTTON, self.update_names )
		self.m_button_edit_names.Bind( wx.EVT_BUTTON, self.edit_names )
		self.m_sdbSizer1Apply.Bind( wx.EVT_BUTTON, self.apply_press )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.cancel_press )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.ok_press )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def set_info( self, event ):
		event.Skip()

	def import_filter( self, event ):
		event.Skip()

	def output_group( self, event ):
		event.Skip()

	def update_names( self, event ):
		event.Skip()

	def edit_names( self, event ):
		event.Skip()

	def apply_press( self, event ):
		event.Skip()

	def cancel_press( self, event ):
		event.Skip()

	def ok_press( self, event ):
		event.Skip()


###########################################################################
## Class MyDialogKetValueSetting
###########################################################################

class MyDialogKetValueSetting ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"编辑键值对", pos = wx.DefaultPosition, size = wx.Size( 256,512 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		m_listBox_name_existChoices = []
		self.m_listBox_name_exist = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_name_existChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE )
		bSizer14.Add( self.m_listBox_name_exist, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )

		self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer13.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"键【KEY】", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer15.Add( self.m_staticText3, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl_new_key = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_textCtrl_new_key, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"值【value】", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer15.Add( self.m_staticText4, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl_new_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_textCtrl_new_value, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline16 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer15.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton_import_names = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_import_names.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_BUTTON ) )
		bSizer16.Add( self.m_bpButton_import_names, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline17 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer16.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_clear = wx.Button( self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button_clear, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_add = wx.Button( self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button_add, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer16, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		bSizer13.Add( bSizer15, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close_save )
		self.Bind( wx.EVT_INIT_DIALOG, self.editor_init )
		self.m_listBox_name_exist.Bind( wx.EVT_LISTBOX, self.edit_exist_item )
		self.m_listBox_name_exist.Bind( wx.EVT_LISTBOX_DCLICK, self.view_item )
		self.m_bpButton_import_names.Bind( wx.EVT_BUTTON, self.import_names )
		self.m_button_clear.Bind( wx.EVT_BUTTON, self.clear_item )
		self.m_button_add.Bind( wx.EVT_BUTTON, self.add_item )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def close_save( self, event ):
		event.Skip()

	def editor_init( self, event ):
		event.Skip()

	def edit_exist_item( self, event ):
		event.Skip()

	def view_item( self, event ):
		event.Skip()

	def import_names( self, event ):
		event.Skip()

	def clear_item( self, event ):
		event.Skip()

	def add_item( self, event ):
		event.Skip()


###########################################################################
## Class MyDialogAddFace
###########################################################################

class MyDialogAddFace ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"接头器", pos = wx.DefaultPosition, size = wx.Size( 681,467 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_main_view = wx.StaticBitmap( self.m_scrolledWindow2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_bitmap_main_view, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow2.SetSizer( bSizer19 )
		self.m_scrolledWindow2.Layout()
		bSizer19.Fit( self.m_scrolledWindow2 )
		bSizer26.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline16 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer26.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetMinSize( wx.Size( 256,-1 ) )
		self.m_panel6.SetMaxSize( wx.Size( 192,-1 ) )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_info = wx.Notebook( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_BOTTOM )
		self.m_panel7 = wx.Panel( self.m_notebook_info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"左上角横坐标", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer22.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl_x_value = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer22.Add( self.m_textCtrl_x_value, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"左上角纵坐标", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer22.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl_y_value = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_textCtrl_y_value, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer22 )
		self.m_panel7.Layout()
		bSizer22.Fit( self.m_panel7 )
		self.m_notebook_info.AddPage( self.m_panel7, u"接头", False )
		self.m_panel14 = wx.Panel( self.m_notebook_info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"左上角横坐标", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer30.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_textCtrl_pic_x = wx.TextCtrl( self.m_panel14, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_textCtrl_pic_x, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"左上角纵坐标", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer30.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_textCtrl_pic_y = wx.TextCtrl( self.m_panel14, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_textCtrl_pic_y, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel14.SetSizer( bSizer30 )
		self.m_panel14.Layout()
		bSizer30.Fit( self.m_panel14 )
		self.m_notebook_info.AddPage( self.m_panel14, u"立绘坐标", True )
		self.m_panel_face = wx.Panel( self.m_notebook_info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_face = wx.StaticBitmap( self.m_panel_face, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_bitmap_face, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_face.SetSizer( bSizer23 )
		self.m_panel_face.Layout()
		bSizer23.Fit( self.m_panel_face )
		self.m_notebook_info.AddPage( self.m_panel_face, u"头预览", False )

		bSizer20.Add( self.m_notebook_info, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline18 = wx.StaticLine( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer20.Add( self.m_staticline18, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"导入的面部表情", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer20.Add( self.m_staticText6, 0, wx.ALL, 5 )

		m_listBox_import_faceChoices = []
		self.m_listBox_import_face = wx.ListBox( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_import_faceChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB )
		bSizer20.Add( self.m_listBox_import_face, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline23 = wx.StaticLine( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer20.Add( self.m_staticline23, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_checkBox_alpha = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"透明背景叠加", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		bSizer20.Add( self.m_checkBox_alpha, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_checkBox_minosity_size = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"以最小尺寸导出", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		bSizer20.Add( self.m_checkBox_minosity_size, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel6.SetSizer( bSizer20 )
		self.m_panel6.Layout()
		bSizer20.Fit( self.m_panel6 )
		bSizer26.Add( self.m_panel6, 1, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		bSizer17.Add( bSizer26, 1, wx.EXPAND, 5 )

		self.m_staticline19 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline19, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, u"NONE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_info.Wrap( -1 )

		bSizer27.Add( self.m_staticText_info, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline20 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer27.Add( self.m_staticline20, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"步长：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer27.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice_stepChoices = [ u"1", u"25", u"100", u"250" ]
		self.m_choice_step = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_stepChoices, 0 )
		self.m_choice_step.SetSelection( 0 )
		bSizer27.Add( self.m_choice_step, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer27.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_export = wx.Button( self, wx.ID_ANY, u"导出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_button_export, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer27, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.initial )
		self.m_bitmap_main_view.Bind( wx.EVT_ERASE_BACKGROUND, self.on_erase )
		self.m_bitmap_main_view.Bind( wx.EVT_LEFT_DCLICK, self.set_face_place )
		self.m_textCtrl_x_value.Bind( wx.EVT_MOUSEWHEEL, self.wheel_x )
		self.m_textCtrl_x_value.Bind( wx.EVT_TEXT, self.value_check_x )
		self.m_textCtrl_x_value.Bind( wx.EVT_TEXT_ENTER, self.x_value )
		self.m_textCtrl_y_value.Bind( wx.EVT_MOUSEWHEEL, self.y_wheel )
		self.m_textCtrl_y_value.Bind( wx.EVT_TEXT, self.value_check_y )
		self.m_textCtrl_y_value.Bind( wx.EVT_TEXT_ENTER, self.y_value )
		self.m_textCtrl_pic_x.Bind( wx.EVT_MOUSEWHEEL, self.px_wheel )
		self.m_textCtrl_pic_x.Bind( wx.EVT_TEXT, self.value_check_px )
		self.m_textCtrl_pic_y.Bind( wx.EVT_MOUSEWHEEL, self.py_wheel )
		self.m_textCtrl_pic_y.Bind( wx.EVT_TEXT, self.value_check_py )
		self.m_listBox_import_face.Bind( wx.EVT_LISTBOX, self.view_face )
		self.m_listBox_import_face.Bind( wx.EVT_LISTBOX_DCLICK, self.select_face )
		self.m_checkBox_alpha.Bind( wx.EVT_CHECKBOX, self.change_method )
		self.m_choice_step.Bind( wx.EVT_CHOICE, self.set_step )
		self.m_button_export.Bind( wx.EVT_BUTTON, self.export )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def initial( self, event ):
		event.Skip()

	def on_erase( self, event ):
		event.Skip()

	def set_face_place( self, event ):
		event.Skip()

	def wheel_x( self, event ):
		event.Skip()

	def value_check_x( self, event ):
		event.Skip()

	def x_value( self, event ):
		event.Skip()

	def y_wheel( self, event ):
		event.Skip()

	def value_check_y( self, event ):
		event.Skip()

	def y_value( self, event ):
		event.Skip()

	def px_wheel( self, event ):
		event.Skip()

	def value_check_px( self, event ):
		event.Skip()

	def py_wheel( self, event ):
		event.Skip()

	def value_check_py( self, event ):
		event.Skip()

	def view_face( self, event ):
		event.Skip()

	def select_face( self, event ):
		event.Skip()

	def change_method( self, event ):
		event.Skip()

	def set_step( self, event ):
		event.Skip()

	def export( self, event ):
		event.Skip()


###########################################################################
## Class MyDialogUpdateLocation
###########################################################################

class MyDialogUpdateLocation ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"更新本地化文件", pos = wx.DefaultPosition, size = wx.Size( 628,256 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"可选的本地化", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer26.Add( self.m_staticText11, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox_selectChoices = [ u"OSSSY152" ]
		self.m_listBox_select = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_selectChoices, 0 )
		bSizer26.Add( self.m_listBox_select, 1, wx.ALL, 5 )

		self.m_staticline25 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer26.Add( self.m_staticline25, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_load_file = wx.Button( self, wx.ID_ANY, u"加载文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button_load_file, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizer29.Add( bSizer26, 0, wx.EXPAND, 5 )

		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer29.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeCtrl_info = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT|wx.TR_TWIST_BUTTONS )
		bSizer27.Add( self.m_treeCtrl_info, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( bSizer27, 1, wx.EXPAND, 5 )

		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer29.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_apply_all = wx.Button( self, wx.ID_ANY, u"应用-全部", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button_apply_all, 0, wx.ALL, 5 )

		self.m_button_apply_new = wx.Button( self, wx.ID_ANY, u"应用-新增", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button_apply_new, 0, wx.ALL, 5 )

		self.m_button_apply_cover = wx.Button( self, wx.ID_ANY, u"应用-覆盖", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button_apply_cover, 0, wx.ALL, 5 )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button_cancel, 0, wx.ALL, 5 )


		bSizer29.Add( bSizer28, 0, wx.EXPAND, 5 )


		bSizer25.Add( bSizer29, 1, wx.EXPAND, 5 )

		self.m_staticline24 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer25.Add( self.m_staticline24, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_info.Wrap( -1 )

		bSizer25.Add( self.m_staticText_info, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer25 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_listBox_select.Bind( wx.EVT_LISTBOX_DCLICK, self.request_info )
		self.m_button_load_file.Bind( wx.EVT_BUTTON, self.load_file )
		self.m_button_apply_all.Bind( wx.EVT_BUTTON, self.apply_all )
		self.m_button_apply_new.Bind( wx.EVT_BUTTON, self.apply_new )
		self.m_button_apply_cover.Bind( wx.EVT_BUTTON, self.apply_cover )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def request_info( self, event ):
		event.Skip()

	def load_file( self, event ):
		event.Skip()

	def apply_all( self, event ):
		event.Skip()

	def apply_new( self, event ):
		event.Skip()

	def apply_cover( self, event ):
		event.Skip()

	def cancel( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog6
###########################################################################

class MyDialog6 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_KEY_DOWN, self.on_key_down )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_key_down( self, event ):
		event.Skip()


