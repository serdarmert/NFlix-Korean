import json
from tkinter import BOTH, RIGHT, Scrollbar, Tk,Text,Listbox
from tkinter.ttk import PanedWindow


root = Tk()

with open('kore_list.json', 'r') as handle:
    koreler = json.load(handle)

#koreler = json.dumps(koreler, indent=4, sort_keys=True)
root.resizable(False,False)
root.title("NetFlix Kore Filmleri")
root.geometry("500x500")
myPanel = PanedWindow()
myPanel.place(x=1,y=1,width=200,height=500)
liste = Listbox(myPanel, width=30, height=30)

scroll = Scrollbar(myPanel)
scroll.pack(side=RIGHT,fill=BOTH)



for x in range(0,len(koreler["Kore"])-1):
    liste.insert(x+1,koreler["Kore"][x]["Movie Name"])

liste.config(yscrollcommand=scroll.set)
liste.place(x=10, y=1)
scroll.config(command=liste.yview)



root.mainloop()