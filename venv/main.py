import tkinter
from tkinter import *

if __name__ == '__main__':
    main_screen = Tk()
    main_screen.title("TK-Inter-Calculator-Test")
    main_screen.configure(bg="#D6D6D6")
    main_screen.geometry("400x600")  # set the relation of the screen

    # configuration of the column and row weight
    main_screen.grid_columnconfigure(0, weight=1)
    main_screen.grid_columnconfigure(1, weight=1)
    main_screen.grid_columnconfigure(2, weight=1)
    main_screen.grid_columnconfigure(3, weight=1)
    main_screen.grid_rowconfigure(0, weight=1)
    main_screen.grid_rowconfigure(1, weight=1)
    main_screen.grid_rowconfigure(2, weight=1)
    main_screen.grid_rowconfigure(3, weight=1)
    main_screen.grid_rowconfigure(4, weight=1)
    main_screen.grid_rowconfigure(5, weight=1)

    # label
    label = tkinter.Label(
        main_screen,
        bg="#D6D6D6",
        text="0",
        anchor="e",
        font="consolas 30 bold",
        width=4,
        fg="#4C4C4C"
    )

    # buttons
    number_0 = tkinter.Button(
        main_screen,
        text="0",
        font="consolas 20 bold",
        width=4,
        bg="#4C4C4C",
        fg="white"
    )
    number_1 = tkinter.Button(
        main_screen,
        text="1",
        font="consolas 20 bold",
        width=4,
        bg="#4C4C4C",
        fg="white"
    )
    number_2 = tkinter.Button(
        main_screen,
        text="2",
        font="consolas 20 bold",
        width=4,
        bg="#4C4C4C",
        fg="white"
    )
    number_3 = tkinter.Button(
        main_screen,
        text="3",
        font="consolas 20 bold",
        width=4,
        bg="#4C4C4C",
        fg="white"
    )
    number_4 = tkinter.Button(
        main_screen,
        text="4",
        font="consolas 20 bold",
        width=4,
        bg="#4C4C4C",
        fg="white"
    )
    number_5 = tkinter.Button(
        main_screen,
        text="5",
        font="consolas 20 bold",
        width=4,
        bg="#4C4C4C",
        fg="white"
    )
    number_6 = tkinter.Button(
        main_screen,
        text="6",
        font="consolas 20 bold",
        width=4,
        bg="#4C4C4C",
        fg="white"
    )
    number_7 = tkinter.Button(
        main_screen,
        text="7",
        font="consolas 20 bold",
        width=4,
        bg="#4C4C4C",
        fg="white"
    )
    number_8 = tkinter.Button(
        main_screen,
        text="8",
        font="consolas 20 bold",
        width=4,
        bg="#4C4C4C",
        fg="white"
    )
    number_9 = tkinter.Button(
        main_screen,
        text="9",
        font="consolas 20 bold",
        width=4,
        bg="#4C4C4C",
        fg="white"
    )

    # Signs
    equals = tkinter.Button(
        main_screen,
        text="=",
        font="consolas 20 bold",
        width=4,
        bg="#9B9A9A",
        fg="#FFDD00"
    )
    plus = tkinter.Button(
        main_screen,
        text="+",
        font="consolas 20 bold",
        width=4,
        bg="#9B9A9A",
        fg="#FFDD00"
    )
    less = tkinter.Button(
        main_screen,
        text="-",
        font="consolas 20 bold",
        width=4,
        bg="#9B9A9A",
        fg="#FFDD00"
    )
    multiplication = tkinter.Button(
        main_screen,
        text="×",
        font="consolas 20 bold",
        width=4,
        bg="#9B9A9A",
        fg="#FFDD00"
    )
    division = tkinter.Button(
        main_screen,
        text="÷",
        font="consolas 20 bold",
        width=4,
        bg="#9B9A9A",
        fg="#FFDD00"
    )

    # buttons to put parentheses and point
    parentheses = tkinter.Button(
        main_screen,
        text="()",
        font="consolas 20 bold",
        width=4,
        bg="#9B9A9A",
        fg="#FFDD00"
    )
    point = tkinter.Button(
        main_screen,
        text=".",
        font="consolas 20 bold",
        width=4,
        bg="#9B9A9A",
        fg="#FFDD00"
    )

    # buttons to clear all and delete the las insert
    clear = tkinter.Button(
        main_screen,
        text="C",
        font="consolas 20 bold",
        width=4,
        bg="#9B9A9A",
        fg="#FFDD00"
    )

    photo = PhotoImage(file="delete.png") # Creating a photoimage object to use image
    photo_image = photo.subsample(15, 15) # Resizing image to fit on button

    erase = tkinter.Button(
        main_screen,
        image=photo_image,
        font="consolas 20 bold",
        width=4,
        bg="#9B9A9A",
        fg="#FFDD00"
    )

    label.grid(row=0, column=0, sticky="nsew", columnspan=4)

    number_0.grid(row=5, column=1, sticky="nsew", pady=2, padx=2)
    number_1.grid(row=4, column=0, sticky="nsew", pady=2, padx=2)
    number_2.grid(row=4, column=1, sticky="nsew", pady=2, padx=2)
    number_3.grid(row=4, column=2, sticky="nsew", pady=2, padx=2)
    number_4.grid(row=3, column=0, sticky="nsew", pady=2, padx=2)
    number_5.grid(row=3, column=1, sticky="nsew", pady=2, padx=2)
    number_6.grid(row=3, column=2, sticky="nsew", pady=2, padx=2)
    number_7.grid(row=2, column=0, sticky="nsew", pady=2, padx=2)
    number_8.grid(row=2, column=1, sticky="nsew", pady=2, padx=2)
    number_9.grid(row=2, column=2, sticky="nsew", pady=2, padx=2)

    equals.grid(row=4, column=3, sticky="nsew", rowspan=2, pady=2, padx=2)
    plus.grid(row=3, column=3, sticky="nsew", pady=2, padx=2)
    less.grid(row=2, column=3, sticky="nsew", pady=2, padx=2)
    multiplication.grid(row=1, column=2, sticky="nsew", pady=2, padx=2)
    division.grid(row=1, column=1, sticky="nsew", pady=2, padx=2)

    point.grid(row=5, column=0, sticky="nsew", pady=2, padx=2)
    parentheses.grid(row=5, column=2, sticky="nsew", pady=2, padx=2)

    clear.grid(row=1, column=0, sticky="nsew", pady=2, padx=2)
    erase.grid(row=1, column=3, sticky="nsew", pady=2, padx=2)

    main_screen.mainloop()