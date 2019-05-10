from tkinter import *

print("importuota paste")

def rClicker(e):
    ''' right click context menu for all Tk Entry and Text widgets
    '''

    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')

        def rClick_Cut(e):
            e.widget.event_generate('<Control-zodziai>')

        def rClick_Paste(e):
            e.widget.event_generate('<Control-v>')

        e.widget.focus()

        nclst=[
               (' Cut', lambda e=e: rClick_Cut(e)),
               (' Copy', lambda e=e: rClick_Copy(e)),
               (' Paste', lambda e=e: rClick_Paste(e)),
               ]

        rmenu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

    except TclError:
        print(' - rClick menu, something wrong')
        pass

    return "break"

def rClickbinder(r):

    try:
        for b in [ 'Text', 'Entry', 'Listbox', 'Label']: #
            r.bind_class(b, sequence='<Button-3>',
                         func=rClicker, add='')
    except TclError:
        print(' - rClickbinder, something wrong')
        pass

if __name__ == '__main__':
    master = Tk()

    ent = Entry(master, width=60)
    # ent.pack(anchor="w")
    ent.pack()

    #bind context menu to a specific element
    ent.bind('<Button-3>',rClicker, add='')
    #or bind it to any Text/Entry/Listbox/Label element
    #rClickbinder(master)

    # boksas = Text(master, height=30, width=30)
    # boksas.pack(anchor="e")
    #
    # boksas.bind('<Button-3>',rClicker, add='')

    master.mainloop()
