from tkinter import *
import settings

root = Tk()

root.configure(bg="#c6c6c6")
# Change the settings of the window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(root,
                  bg="black",  # Change later
                  width=1440,
                  height=180)

top_frame.place(x=0, y=0)  # Set starting point according to pixels

left_frame = Frame(root,
                   bg='blue',  # Change later
                   width=360,
                   height=540
                   )

left_frame.place(x=0, y=0)

# Run the window
root.mainloop()  # Open until x is clicked
