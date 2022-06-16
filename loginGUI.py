import tkinter as tk

# Checks
def passChecks():
    if(str(passwordTk.get()) == 'tkinterpain'):
        for widgets in window.winfo_children():
            widgets.destroy()
        canvas = tk.Canvas(window, width=screen_width, height=screen_height, bg='#261C2C')
        canvas.pack()
        ConfirmationLabel = tk.Label(window, text=str(userNameTk.get()), bg='#261C2C', fg='white',
                                font=('Norican', 50, 'normal')).place(x=screen_width * 0.2278,
                                y=screen_height * 0.0381)

# Initializing
window = tk.Tk()
window.title("Login Screen")
window.attributes("-fullscreen", False)

# Getting info
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Setting the background
canvas = tk.Canvas(window, width=screen_width, height=screen_height, bg='#261C2C')
canvas.pack()

# Tkinter Vars
userNameTk = tk.StringVar()
passwordTk = tk.StringVar()

# Setting up Entries and Text
userNameEntry = tk.Entry(window, textvariable = userNameTk, bg='#E63E6D', borderwidth=0, justify='center', width=10,
                         font=('Norican', 50, 'normal')).place(x=screen_width*0.2, y=screen_height * 0.15625)
passwordEntry = tk.Entry(window, textvariable = passwordTk, bg='#E63E6D', borderwidth=0, justify='center', width=10,
                         font=('Norican', 50, 'normal')).place(x=screen_width*0.5, y=screen_height * 0.15625)

userNameLabel = tk.Label(window, text = 'Username', bg='#261C2C', fg='white', font = ('Norican', 50, 'normal')).place(
    x=screen_width * 0.2278, y=screen_height * 0.0381)
passwordLabel = tk.Label(window, text = 'Password', bg='#261C2C', fg='white', font = ('Norican', 50, 'normal')).place(
    x=screen_width * 0.537, y=screen_height * 0.0381)

loginButton = tk.Button(window, text = 'Login', font = ('Norican', 30, 'normal'), bg='#8FD6E1', borderwidth=0, justify='center', width=12,
                        command = passChecks).place(x=screen_width*0.390625, y=screen_height * 0.3819)

# Run the window
window.mainloop()
