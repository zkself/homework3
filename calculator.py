# -*- coding: utf-8 -*-
import wx
import wx.xrc
from calculate import *
import threading
import time
###########################################################################
# Class MyFrame1
###########################################################################
class MyFrame1 (wx.Frame):
    res = []
    creatvar = locals()
    eve = threading.Event()
    ratio = [0, 0]

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            600, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer1 = wx.GridBagSizer(10, 10)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.btnStart = wx.Button(self, wx.ID_ANY, u"开始答题")
        gbSizer1.Add(self.btnStart, span=(1, 1), pos=(1, 6))

        self.labTime = wx.StaticText(self, wx.ID_ANY, u"时间:")
        gbSizer1.Add(self.labTime, span=(1, 1), pos=(
            2, 0), flag=wx.EXPAND, border=3)

        self.labTime1 = wx.StaticText(self, wx.ID_ANY, u"0:0:0")
        gbSizer1.Add(self.labTime1, span=(1, 1),
                     pos=(2, 1), flag=wx.EXPAND, border=3)
        self.labRatio = wx.StaticText(self, wx.ID_ANY, u"1234")
        gbSizer1.Add(self.labRatio, span=(1, 1),
                     pos=(2, 3), flag=wx.EXPAND, border=3)
        self.btnNext = wx.Button(self, wx.ID_ANY, u"再来5题")
        gbSizer1.Add(self.btnNext, span=(1, 1), pos=(9, 3))

        self.btnPause = wx.Button(self, wx.ID_ANY, u"暂停")
        gbSizer1.Add(self.btnPause, span=(1, 1), pos=(9, 6))

        self.btnEnd = wx.Button(self, wx.ID_ANY, u"结束答题")
        gbSizer1.Add(self.btnEnd, span=(1, 1), pos=(9, 8))

        self.SetSizer(gbSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        
    def __del__(self):
        pass
app = wx.App(False)
frame = MyFrame1(None)
frame.Show(True)
app.MainLoop()