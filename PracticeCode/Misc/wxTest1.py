import wx

class bucky(wx.Frame):

        def __init__(self,parent,id):
            wx.frame.__init__(self,parent,id,'Frame aka window', size=(300,200))

if __name__=='__main__':
        app=wx.PySimipleApp()
        frame=bucky(parent=None, id=-1)
        frame.Show()
         
