import random
import tkinter
from tkinter.font import Font

# initializing the window
window = tkinter.Tk()
window.title("Coin Flipper")
window.attributes('-fullscreen', True)

# Defining the Font
bigFont = Font(window, family='Roboto Bold', size=56, weight='bold', )

# Setting background
canvas = tkinter.Canvas(window, width=1600, height=1024, bg='#261C2C')
canvas.pack()

# Text using Label
flip1 = tkinter.Label(window, text="FLIP THE COIN", font=bigFont, bg='#261C2C', fg='white').place(x=475, y=38)
flip2 = tkinter.Label(window, text="TIMES", font=bigFont, bg='#261C2C', fg='white').place(x=640, y=238)
flip3 = tkinter.Label(window, text="AND GET HEADS", font=bigFont, bg='#261C2C', fg='white').place(x=475, y=512)
flip4 = tkinter.Label(window, text="TIMES", font=bigFont, bg='#261C2C', fg='white').place(x=640, y=712)

# tkinter variables initialize
entryVar = tkinter.StringVar()
tkPercentvar = tkinter.StringVar()

# Entry box initialize and place
number_entry = tkinter.Entry(window, textvariable=entryVar, bg='#E63E6D', borderwidth=0, justify='center', width=15,
                             font=('Norican', 50, 'normal'))
number_entry.place(x=450, y=135)


# Class for coin flip
def class_coin():
    loopNumber = int(number_entry.get())
    headsTracker = 0
    if (loopNumber > 0):
        for loopTracker in range(1, loopNumber + 1):
            randomInt = random.randint(0, 1)
            if (randomInt == 1):
                headsTracker += 1
        if (headsTracker == 0):
            percent = "0%"
        else:
            percent = headsTracker / loopNumber * 100
            percent = percent * (10 ** 6)
            percent = percent // 1
            percent = percent / (10 ** 6)
            percent = str(percent)
            percent = percent + "%"
    else:
        percent = "Enter a positive Integer"

    tkPercentvar.set(percent)


# Output box intiialize and place
number_output = tkinter.Label(window, textvariable=(tkPercentvar), bg='#E63E6D', borderwidth=0, justify='center',
                              width=16, font=('Norican', 50, 'normal'))
number_output.place(x=455, y=612)

# Run button initialize and place
runButton = tkinter.Button(window, text="Flip", bg='#8FD6E1', borderwidth=0, justify='center', width=12, height=-2,
                           command=class_coin, font=('Norican', 50, 'bold'))
runButton.place(x=520, y=330)

# Blank labels for adjusting button size
blank_label = tkinter.Label(window, text=' ', bg='#261C2C', borderwidth=0, justify='center', width=70,
                            font=('calibre', 10, 'bold'))
blank_label.place(x=520, y=330)
blank_label1 = tkinter.Label(window, text=' ', bg='#261C2C', borderwidth=0, justify='center', width=70,
                             font=('calibre', 10, 'bold'))
blank_label1.place(x=520, y=475)


# Class for setting character limit in Entry Box
def character_limit(entryVar):
    if len(entryVar.get()) > 6:
        entryVar.set(entryVar.get()[:-1])


# Tracing the entry widget and running the character limit class
entryVar.trace("w", lambda *args: character_limit(entryVar))

# Running the window
window.mainloop()


