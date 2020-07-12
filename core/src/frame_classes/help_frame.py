import os

import wx
import wx.html2

from core.src.frame_classes.design_frame import MyFrameHelp


class HelpPageFrame(MyFrameHelp):
    def __init__(self, path):
        super(HelpPageFrame, self).__init__(None)

        self.path = path
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.help_page: wx.html2.WebView = wx.html2.WebView.New(self.m_scrolledWindow_bg)
        sizer.Add(self.help_page, 1, wx.EXPAND, 10)
        self.m_scrolledWindow_bg.SetSizer(sizer)

        self.target = os.path.join(self.path, "core/assets/help.html")
        self.help_page.LoadURL(self.target)

        self.is_busy = False
        self.url = ""
        self.title = title = self.help_page.GetCurrentTitle()
        self.SetTitle(title)
        self.in_init = True

    def redo_page(self, event):
        pass
        # if self.help_page.CanRedo():
        #    self.help_page.Redo()

    def undo_page(self, event):
        pass
        # if self.help_page.CanUndo():
        #    self.help_page.Undo()

    def reload(self, event):
        self.help_page.Reload()

    def stop(self, event):
        self.help_page.Stop()

    def use_target_url(self, event):
        pass

    # url = event.GetString()
    # self.help_page.LoadURL(url)

    def go_back(self, event):
        pass
        # if self.help_page.CanGoBack():
        #    self.help_page.GoBack()

    def go_forword(self, event):
        pass
        # if self.help_page.CanGoForward():
        #    self.help_page.GoForward()
