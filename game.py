# Modules
from tkinter import *
from tkinter import messagebox
from pygame import mixer
import random
import os

mixer.init()

# Window Customisation
login = Tk()
login.title('RetroConsole(X/O)')
login.geometry('451x384')
login.config(bg='#FF6EC7')

# Title
Title_lbl = Label(login, text='RetroConsole(X/O)', font='Times 16 italic bold underline', bg='#FF6EC7')
Title_lbl.pack()
Credit_lbl = Label(login, text='Made By Advait Jadhav', bg='#FF6EC7')
Credit_lbl.pack(pady=10)
Note_lbl = Label(login, text="(Note:-Your name shouldn't contain\nmore than 8 letters)", bg='#FF6EC7')
Note_lbl.pack()

# Paths for pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Creation of command for entry button
def entry_clear():
    global player1, player2
    mixer.music.load(resource_path("start_sound.mp3"))
    mixer.music.play()

    player1 = Entry1.get()
    player2 = Entry2.get()
    login.destroy()


# Entry Box
Entry_lbl1 = Label(login, text='Player 1(X)', font='none 14', bg='#FF6EC7', fg='#800080')
Entry_lbl1.pack()
Entry1 = Entry(login, width=15, bg='#FFDAB9', font='Garamond 18', justify=CENTER)
Entry1.pack()

Entry_lbl2 = Label(login, text='Player 2(O)', font='none 14', bg='#FF6EC7', fg='#800080')
Entry_lbl2.pack()
Entry2 = Entry(login, width=15, bg='#FFDAB9', font='Garamond 18', justify=CENTER)
Entry2.pack()

# Button fo entry box
entry_btn = Button(login, text='PROCEED', bd=5, bg='cadet blue', activebackground='#abd7eb', highlightcolor='#abd7eb',
                   command=entry_clear)
entry_btn.pack(pady=20)

# Creation of menu
my_menubar = Menu(login)
my_options = Menu(my_menubar, tearoff=False)
my_menubar.add_cascade(label='Options', menu=my_options)
my_options.add_command(label='Exit Game', command=login.quit)
login.config(menu=my_menubar)

if __name__ == '__main__':
    login.mainloop()

# Window Customisation
game = Tk()
game.title('RetroConsole(X/O)')
game.config(bg='#FF6EC7')

# Player Profiles
l1 = Label(game, text=f'{player1}: X', bg='#FF6EC7', fg='#800080', font='times 16')
l1.grid(row=0, column=1)

l2 = Label(game, text=f'{player2}: O', bg='#FF6EC7', fg='#800080', font='times 16')
l2.grid(row=0, column=2)

# Important Variables
player = 1
count = 0


# disable_all_buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# Music for winner
def winning_sound():
    global sound_lst, ran

    sound_lst = ["winningdamn_sound.mp3", "winningfly_sound.mp3", "winninglol_sound.mp3"]
    mixer.music.load(resource_path(random.choice(sound_lst)))
    mixer.music.play(loops=0)


# check_for_winner for player 1(X)
def check_for_winner():
    global winner
    winner = False
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg='#D53A7D')
        b2.config(bg='#D53A7D')
        b3.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player1}: X wins..!')
        reset()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg='#D53A7D')
        b5.config(bg='#D53A7D')
        b6.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player1}: X wins..!')
        reset()
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        b7.config(bg='#D53A7D')
        b8.config(bg='#D53A7D')
        b9.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player1}: X wins..!')
        reset()
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg='#D53A7D')
        b4.config(bg='#D53A7D')
        b7.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player1}: X wins..!')
        reset()
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg='#D53A7D')
        b5.config(bg='#D53A7D')
        b8.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player1}: X wins..!')
        reset()
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg='#D53A7D')
        b6.config(bg='#D53A7D')
        b9.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player1}: X wins..!')
        reset()
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg='#D53A7D')
        b5.config(bg='#D53A7D')
        b9.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player1}: X wins..!')
        reset()
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        b3.config(bg='#D53A7D')
        b5.config(bg='#D53A7D')
        b7.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player1}: X wins..!')
        reset()

    # check_for_winner for player 2(O)

    if b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg='#D53A7D')
        b2.config(bg='#D53A7D')
        b3.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player2}: X wins..!')
        reset()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg='#D53A7D')
        b5.config(bg='#D53A7D')
        b6.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player2}: X wins..!')
        reset()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(bg='#D53A7D')
        b8.config(bg='#D53A7D')
        b9.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player2}: X wins..!')
        reset()
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg='#D53A7D')
        b4.config(bg='#D53A7D')
        b7.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player2}: X wins..!')
        reset()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg='#D53A7D')
        b5.config(bg='#D53A7D')
        b8.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player2}: X wins..!')
        reset()
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg='#D53A7D')
        b6.config(bg='#D53A7D')
        b9.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player2}: X wins..!')
        reset()
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg='#D53A7D')
        b5.config(bg='#D53A7D')
        b9.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player2}: X wins..!')
        reset()
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        b3.config(bg='#D53A7D')
        b5.config(bg='#D53A7D')
        b7.config(bg='#D53A7D')
        winner = True
        disable_all_buttons()
        winning_sound()
        messagebox.showinfo('Game Over', f'{player2}: X wins..!')
        reset()
    elif count == 9 and winner == False:
        disable_all_buttons()
        mixer.music.load(resource_path("draw_sound.mp3"))
        mixer.music.play(loops=0)
        messagebox.showinfo('Game Over', 'It is a Draw\nNo one wins..!')
        reset()


