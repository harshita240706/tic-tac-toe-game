from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Tic Tac Toe")
root.geometry("300x320")


p = "X"
bs = []


def c_w():
    for r in range(3):
        if bs[r][0]["text"] == bs[r][1]["text"] == bs[r][2]["text"] != "":
            return True

    for c in range(3):
        if bs[0][c]["text"] == bs[1][c]["text"] == bs[2][c]["text"] != "":
            return True

    if bs[0][0]["text"] == bs[1][1]["text"] == bs[2][2]["text"] != "":
        return True

    if bs[0][2]["text"] == bs[1][1]["text"] == bs[2][0]["text"] != "":
        return True

    return False


def click(r, c):
    global p

    if bs[r][c]["text"] == "":
        bs[r][c]["text"] = p

        if c_w():
            messagebox.showinfo("Winner", f"Player {p} wins!")
            reset()

        elif all(bs[i][j]["text"] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Draw", "It's a Draw!")
            reset()

        p = "O" if p == "X" else "X"


def reset():
    global p
    p = "X"
    for i in range(3):
        for j in range(3):
            bs[i][j]["text"] = ""


for i in range(3):
    r = []
    for j in range(3):
        btn = Button(root, text="", font=("Arial", 20),
                     width=5, height=2,
                     command=lambda r=i, c=j: click(r, c))
        btn.grid(row=i, column=j)
        r.append(btn)
    bs.append(r)

root.mainloop()
