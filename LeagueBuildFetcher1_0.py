import webbrowser
from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("League Build Fetcher")

#Adjust window size
window.geometry('640x200')

window.resizable(False,False)

f1 = Frame(window)


def clicked(event=None):
	Champname = txt.get()
	if(selected.get() == 1):
		role = "top"
	elif(selected.get() == 2):
		role = "middle"
	elif(selected.get() == 3):
		role = "jungle"
	elif(selected.get() == 4):
		role = "adc"
	elif(selected.get() == 5):
		role = "support"
	else:
		role = ""

	webbrowser.open('https://u.gg/lol/champions/' + Champname + '/build?role=' + role)

def on_close():
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)


lbl1 = Label(window, text = "                     ", font=("Arial", 20))
#Position of Label
lbl1.grid(column = 0, row = 0)

lbl = Label(window, text = "Enter Champion name:", font=("Arial", 20))
#Position of Label
lbl.grid(column = 1, row = 0)

lbl1 = Label(window, text = "                     ", font=("Arial", 20))
#Position of Label
lbl1.grid(column = 0, row = 1)

txt = Entry(window,width= 30)#,state='disabled')
txt.grid(column=1,row=1)
txt.focus()

btn = Button(window, text="Find my Build!", command=clicked)
btn.grid(column=1,row=2)

selected = IntVar()

top = Radiobutton(f1,text='Top', value=1, variable = selected)
middle = Radiobutton(f1,text='Middle', value=2, variable = selected)
jungle = Radiobutton(f1,text='Jungle', value=3, variable = selected)
bottom = Radiobutton(f1,text='Bottom', value=4, variable = selected)
support = Radiobutton(f1,text='Support', value=5, variable = selected)


f1.grid(column=1,row=3,sticky="nsew")


top.pack(side="left")
middle.pack(side="left")
jungle.pack(side="left")
bottom.pack(side="left")
support.pack(side="left")

window.bind('<Return>', clicked)

exit_btn = Button(window, text="Exit", command=clicked)


#Displays Window
window.mainloop()
