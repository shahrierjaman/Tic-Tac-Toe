from tkinter import *
import tkinter.messagebox
import random

def next_turn(row,column):
    global player

    if btns[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            btns[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                lbl.config(text=(players[1]+"'s"+" turn"))

            elif check_winner() is True:
                lbl.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                lbl.config(text="Match Tie")

        else:
            btns[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                lbl.config(text=(players[0] + "'s" + " turn"))

            elif check_winner() is True:
                lbl.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                lbl.config(text="Match Tie")



def check_winner():
    for row in range(3):
        if btns[row][0]['text'] == btns[row][1]['text'] == btns[row][2]['text'] != "":
            btns[row][0].config(bg='green')
            btns[row][1].config(bg='green')
            btns[row][2].config(bg='green')
            return True

    for col in range(3):
        if btns[0][col]['text'] == btns[1][col]['text'] == btns[2][col]['text'] != "":
            btns[0][col].config(bg='green')
            btns[1][col].config(bg='green')
            btns[2][col].config(bg='green')
            return True

    if btns[0][0]['text'] == btns[1][1]['text'] == btns[2][2]['text'] != "":
        btns[0][0].config(bg='green')
        btns[1][1].config(bg='green')
        btns[2][2].config(bg='green')
        return True

    elif btns[0][2]['text'] == btns[1][1]['text'] == btns[2][0]['text'] != "":
        btns[0][2].config(bg='green')
        btns[1][1].config(bg='green')
        btns[2][0].config(bg='green')
        return True

    elif empty_space() is False:
        for row in range(3):
            for col in range(3):
                btns[row][col].config(bg='yellow')
        return "Tie"

    else:
        return False
def empty_space():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if btns[row][col]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True
def new_game():
    global player
    player = random.choice(players)
    lbl.config(text=player + "'s" + " turn")
    for row in range(3):
        for column in range(3):
            btns[row][column].config(text="", bg='#F0F0F0')

win = Tk()
win.title("Tic-Tac-Toe")
win.config()
players = ["X","O"]
player = random.choice(players)
btns = [[0,0,0],
        [0,0,0,],
        [0,0,0]]
lbl = Label(text=player+"'s"+" turn",font=('consolas',40))
lbl.pack(side='top')

reset_btn = Button(text="Reset",font=('consolas',20),command=new_game)
reset_btn.pack(side="top")

frame = Frame(win)
frame.pack()

for row in range(3):
    for column in range(3):
        btns[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                     command=lambda row=row, column=column: next_turn(row, column))
        btns[row][column].grid(row=row, column=column)
win.mainloop()
