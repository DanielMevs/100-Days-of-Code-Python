from tkinter import *

'''Grid and pack are incompatible with each other. You have to choose one or the other
Pack with stack components on top of each other
Grid allows you to specify where to place the component based on grid-based coordinates'''
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I AM a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# - Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click ME", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)



input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()