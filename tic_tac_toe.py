from tkinter import *
from tkinter import messagebox

#defualt for first click
clicked = True
#count of moves
count = 0

#check click
def b_click(b):
    global clicked, count, all_square
    #list of all button
    all_square = [b1, b2, b3,
                  b4, b5, b6,
                  b7, b8, b9]

    #check click X
    if b["text"] == " " and clicked==True:
        b["text"] = "X"
        clicked = False
        count += 1
        for i in all_square:
            if b==i:
                square = all_square.index(i)
        check_winner(square, "X")

    #check click O
    elif b["text"] == " " and clicked==False:
        b["text"] = "O"
        clicked = True
        count += 1
        for i in all_square:
            if b==i:
                square = all_square.index(i)
        check_winner(square, "O")

    #Check selected boxes
    else:
        messagebox.showerror('Tic Tac Toe'
                             ,"This box is already selected")


def check_winner(square, text):
    global winner, all_square
    winner = False
    #list of the button text
    TIC = [b1["text"], b2["text"], b3["text"],
           b4["text"], b5["text"], b6["text"],
           b7["text"], b8["text"], b9["text"]]

    #chek win in row
    row_ind = square // 3
    row = TIC[row_ind * 3:(row_ind + 1) * 3]
    if all([spot == text for spot in row]):
        winner = True
        for i in all_square[row_ind * 3:(row_ind + 1) * 3]:
            i.config(bg="red")
        disable_all_buttons()
        messagebox.showinfo('Tic Tac Toe', f'{text}! won the game')

    #check win in column
    col_ind = square % 3
    column = [TIC[col_ind + i * 3] for i in range(3)]
    if all([spot == text for spot in column]):
        winner = True
        for i in [all_square[col_ind + i * 3] for i in range(3)]:
            i.config(bg="red")
        disable_all_buttons()
        messagebox.showinfo('Tic Tac Toe', f'{text}! won the game')


    #check win in diagonal
    if square % 2 == 0:
        diagonal_1 = [TIC[i] for i in [0, 4, 8]]
        if all([spot == text for spot in diagonal_1]):
            winner = True
            for i in [all_square[j] for j in [0, 4, 8]]:
                i.config(bg="red")
            disable_all_buttons()
            messagebox.showinfo('Tic Tac Toe', f'{text}! won the game')
        diagonal_2 = [TIC[i] for i in [2, 4, 6]]
        if all([spot == text for spot in diagonal_2]):
            winner = True
            for i in [all_square[j] for j in [2, 4, 6]]:
                i.config(bg="red")
            disable_all_buttons()
            messagebox.showinfo('Tic Tac Toe', f'{text}! won the game')

    if count==9 and winner==False:
        disable_all_buttons()
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")

#disable buttons after end game
def disable_all_buttons():
    global all_square
    for i in all_square:
        i.config(state=DISABLED)

window = Tk()
window.title("Tic Tac Toe")

def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,clicked,count
    clicked = True
    count = 0
    b1 = Button(window, text=" ", font=("Helvetica", 20),height=3
                , width=6, bg="SystemButtonFace",command=lambda: b_click(b1))
    b2 = Button(window, text=" ", font=("Helvetica", 20),height=3
                , width=6, bg="SystemButtonFace",command=lambda: b_click(b2))
    b3 = Button(window, text=" ", font=("Helvetica", 20),height=3
                , width=6, bg="SystemButtonFace",command=lambda: b_click(b3))
    b4 = Button(window, text=" ", font=("Helvetica", 20),height=3
                , width=6, bg="SystemButtonFace",command=lambda: b_click(b4))
    b5 = Button(window, text=" ", font=("Helvetica", 20),height=3
                , width=6, bg="SystemButtonFace",command=lambda: b_click(b5))
    b6 = Button(window, text=" ", font=("Helvetica", 20),height=3
                , width=6, bg="SystemButtonFace",command=lambda: b_click(b6))
    b7 = Button(window, text=" ", font=("Helvetica", 20),height=3
                , width=6, bg="SystemButtonFace",command=lambda: b_click(b7))
    b8 = Button(window, text=" ", font=("Helvetica", 20),height=3
                , width=6, bg="SystemButtonFace",command=lambda: b_click(b8))
    b9 = Button(window, text=" ", font=("Helvetica", 20),height=3
                , width=6, bg="SystemButtonFace",command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

my_menu = Menu(window)
window.config(menu=my_menu)
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)

reset()
window.mainloop()