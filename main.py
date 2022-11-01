
from sys import set_coroutine_origin_tracking_depth
from tkinter import *
from turtle import width
from data import words

# main:
window = Tk()
window.title("Българо-Ромски речник")
# window.geometry("600x300")
#label:
text = Label (window,text="Напишете думата която искате да преведете :")
text.grid(row=0 ,column=0,sticky=W,pady=5 )



#entry text
en_text = Entry(window,width=42*2)
en_text.grid(row=1,column=0,sticky=W)



#prevod function
def click():
    entered_text=en_text.get() # colect the enter text
    prevod.delete(0.0, END) # delete the text
    try:
        definition = words[entered_text.title()]
    except:
        definition = "Съжеляваме не можем да преведем тази дума"
    prevod.insert(END, definition)   



#button:
btn = Button(window, text="ПРЕВОД",width=36*2,border=0,command=click,)
btn.grid(row=2,column=0,sticky=W)

#text box
prevod = Text(window,wrap=WORD ,width=63,height=1)
prevod.grid(row=3,column=0,sticky=W)


window.mainloop()