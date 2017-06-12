from Tkinter import *
import tkMessageBox
root=None
count=0
deCount=0
link=[[] for i in range(3)] 
sym="."
def addButton(root,sideToPack,i,j):
    global count
    global link
    global sym
    button=Button(root,text=sym,height=3,width=3,command=lambda:deactivate(button,i,j))
    button.pack(side=sideToPack)
    #print str(i)+" "+str(j)
    #link[i][j]=button   #This produces an IndexError! why?
    link[count/3].append(button)
    count+=1
def resetButton(root):
    button=Button(root,text="Reset",command=reactivate)
    button.pack()
def deactivate(button,row,col):
    global sym
    global deCount 
    
    if deCount%2 == 0:
        sym='X'
    else:
        sym='O'    
    button.config(text=sym,state='disabled')
    
    if CheckVictory(row,col)==True:
        tkMessageBox.showinfo("Game Over!", "You won!")
        root.destroy() 
    deCount+=1
def CheckVictory(x,y):
    global link
    #check if previous move caused a win on vertical line 
    if link[0][y]['text'] == link[1][y]['text'] == link [2][y]['text'] != '.' :
        return True

    #check if previous move caused a win on horizontal line 
    if link[x][0]['text'] == link[x][1]['text'] == link [x][2]['text'] != '.' :
        return True

    #check if previous move was on the main diagonal and caused a win
    if x == y and link[0][0]['text'] == link[1][1]['text'] == link [2][2]['text'] != '.' :
        return True

    #check if previous move was on the secondary diagonal and caused a win
    if x + y == 2 and link[0][2]['text'] == link[1][1]['text'] == link [2][0]['text'] != '.' :
        return True

    return False                     


def reactivate():    
    global link
    global sym
    global deCount
    sym="."
    for i in range(3):
        for j in range(3):
            link[i][j].config(text=sym,state='normal')
    deCount=0


    
def main():
    global root
    root=Tk()
    root.title("Tic-Tac-Toe")
    for i in range(3):
        frame=Frame(root)
        for j in range(3):
            addButton(frame,LEFT,i,j) 
        frame.pack()
    bottomFrame=Frame(root)
    bottomFrame.pack(side=BOTTOM)
    resetButton(bottomFrame)            
    root.mainloop()
main()        
