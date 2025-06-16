import tkinter as tk
from tkinter import messagebox


def check_winner(b, s):
    return any([
        b[0][0] == b[0][1] == b[0][2] == s,
        b[1][0] == b[1][1] == b[1][2] == s,
        b[2][0] == b[2][1] == b[2][2] == s,
        b[0][0] == b[1][0] == b[2][0] == s,
        b[0][1] == b[1][1] == b[2][1] == s,
        b[0][2] == b[1][2] == b[2][2] == s,
        b[0][0] == b[1][1] == b[2][2] == s,
        b[0][2] == b[1][1] == b[2][0] == s
    ])

def is_draw(b):
    return all(cell != ' ' for row in b for cell in row)

def evaluate(b):
    if check_winner(b, 'X'):
        return 1
    elif check_winner(b, 'O'):
        return -1
    return 0


def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)
    if score != 0 or is_draw(board):
        return score

    if is_maximizing:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    val = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best = max(best, val)
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    val = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best = min(best, val)
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def best_move(board):
    best_val = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = ' '
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move


def on_click(i, j):
    global board, buttons, stats

    if board[i][j] != ' ':
        return
    board[i][j] = 'O'
    buttons[i][j].config(text='O', state='disabled')

    if check_winner(board, 'O'):
        stats['Wins'] += 1
        messagebox.showinfo("نتیجه", "شما بردید!")
        update_stats()
        return

    if is_draw(board):
        stats['Ties'] += 1
        messagebox.showinfo("نتیجه", "مساوی شد!")
        update_stats()
        return

    ai_i, ai_j = best_move(board)
    board[ai_i][ai_j] = 'X'
    buttons[ai_i][ai_j].config(text='X', state='disabled')

    if check_winner(board, 'X'):
        stats['Losses'] += 1
        messagebox.showinfo("نتیجه", "هوش مصنوعی برد!")
        update_stats()
        return

    if is_draw(board):
        stats['Ties'] += 1
        messagebox.showinfo("نتیجه", "مساوی شد!")
        update_stats()

def update_stats():
    stats_label.config(text=f"برد: {stats['Wins']}   باخت: {stats['Losses']}   مساوی: {stats['Ties']}")

def reset_game():
    global board, buttons
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ', state='normal')




root = tk.Tk()
root.title("Tic Tac Toe - با هوش مصنوعی")
root.configure(bg="#222831")

board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
stats = {'Wins': 0, 'Losses': 0, 'Ties': 0}

style = {'font': ('Helvetica', 24), 'width': 5, 'height': 2, 'bg': '#EEEEEE', 'fg': '#222831', 'bd': 2}

frame = tk.Frame(root, bg="#222831")
frame.pack(pady=20)

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(frame, text=' ', command=lambda i=i, j=j: on_click(i, j), **style)
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

stats_label = tk.Label(root, text="برد: 0   باخت: 0   مساوی: 0", font=('Helvetica', 14), bg="#222831", fg="white")
stats_label.pack(pady=10)

reset_button = tk.Button(root, text="شروع بازی جدید", command=reset_game, font=('Helvetica', 12), bg="#00ADB5", fg="white")
reset_button.pack(pady=10)

root.mainloop()
