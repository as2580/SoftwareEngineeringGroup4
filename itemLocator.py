import tkinter 

class itemLocator_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Search")

        button = tkinter.Button(self,text=u"Enter",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="black",bg="lightgrey")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        

        self.grid_columnconfigure(0,weight=2)
        self.resizable(True,False)
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        
        
    def OnButtonClick(self):
        self.labelVariable.set( self.entryVariable.get())

    def OnPressEnter(self,event):
        self.labelVariable.set( self.entryVariable.get())
        

if __name__ == "__main__":
    function= itemLocator_tk(None)
    function.title('Item Locator')
    function.mainloop()

