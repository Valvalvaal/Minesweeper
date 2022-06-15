from tkinter import Button


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text='text'
        )

        # Assign an event to a button with bind method
        btn.bind('<Button-1>', self.left_click_actions)  # Left click
        btn.bind('<Button-2>', self.right_click_actions)  # Right click

        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print('I am left clicked!')

    def right_click_actions(self, event):
        print('I am right clicked!')
