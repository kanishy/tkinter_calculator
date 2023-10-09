import tkinter as tk
from tkinter import messagebox

end = False
ch=0
s1 = 0
s2 = 0
d = 0
curr_player:str
board=[['', '', ''], ['', '', ''], ['', '', '']]


p1:str
p2:str

def play():
    global p1, p2, curr_player, end
    n1 = name1.get()
    n2 = name2.get()
    if choice.get():
        p1 = 'X'
        p2 = 'O'
    else:
        p1 = 'O'
        p2 = 'X'
    curr_player = p1
    root = tk.Toplevel(root1)
    root.title("Tic-Tac-Toe")
    root.resizable(False, False)
    root.config(padx=10, pady=10, bg="#297F87")
    
    score1 = tk.StringVar(root, value=f"{n1}'s score: {s1}")
    tk.Label(root, anchor="w", textvariable=score1, font=("Consolas", 15),fg="white", bg="#297F87").grid(row=0, column=0, columnspan=3, sticky="w")
    score2 = tk.StringVar(root, value=f"{n2}'s score: {s2}")
    tk.Label(root, anchor="w", textvariable=score2, font=("Consolas", 15),fg="white", bg="#297F87").grid(row=1, column=0, sticky="w", columnspan=3, pady=3)
    draw = tk.StringVar(root, value= f'Draws: {d}')
    tk.Label(root, anchor="w", textvariable=draw, font=("Consolas", 15),fg="white", bg="#297F87").grid(row=2, column=0, sticky="w", columnspan=3, pady=3)
    turn = tk.StringVar(value=f"{name1.get()}'s turn")
    tk.Label(root, anchor="w", textvariable=turn, font=("Consolas", 15),fg="yellow", bg="#297F87").grid(row=3, column=0, sticky="w", columnspan=3, pady=3)
    
    
    buttons=[['', '', ''], ['', '', ''], ['', '', '']]
    b_frame = tk.Frame(root, bg="#297F87")
    b_frame.grid(row=4, columnspan=3, padx=20, pady=20)
    for i in range(4,7):
        for j in range(3):
            buttons[i-4][j] = tk.Button(b_frame, bg="#C1CFC0", font=("Consolas", 60), text=" ", command=lambda i=i-4, j=j: click(i, j, buttons, score1, score2, draw, turn), width=3, height=1)
            buttons[i-4][j].grid(row=i, column=j, padx=5, pady=5)
    
    tk.Button(root, text="Reset", font=("Consolas", 15), bg="#DF2E2E", fg="white", command=lambda:reset_score(buttons, score1, score2, draw)).grid(row=5, column=0, sticky="e", padx=80)
    tk.Button(root, text="Final", font=("Consolas", 15), bg="#DF2E2E", fg="white", command=lambda: final(root)).grid(row=5, column=2, sticky="w", padx=80)
    
    
def click(i, j, buttons, score1, score2, draw, turn):
    global curr_player, s1, s2, d, board, ch
    if curr_player == p1 and board[i][j] == '':
        buttons[i][j].config(text=p1, bg="#F6D167", font=("Consolas", 60), state="disabled")
        board[i][j] = p1
        curr_player = p2
        turn.set(f"{name2.get()}'s turn")
    elif board[i][j] == '':
        buttons[i][j].config(text=p2, bg="#FFF7AE", font=("Consolas", 60), state="disabled")
        board[i][j] = p2
        curr_player = p1
        turn.set(f"{name1.get()}'s turn")
    result = update()
    if result is not None:
        if result == p1:
            s1 += 1
            score1.set(f"{name1.get()}'s score: {s1}")
            ch = 0
            
        elif result == p2:
            s2 += 1
            score2.set(f"{name2.get()}'s score: {s2}")
            ch = 0
            
        else:
            d += 1
            draw.set(f'Draws: {d}')
            ch = 0
            
        reset(buttons)
    else:
        ch += 1
        if ch > 8:
            ch = 0
            d += 1
            draw.set(f'Draws: {d}')
            reset(buttons)
        