# Activation of Buttons
def b_click(b):
    global player, count

    if b['text'] == ' ' and player == 1:
        b['text'] = 'X'
        mixer.music.load(resource_path("b_click1_sound.mp3"))
        mixer.music.play(loops=0)
        player = 2
        count += 1
        check_for_winner()
    elif b['text'] == ' ' and player == 2:
        b['text'] = 'O'
        mixer.music.load(resource_path("b_click2_sound.mp3"))
        mixer.music.play(loops=0)
        player = 1
        count += 1
        check_for_winner()
    else:
        messagebox.showerror('RetroConsole(X/O)',
                             'Hey! That box has already been selected\nPlease select another box...')


Grid.rowconfigure(game, 1, weight=1)
Grid.rowconfigure(game, 4, weight=1)
Grid.rowconfigure(game, 8, weight=1)
Grid.columnconfigure(game, 1, weight=1)
Grid.columnconfigure(game, 2, weight=1)
Grid.columnconfigure(game, 3, weight=1)


# Resetting the Game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global player, count
    player = 1
    count = 0

    # Construction of Buttons
    b1 = Button(game, text=' ', width=6, height=3, font='Helvetica 20', bd=5, activebackground='#abd7eb',
                highlightcolor='#abd7eb', bg='cadet blue', command=lambda: b_click(b1))
    b1.grid(row=1, column=1, sticky='nsew')

    b2 = Button(game, text=' ', width=6, height=3, font='Helvetica 20', bd=5, activebackground='#abd7eb',
                highlightcolor='#abd7eb', bg='cadet blue', command=lambda: b_click(b2))
    b2.grid(row=1, column=2, sticky='nsew')

    b3 = Button(game, text=' ', width=6, height=3, font='Helvetica 20', bd=5, activebackground='#abd7eb',
                highlightcolor='#abd7eb', bg='cadet blue', command=lambda: b_click(b3))
    b3.grid(row=1, column=3, sticky='nsew')

    b4 = Button(game, text=' ', width=6, height=3, font='Helvetica 20', bd=5, activebackground='#abd7eb',
                highlightcolor='#abd7eb', bg='cadet blue', command=lambda: b_click(b4))
    b4.grid(row=4, column=1, sticky='nsew')

    b5 = Button(game, text=' ', width=6, height=3, font='Helvetica 20', bd=5, activebackground='#abd7eb',
                highlightcolor='#abd7eb', bg='cadet blue', command=lambda: b_click(b5))
    b5.grid(row=4, column=2, sticky='nsew')

    b6 = Button(game, text=' ', width=6, height=3, font='Helvetica 20', bd=5, activebackground='#abd7eb',
                highlightcolor='#abd7eb', bg='cadet blue', command=lambda: b_click(b6))
    b6.grid(row=4, column=3, sticky='nsew')

    b7 = Button(game, text=' ', width=6, height=3, font='Helvetica 20', bd=5, activebackground='#abd7eb',
                highlightcolor='#abd7eb', bg='cadet blue', command=lambda: b_click(b7))
    b7.grid(row=8, column=1, sticky='nsew')

    b8 = Button(game, text=' ', width=6, height=3, font='Helvetica 20', bd=5, activebackground='#abd7eb',
                highlightcolor='#abd7eb', bg='cadet blue', command=lambda: b_click(b8))
    b8.grid(row=8, column=2, sticky='nsew')

    b9 = Button(game, text=' ', width=6, height=3, font='Helvetica 20', bd=5, activebackground='#abd7eb',
                highlightcolor='#abd7eb', bg='cadet blue', command=lambda: b_click(b9))
    b9.grid(row=8, column=3, sticky='nsew')


# Creation of Menu
mymenu = Menu(game)
game.config(menu=mymenu)

# Creation of Options Menu
Options_menu = Menu(mymenu, tearoff=False)
mymenu.add_cascade(label='Options', menu=Options_menu)
Options_menu.add_command(label='Restart Game', command=reset)
mymenu.add_separator()
# Adding the menu
Options_menu.add_command(label='Exit', command=game.quit)



# Starting the game
reset()

if __name__ == '__main__':
    game.mainloop()
