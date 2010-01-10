import wx, wx.html
from wx import *

class jnet(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(640, 480))
		panel = wx.Panel(self, -1)
		global html
		html = wx.html.HtmlWindow(self)
		html.SetStandardFonts()
		html.SetSize((640,455))
		html.SetPosition((0,25))

		fileMenu = wx.Menu()
		fileMenu.Append(1, '&New Window\tCtrl+N', 'New Window')
		fileMenu.Append(2, 'New &Tab\tCtrl+T', 'New Tab')
		fileMenu.Append(3, 'Open &Location\tCtrl+L', 'Open Location')
		fileMenu.Append(4, '&Open FIle\tCtrl+O', 'Open File')
		fileMenu.Append(5, 'Close &Window\tCtrl+Shift+W', 'Close Window')
		fileMenu.Append(6, 'Close Tab\tCtrl+W', 'Close Tab')
		fileMenu.Append(7, 'Go\tEnter', 'Go')

		editMenu = wx.Menu()
		editMenu.Append(8, 'Cut\tCtrl+X', 'Cut')
		editMenu.Append(9, '&Copy\tCtrl+C', 'Copy')
		editMenu.Append(10, 'Paste\tCtrl+V', 'Paste')

		menuBar = wx.MenuBar()
		menuBar.Append(fileMenu, 'File')
		menuBar.Append(editMenu, 'Edit')
		self.SetMenuBar(menuBar)

		self.urlText = wx.TextCtrl(self, -1,'http://',(0,0),(400,24))

		self.Bind(wx.EVT_MENU, self.onGo, id=7)

	def onGo(self, event):
		url = self.urlText.GetLineText(0)
		html.LoadPage(url)


app = wx.App()
frame = jnet(None, -1, 'Jnet')
frame.Show(True)
app.MainLoop()
