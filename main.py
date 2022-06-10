from tkinter import *

root = Tk()

root.configure(bg="#c6c6c6")
# Change the settings of the window
root.geometry("1440x720")
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(root, bg="black", width=1440, height=180)  # Change later

# Run the window
root.mainloop()  # Open until x is clicked
