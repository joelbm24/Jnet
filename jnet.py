import wx, wx.html
from wx import *

class jnet(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(640, 480))
		global html
		html = wx.html.HtmlWindow(self)
		html.SetStandardFonts()
		html.SetSize((640,430))
		html.SetPosition((0,25))
		html.LoadPage('file:///home/joel/Python/wx/Jnet/home.html')

		fileMenu = wx.Menu()
		fileMenu.Append(1, '&New Window\tCtrl+N', 'New Window')
		fileMenu.Append(2, 'New &Tab\tCtrl+T', 'New Tab')
		fileMenu.Append(3, '&Open File\tCtrl+O', 'Open File')
		fileMenu.Append(4, 'Close &Window\tCtrl+Shift+W', 'Close Window')
		fileMenu.Append(5, 'Close Tab\tCtrl+W', 'Close Tab')
		fileMenu.Append(6, 'Go\tEnter', 'Go')

		editMenu = wx.Menu()
		editMenu.Append(7, 'Cut\tCtrl+X', 'Cut')
		editMenu.Append(8, '&Copy\tCtrl+C', 'Copy')
		editMenu.Append(9, 'Paste\tCtrl+V', 'Paste')

		menuBar = wx.MenuBar()
		menuBar.Append(fileMenu, 'File')
		menuBar.Append(editMenu, 'Edit')
		self.SetMenuBar(menuBar)

		self.urlText = wx.TextCtrl(self, -1,'http://',(0,0),(640,24))

		self.Bind(wx.EVT_MENU, self.onOpen, id=3)
		self.Bind(wx.EVT_MENU, self.onGo, id=6)

	def onGo(self, event):
		url = self.urlText.GetLineText(0)
		html.LoadPage(url)
	def onOpen(self, event):
		fileOpen = wx.FileDialog(self, "Open a file",'.','', 'All Files|**| Python (*.py)|*.py', wx.OPEN)
		fileOpen.ShowModal()
		global filePath
		filePath = fileOpen.GetPath()
		html.LoadPage(fileOpen.GetPath())

app = wx.App()
frame = jnet(None, -1, 'Jnet')
frame.Show(True)
app.MainLoop()
