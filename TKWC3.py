
from tkinter import*
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0),('paper',1),('scissors',2)]

def computer_wins():
    global computer_score, player_score
    computer_score +=1
    winner_label.config(text= "Computer Won!!")
    computer_score_label.config(text = "computer Score:" + str(computer_score))
    player_score_label.config(text = "Player Score:" + str(player_score))

def player_wins():
    global computer_score, player_score
    player_score +=1
    winner_label.config(text= "Player Won!!")
    computer_score_label.config(text = "computer Score:" + str(computer_score))
    player_score_label.config(text = "Player Score:" + str(player_score))

def tie():
    global computer_score, player_score
    winner_label.config(text= "TIE!!")
    computer_score_label.config(text = "computer Score:" + str(computer_score))
    player_score_label.config(text = "Player Score:" + str(player_score))

def player_choice(player_input):
    global computer_score,player_score
    print(player_input)

    computer_input = get_computer_choice()
    print(computer_input)

    player_choice_label.config(text='You Seleceted' + player_input[0])
    computer_choice_label.config(text='Computer Seleceted' + computer_input[0])

    #game logic
    if(player_input == computer_input):
        tie()

    #if palyer chosen rock
    if (player_input[1]==0):
        if(computer_input[1]==1):
            computer_wins()
        elif(computer_input[1]==2):
            player_wins()

    #if has paper
    if(player_input[1]==1):
        if(computer_input[1]==0):
            player_wins()
        elif(computer_input[1]==2):
            computer_wins()

    #if palyer has cirssors
    if(player_input[1]==2):
        if(computer_input[1]==0):
            computer_wins()
        elif(computer_input[1]==1):
            player_wins()

def get_computer_choice():
    return random.choice(options)

window = Tk()
window.title("ROCK PAPEER SCISSOR S GAME")

app_font = font.Font(size =12)

game_title = Label(text="LEsts start the game", font=font.Font(size=20),fg='grey')
game_title.pack()

winner_label = Label(text="LEsts start the game", font=font.Font(size=13),fg='green', pady=8)
winner_label.pack()

input_frame = Frame(window)
input_frame.pack()

player_options = Label(input_frame, text="Your optiojs:",font = app_font, fg='grey')
player_options.grid(row=0,column=1, pady=8)

rock_btn = Button(input_frame, text="Rock", width = 15,bg="pink",pady=5,command=lambda:player_choice(options[0]))
rock_btn.grid(row=1, column=1, pady=5, padx=8)

paper_btn = Button(input_frame, text="paper", width = 15,bg="silver",pady=5,command=lambda:player_choice(options[1]))
paper_btn.grid(row=1, column=1, pady=5, padx=8)

scissors_btn = Button(input_frame, text="scissors", width = 15,bg="pink",pady=5,command=lambda:player_choice(options[2]))
scissors_btn.grid(row=1, column=1, pady=5, padx=8)

score_label = Label(input_frame,text="Score:", font = app_font,fg="grey")
score_label.grid(row=2,column=0)

player_choice_label = Label(input_frame,text="You selected:", font=app_font)
player_choice_label.grid(row=3,column=1, pady=5)

player_score_label = Label(input_frame,text="Your score:--", font=app_font)
player_score_label.grid(row=3,column=2)

computer_choice_label = Label(input_frame,text="Computer Selected--",font=app_font,fg="black")
computer_choice_label.grid(row=4, column=1, pady=5)

computer_score_label = Label(input,text="Computer score--",font=app_font,fg="black")
computer_choice_label.grid(row=4, column=2, padx=(10,0), pady=5)

window.geometry('7000x300')
window.mainloop()


