import tkinter as tk
from tkinter import ttk

def main():
    app = Application()
    app.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__() 
        self.title("RSA cryptography")

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)
        self.columnconfigure(2,weight=1)
        self.rowconfigure(0,weight=1)

        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        frame2 = InputForm(self)                                     
        frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        frame3 = InputForm(self)
        frame3.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew")

        self.entry.bind("<Return>", self.add_to_list)

        self.entry_btn = ttk.Button(self, text="Add", command=self.add_to_list)
        self.entry_btn.grid(row=0, column=1)

        self.clear_btn = ttk.Button(self, text="Clear", command=self.clear_list)
        self.clear_btn.grid(row=0, column=2)

        self.text_lists = tk.Listbox(self)
        self.text_lists.grid(row=1, column=0, columnspan=3, sticky="nsew")

    def add_to_list(self, event=None):
        text = self.entry.get()
        if text:
            self.text_lists.insert(tk.END, text)
            self.entry.delete(0, tk.END)
    def clear_list(self):
        self.text_lists.delete(0,tk.END)





if __name__ == "__main__":
    main()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 root = tk.Tk()
 root.title("RSA App")

 def add_to_list(event="None"):
     text = entry.get()
     text2 = entry2.get()
     if text:
         text_lists.insert(tk.END, text)
         entry.delete(0, tk.END)
     elif text2:
         text_lists2.insert(tk.END, text2)
         entry2.delete(0, tk.END)

 root.columnconfigure(0,weight=1)
 root.columnconfigure(1,weight=3)
 root.rowconfigure(0,weight=1)

 frame = ttk.Frame(root)
 frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

 frame.columnconfigure(0, weight=1)
 frame.rowconfigure(1, weight=1)

 entry = ttk.Entry(frame)
 entry.grid(row=0,column=0,sticky="ew")

 entry.bind("<Return>", add_to_list)

 entry_btn = ttk.Button(frame, text = "Add",command=add_to_list)
 entry_btn.grid(row=0,column=1)




 text_lists = tk.Listbox(frame)
 text_lists.grid(row=1,column=0,columnspan=15, sticky="nsew")

 #kolejny frame

 frame2 = tk.Frame(root)
 frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

 frame2.columnconfigure(0, weight=1)
 frame2.columnconfigure(1, weight=0)  # Btn nie musi mieć dużej wagi
 frame2.rowconfigure(0, weight=0)  # Wiersz na Entry
 frame2.rowconfigure(1, weight=1)  # Wiersz na Listbox, rozciąga się

 entry2 = tk.Entry(frame2)
 entry2.grid(row=0,column=0,sticky="ew")

 entry2.bind("<Return>", add_to_list)

 entry_btn2 = tk.Button(frame2, text = "Add",command=add_to_list)
 entry_btn2.grid(row=0,column=1)

 text_lists2 = tk.Listbox(frame2)
 text_lists2.grid(row=1,column=0,columnspan=15, sticky="nsew")





 #def on_click():
 #    print("testing")
 #    a = 5
 #    b = 3
 #    lbl.config(text=f"Your score is {a*b}", background="yellow")
 #
 #lbl = tk.Label(root, text="Label")
 #lbl.grid(row=5, column=5)
 ##
 #btn = tk.Button(root, text="Click me!", command=on_click)
 #btn.grid(row=6, column=6)
 #
 root.mainloop()