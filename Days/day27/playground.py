from tkinter import *

def add(*args):
    # print(args)
    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6, 7, 8, 9, 2, 4))


def calculate(n, **kwargs):
    print(kwargs)
    # print(kwargs["add"])
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Lamborghini", model="Urus")
print(my_car.model)

# - Entry

input = Entry(width=10)
input.pack()
print(input.get())


# - Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")

print(text.get("1.0", END))
text.pack()

def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# - Scale
# - Called with current scale value.

def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# - Checkbox
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# - Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# - Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "pear", "orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


#############################

window.mainloop()