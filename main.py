import tkinter as tk

# ----------- GLOBAL VARIABLES ----------- #
window_color = '#53366b'
grid_color = '#ffff'

# ----------- MAIN WINDOW ---------------- #

class BoggleGame(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Boggle Game')


app = BoggleGame()
app.mainloop()