def reset(buttons):
    global board, curr_player
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(bg="#C1CFC0", text=" ", state="normal")
            board[i][j] = ''
    curr_player = p1
            
def update():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None
        
def reset_score(buttons, score1, score2, draw):
    global ch, s1, s2, d
    reset(buttons)
    ch=s1=s2=d=0
    score1.set(f"{name1.get()}'s score: {s1}")
    score2.set(f"{name2.get()}'s score: {s2}")
    draw.set(f'Draws: {d}')

def final(root):
    global end
    if s1>s2:
        messagebox.showinfo(title="Result", message=f"{name1.get()}'s score = {s1}\n{name2.get()}'s score = {s2}\nDraws = {d}\n{name1.get()} is winner")
    elif s1<s2:
        messagebox.showinfo(title="Result", message=f"{name1.get()}'s score = {s1}\n{name2.get()}'s score = {s2}\nDraws = {d}\n{name2.get()} is winner")
    else:
        messagebox.showinfo(title="Result", message=f"{name1.get()}'s score = {s1}\n{name2.get()}'s score = {s2}\nDraws = {d}\nIt's a draw")
    root.destroy()
    
root1 = tk.Tk()
root1.title("Tic-Tac-Toe")
root1.resizable(False, False)
root1.config(padx=10, pady=10, bg="#26577C")

player1 = tk.Label(root1, text="Player 1 -", font=("Consolas", 15), anchor="w", fg="#EBE4D1", bg="#26577C")
player1.grid(row=0, column=0)
name1_lbl = tk.Label(root1, text="Name: ", font=("Consolas", 15), anchor="w", fg="#EBE4D1", bg="#26577C")
name1_lbl.grid(row=1, column=0, sticky="w")
name1 = tk.Entry(root1, font=("Consolas", 15), width=13, bg="#EBE4D1")
name1.focus()
name1.grid(row=1, column=1, sticky="w", columnspan=2)

frame1 = tk.Frame(root1, bg="#26577C")
frame1.grid(row=2, column=1)
choice = tk.BooleanVar()
sym1_lbl = tk.Label(root1, text="Symbol: ", font=("Consolas", 15), anchor="w", fg="#EBE4D1", bg="#26577C")
sym1_lbl.grid(row=2, column=0, sticky="w")
sym1_x = tk.Radiobutton(frame1, variable=choice, text="X", font=("Consolas", 18), value=True, bg="#26577C")
sym1_x.grid(row=2, column=1, sticky="w")
sym1_O = tk.Radiobutton(frame1, variable=choice, text="O", font=("Consolas", 18), value=False, bg="#26577C")
sym1_O.grid(row=2, column=2, sticky="w")


player2 = tk.Label(root1, text="\nPlayer 2 -", font=("Consolas", 15), anchor="w", fg="#EBE4D1", bg="#26577C")
player2.grid(row=3, column=0)
name2_lb1 = tk.Label(root1, text="Name: ", font=("Consolas", 15), anchor="w", fg="#EBE4D1", bg="#26577C")
name2_lb1.grid(row=4, column=0, sticky="w")
name2 = tk.Entry(root1, font=("Consolas", 15), width=13, bg="#EBE4D1")
name2.grid(row=4, column=1, sticky="w", columnspan=2)

frame2 = tk.Frame(root1, bg="#26577C")
frame2.grid(row=5, column=1)
sym2_lbl = tk.Label(root1, text="Symbol: ", font=("Consolas", 15), anchor="w", fg="#EBE4D1", bg="#26577C")
sym2_lbl.grid(row=5, column=0, sticky="w")
sym1_x = tk.Radiobutton(frame2, variable=choice, text="X", font=("Consolas", 18), value=False, bg="#26577C")
sym1_x.grid(row=5, column=1, sticky="w")
sym1_O = tk.Radiobutton(frame2, variable=choice, text="O", font=("Consolas", 18), value=True, bg="#26577C")
sym1_O.grid(row=5, column=2, sticky="w")

play_b = tk.Button(text="  Play ▶️", font=("Consolas", 18), command=play, bg="#E55604", fg="#EBE4D1")
play_b.grid(row=6, columnspan=3) 
root1.mainloop()