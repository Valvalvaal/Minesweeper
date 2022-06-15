from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

root.configure(bg=settings.COLOR)
# Change the settings of the window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(root,
                  bg=settings.COLOR,  # Change later
                  width=settings.WIDTH,
                  height=utils.height_pct(25))

top_frame.place(x=0, y=0)  # Set starting point according to pixels

left_frame = Frame(root,
                   bg=settings.COLOR,  # Change later
                   width=utils.width_pct(25),
                   height=utils.height_pct(75)
                   )

left_frame.place(x=0, y=utils.height_pct(25))

center_frame = Frame(root,
                     bg=settings.COLOR,
                     width=utils.width_pct(75),
                     height=utils.height_pct(75)
                     )

center_frame.place(
    x=utils.width_pct(25),
    y=utils.height_pct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c1 = Cell()
        c1.create_btn_object(center_frame)
        c1.cell_btn_object.grid(column=x, row=y)

# Run the window
root.mainloop()  # Open until x is clicked
