# to do list app 
# list item  (sornyi item)
#     color, text 

# do do list item list 

# delete method 
# set, get method
# change color method

import tkinter as tk

def show_entry_fields():
    print("item1: %s\nitem2: %s\nitem3: %s" % (e1.get(), e2.get(), e3.get()))

master = tk.Tk()
tk.Label(master, text="item1").grid(row=0)
tk.Label(master, text="item2").grid(row=1)
tk.Label(master, text="item3").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()

class MyItem:
    def __init__(self, entry, color, size):
        self.__entry = entry
        self.__textColor = color
        self.__textSize = size
        self.__entryIsDone = False

    def getEntry(self):
        return self.__entry

    def getColor(self):
        return self.__textColor
    
    def getSize(self):
        return self.__textSize

    def isDone(self):
        return self.__entryIsDone

    # def viewEntry(self):
    #     print(self.__entry)

    def toggleDone(self):
        self.__entryIsDone = not self.__entryIsDone

item1 = MyItem("tej", "black", 12)
item2 = MyItem("vaj", "green", 10)
item3 = MyItem("víz", "green", 10)


item3.getEntry()
item2.getColor()
item1.getSize()
item1.isDone()
item1.toggleDone()


print("item1.entryIsDone ",item1.isDone())

item1.toggleDone()

# print("item1.getColor() ", item1.getColor())
# print("item2.viewEntry() ", item2.viewEntry())
# print("item1.entryIsDone ", item1.entryIsDone)
