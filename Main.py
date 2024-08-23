from tkinter import*

#================================
def btn9(number):
    display.insert(END,number)

def btn8(number):
    display.insert(END,number)

def btn7(number):
    display.insert(END,number)

def btn6(number):
    display.insert(END,number)

def btn5(number):
    display.insert(END,number)

def btn4(number):
    display.insert(END,number)

def btn3(number):
    display.insert(END,number)

def btn2(number):
    display.insert(END,number)

def btn1(number):
    display.insert(END,number)

def btnplus(number):
    display.insert(END,number)



def answer():
    getvalue = display.get()
    resalt =eval(answer)
    display.delete(0,END)
    display.insert(resalt)


#================================
root =Tk()
root.title("Calculator")
root.geometry("300x300")
root.config(bg="orange")

display = Entry(root,font('Arial',23,'bold') width=25)
display.grid(row=0, coloumn=0 ,padx=9 ,pady=4, coloumnspan=4) #pad --> x and y margin

b9 = button(root,text='9', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE, command=Lambda :btn9('9'))
b9.grid(row=1,coloumn=0)

b8 = button(root,text='8', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn8('8'))
b8.grid(row=1,coloumn=1)

b7 = button(root,text='7', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn7('7'))
b7.grid(row=1,coloumn=2)

bplus = button(root,text='+', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btnplus('+'))
bplus.grid(row=1,coloumn=3)



b6 = button(root,text='6', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn6('6'))
b6.grid(row=2,coloumn=0 ,pady=5)

b5 = button(root,text='5', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn5('5'))
b5.grid(row=2,coloumn=1)

b4 = button(root,text='4', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn4('4'))
b4.grid(row=2,coloumn=2)

bmin = button(root,text='-', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btnmin('-'))
bmin.grid(row=2,coloumn=3)



b3 = button(root,text='3', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn3('3'))
b3.grid(row=3,coloumn=0 ,pady=5)

b2 = button(root,text='2', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn2('2'))
b2.grid(row=3,coloumn=1)

b1 = button(root,text='1', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn1('1'))
b1.grid(row=3,coloumn=2)

bmax = button(root,text='X', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btnmax('*'))
bmax.grid(row=3,coloumn=3)


b0 = button(root,text='0', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn1('0'))
b0.grid(row=4,coloumn=0)

bdot = button(root,text='.', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn1('.'))
bdot.grid(row=4,coloumn=1)

bclear = button(root,text='1', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btn1('1'))
bclear.grid(row=4,coloumn=2)

bdev = button(root,text='/', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=Lambda :btndev('/'))
bdev.grid(row=4,coloumn=3)



bsum = button(root,text='/', font('Arial',10,'bold') width=4, cursor='hand2', relief=GROOVE command=answer)
bsum.grid(row=5,coloumn=0, coloumnspan=4,)









root.mainloop()
