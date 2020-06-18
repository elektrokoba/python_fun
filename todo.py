# to do list app 
# list item  (sornyi item)
#     color, text 

# do do list item list 

# delete method 
# set, get method
# change color method

import tkinter

class MyItems:
    def __init__(self, entry, color, size, isdone):
        self.entry = entry
        self.textColor = color
        self.textSize = size
        self.entryIsDone = bool(isdone)

    def getColor(self):
        return self.textColor
    
    def getSize(self):
        return self.getSize

    def viewEntry(self):
        print(self.entry)

    def toggleDone(self, entry):
        self.entryIsDone = True

item1 = MyItems("tej", "black", 12, False)
item2 = MyItems("vaj", "green", 10, True)

print("item1.entryIsDone ",item1.entryIsDone)

item1.toggleDone(item1)

print("item1.getColor() ", item1.getColor())
print("item2.viewEntry() ", item2.viewEntry())
print("item1.entryIsDone ", item1.entryIsDone)
