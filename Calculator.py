from tkinter import *
from tkinter.ttk import Frame, Label, Entry

class Calculator:
        def __init__(self, master):
                self.master = master
                master.title("Calc")

                self.total = 0
                self.last = 0
                self.digite = 0
                self.operation = 0
                
                self.entry_val = IntVar()
                self.entry_val.set(self.total)

                self.label = Label(master)
                self.label.grid(rowspan=5, columnspan=4, sticky=N)

                self.screen = Entry(master, textvariable=self.entry_val)
                self.screen.grid(row=0, columnspan=4)
                
                self.one = Button(master, text="1", command=lambda:self.put(1))
                self.one.grid(row=1, column=0)

                self.two = Button(master, text="2", command=lambda:self.put(2))
                self.two.grid(row=1, column=1)

                self.three = Button(master, text="3", command=lambda:self.put(3))
                self.three.grid(row=1, column=2)

                self.plus = Button(master, text="+", command=lambda:self.exec("add"))
                self.plus.grid(row=1, column=3)

                self.four= Button(master, text="4", command=lambda:self.put(4))
                self.four.grid(row=2, column=0)

                self.five = Button(master, text="5", command=lambda:self.put(5))
                self.five.grid(row=2, column=1)

                self.six = Button(master, text="6", command=lambda:self.put(6))
                self.six.grid(row=2, column=2)

                self.minus = Button(master, text="-", command=lambda:self.exec("subtract"))
                self.minus.grid(row=2, column=3)

                self.seven = Button(master, text="7", command=lambda:self.put(7))
                self.seven.grid(row=3, column=0)

                self.eight = Button(master, text="8", command=lambda:self.put(8))
                self.eight.grid(row=3, column=1)

                self.nine = Button(master, text="9", command=lambda:self.put(9))
                self.nine.grid(row=3, column=2)

                self.multi = Button(master, text="*", command=lambda:self.exec("multi"))
                self.multi.grid(row=3, column=3)

                self.reset = Button(master, text="CE", command=lambda:self.update("reset"))
                self.reset.grid(row=4, column=0)

                self.oh = Button(master, text="0", command=lambda:self.put(0))
                self.oh.grid(row=4, column=1)

                self.equals = Button(master, text="=", command=lambda:self.update("equals"))
                self.equals.grid(row=4, column=2)

                self.div = Button(master, text="/", command=lambda:self.exec("div"))
                self.div.grid(row=4, column=3)
        
        def put(self, d):
                self.last = str(self.last)
                self.digite = str(d)
                self.last += self.digite        
                self.last = int(self.last)
                self.entry_val.set(self.last)

        def exec(self, m):
                if (self.last):
                        if not (self.operation):
                                self.total = self.last
                                self.operation = m
                                self.last = 0
                        else:
                                o = self.operation  
                                self.update("equals")
                                self.operation = o 
                                self.printvars()
                else:
                        self.update("reset")
                        self.total = "Err"
                        self.printvars()

                self.entry_val.set(self.total)
                
        def update(self, method):
                if method == "reset":
                        self.total = 0
                        self.last = 0
                        self.operation = 0
                        self.prevop = 0            
                elif method == "equals":
                        if (self.operation):
                                if self.operation == "add":
                                        self.total += self.last
                                elif self.operation == "subtract":
                                        self.total -= self.last
                                elif self.operation == "multi":
                                        self.total *= self.last
                                elif self.operation == "div":
                                        if not self.last:
                                                self.total = ""
                                        else:
                                                self.total /= self.last      
                        else:
                                if not self.total:
                                        self.total = self.last
                                else:
                                        self.total = "Err"
                        self.operation = 0
                        self.last = 0           
                else:
                	    self.update("reset")
                	    self.total = "Err"
                
                self.entry_val.set(self.total) 
                
root = Tk()                
my_gui = Calculator(root)
root.mainloop()
