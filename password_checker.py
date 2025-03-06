import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

def check_password(*args):
    password = password_var.get()
    score = sum([
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password)
    ])
    
    if score <= 2:
        style.configure("Neon.Horizontal.TProgressbar", background='#FF0055')  # Neon Pink
    elif score <= 3:
        style.configure("Neon.Horizontal.TProgressbar", background='#00FF66')  # Neon Green
    else:
        style.configure("Neon.Horizontal.TProgressbar", background='#00FFFF')  # Neon Cyan
    
    progress['value'] = (score / 5) * 100
    
    if score <= 2:
        strength_var.set("😡 Weak")
        strength_label.configure(fg='#FF0055')  
    elif score <= 3:
        strength_var.set("😬 Medium")
        strength_label.configure(fg='#00FF66')  
    else:
        strength_var.set("💪 Strong")
        strength_label.configure(fg='#00FFFF')  

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300+480+200")
root.configure(bg='#000')  
root.resizable(False, False)

style = ttk.Style()
style.theme_use('default')
style.configure("Neon.Horizontal.TProgressbar", 
                background='#FF0055',
                troughcolor='#111111',
                bordercolor='#000000',
                lightcolor='#000000',
                darkcolor='#000000')


neon_font = tkfont.Font(family='Helvetica', size=14, weight='bold')

password_var = tk.StringVar()
password_var.trace('w', check_password)


title_label = tk.Label(
    root, 
    text="Password Strength Checker", 
    font=('Helvetica', 18, 'bold'),
    bg='#000',
    fg='#FF00FF'  
)
title_label.pack(pady=20)

entry_label = tk.Label(
    root, 
    text="Enter Password:", 
    font=neon_font,
    bg='#000',
    fg='#00FFFF' 
)
entry_label.pack(pady=5)

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    show="•",
    width=30,
    font=neon_font,
    bg='#111111',
    fg='#00FFFF',  
    insertbackground='#00FFFF'  
)
password_entry.pack(pady=10)

progress = ttk.Progressbar(
    root,
    length=300,
    mode="determinate",
    style="Neon.Horizontal.TProgressbar"
)
progress.pack(pady=20)

strength_var = tk.StringVar()
strength_label = tk.Label(
    root,
    textvariable=strength_var,
    font=neon_font,
    bg='#000',
    fg='#FF0055' 
)
strength_label.pack()

root.mainloop()