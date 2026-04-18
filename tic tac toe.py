from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Tic Tac Toe")
root.geometry("300x320")

# Variables
player = "X"
buttons = []

# Check winner
def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

# Button click
def click(row, col):
    global player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player

        if check_winner():
            messagebox.showinfo("Winner", f"Player {player} wins!")
            reset()

        elif all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Draw", "It's a Draw!")
            reset()

        player = "O" if player == "X" else "X"

# Reset board
def reset():
    global player
    player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

# Create buttons
for i in range(3):
    row = []
    for j in range(3):
        btn = Button(root, text="", font=("Arial", 20),
                     width=5, height=2,
                     command=lambda r=i, c=j: click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

root.mainloop()
