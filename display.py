from tkinter import *
import json


class squre(Frame):
    def __init__(self, the_window, r, c, isf):
        super().__init__()
        self["width"] = 30
        self["height"] = 30
        self["highlightbackground"] = "black"
        self["highlightthickness"] = 1
        self["bg"] = "white"
        self.row = r
        self.column = c
        self.isFill = isf

        def printLocation(Event):
            #print("the row is:"+ str(self.row)+ " and the column is:" +str(self.column))
            if not self.isFill:
                self.isFill = TRUE
                self["bg"] = "black"
            else:
                self.isFill = FALSE
                self["bg"] = "white"

        self.bind("<Button-1>", printLocation)

root = Tk()

with open('data.json') as f:
    data = json.load(f)
    X = len(data["rows"])
    Y = len(data["columns"])
    Matrix = [[squre(root, 0, 0, FALSE) for x in range(int(X))] for y in range(int(Y))]
    row_entrys = [Entry(root, width=4) for x in range(int(X))]
    col_entrys = [Entry(root, width=4) for y in range(int(Y))]

    for i in range(len(data["rows"])):

        row_entrys[i].insert(0,str(data["rows"][i]).strip('[]'))
    for i in range(len(data["columns"])):
        col_entrys[i].insert(0,str(data["columns"][i]).strip('[]'))
   
# set the location of the entrys
col = 0
for i in row_entrys:
    i.grid(row=0, column=col+1)
    col += 1
ro = 0
for i in col_entrys:
    i.grid(row=ro+1, column=0)
    ro += 1

# set the location of the squares
ilen = 0
for i in Matrix:
    jlen = 0
    for j in i:
        j.row = ilen
        j.column = jlen
        j.grid(row=ilen+1, column=jlen+1)
        jlen += 1
    ilen += 1

# write the button function

def check():
    passed = test()
    if (passed):
        print("you passed :)")
    else:
        print("you failed :(")

def test():
    for i in range(len(row_entrys)):
        text = row_entrys[i].get()
        array = text.split(",")
        array = list(filter(lambda a: a != "", array))
        count = 0
        index = 0
        for j in range(len(col_entrys)):
            if Matrix[j][i].isFill:
                count += 1
                if (index > (len(array)-1) or int(array[index]) < count):
                    print("fail 1 1")
                    return False
            elif (count != 0):
                if (count != int(array[index])):
                    print("fail 1 2")
                    return False
                count = 0
                index += 1
        if (count != 0 and count != int(array[index])):
            print("fail 1 3")
            return False
            #if the board is 
        if (count != 0):
            index +=1
        if (index != len(array)):
            print("fail 1 4")
            return False

    for i in range(len(col_entrys)):
        text = col_entrys[i].get()
        array = text.split(",")
        array = list(filter(lambda a: a != "", array))
        count = 0
        index = 0
        for j in range(len(row_entrys)):
            if Matrix[i][j].isFill:
                count += 1
                if (index > (len(array)-1) or int(array[index]) < count):
                    print("fail 2 1")
                    return False
            elif (count != 0):
                if (count != int(array[index])):
                    print("fail 2 2")
                    return False
                count = 0
                index += 1
        if (count != 0 and count != int(array[index])):
            print("fail 2 3")
            return False
            #if the board is 
        if (count != 0):
            index +=1
        if (index != len(array)):
            print(index)
            print(array)
            print("fail 2 4")
            return False

    return True


# crete and set location of the button
testButton = Button(root, text="test", padx=100, pady=25, command=check)
testButton.grid(row=len(col_entrys)+1, columnspan=len(row_entrys))

root.mainloop()
