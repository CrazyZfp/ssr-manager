import tkinter as tk

window = tk.Tk()
window.geometry("500x500")

lb = tk.Listbox(window, bg='white')

list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'aaa1')
lb.insert(2, 'aaa2')
lb.pack()
window.mainloop()
