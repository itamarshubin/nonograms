from tkinter import *

class squre(Frame):
    def __init__(self,the_window,r,c,isf):
        super().__init__()
        self["width"]=30
        self["height"]=30
        self["highlightbackground"]="black"
        self["highlightthickness"]=1
        self["bg"]="white"
        self.row=r
        self.column=c
        self.isFill=isf
        def printLocation(Event):
            #print("the row is:"+ str(self.row)+ " and the column is:" +str(self.column))
            if not self.isFill:   
                self.isFill=TRUE
                self["bg"]="black"
            else:
                self.isFill=FALSE
                self["bg"]="white"


        self.bind("<Button-1>", printLocation)
    


root = Tk()
X=input("how many rows? ")
Y=input("how many columns? ")

#all the objects on the screen
Matrix = [[squre(root,0,0,FALSE) for x in range(int(X))] for y in range(int(Y))]
row_entrys=[Entry(root,width=2) for x in range(int(X))]
col_entrys=[Entry(root,width=2) for y in range(int(Y))]

#set the location of the entrys
col=0
for i in row_entrys:
    i.grid(row=0,column=col+1)
    col+=1
ro=0
for i in col_entrys:
    i.grid(row=ro+1,column=0)
    ro+=1

#set the location of the squares
ilen=0
for i in Matrix:
    jlen=0
    for j in i:
        j.row=ilen
        j.column=jlen
        j.grid(row=ilen+1,column=jlen+1)
        jlen+=1
    ilen+=1

#write the button function    
def test():
    for i in range(len(row_entrys)):    
        text=row_entrys[i].get()
        array=[]
        temp=""
        for j in text:
            if j!=',':
                temp=temp+j
            else:
                array.append(temp)
                temp=""
        array.append(temp)
        count=0
        index=0
        if array[0]=="":
            array[0]=-1
        for j in range(len(col_entrys)):
            if Matrix[j][i].isFill:
                count+=1
              #  print("in if:"+str(count))
            if (not Matrix[j][i].isFill) or (i==len(col_entrys)-1):
               # print("in else:"+str(count))
                if count!=0:
                    if count==int(array[index]):
                        index+=1
                        if index==len(array):
                            break
                            #j=len(col_entrys)
                            #print("finish one column")
                        count=0
                    else:
                        print("test fail")
                        return
        if array[0]!=-1 and index==0:
            print("test fail")
            return
    
    for i in range(len(col_entrys)):    
        text=col_entrys[i].get()
        array=[]
        temp=""
        for j in text:
            if j!=',':
                temp=temp+j
            else:
                array.append(temp)
                temp=""
        array.append(temp)
        count=0
        index=0
        if array[0]=="":
            array[0]=-1
        for j in range(len(row_entrys)):
            if Matrix[i][j].isFill:
                count+=1
              #  print("in if:"+str(count))
            if (not Matrix[i][j].isFill) or (i==len(row_entrys)-1):
               # print("in else:"+str(count))
                if count!=0:
                    #print("this is the value of the arry:"+str(array[index])+" and this is the count:"+str(count))
                    if count==int(array[index]):
                        index+=1
                        if index==len(array):
                            break
                            #j=len(row_entrys)
                            #print("finish one column")
                        count=0
                    else:
                        print("test fail")
                        return
        if array[0]!=-1 and index==0:
            print("test fail-empty")
            return
    print("test passed!")
                



#crete and set location of the button
testButton=Button(root,text="test",padx=100,pady=25,command=test)
testButton.grid(row=len(col_entrys)+1,columnspan=len(row_entrys))


root.mainloop()