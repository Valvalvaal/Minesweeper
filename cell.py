from tkinter import Button
import random
import settings


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list

        Cell.all.append(self)  # Attribute

    def create_btn_object(self, location):
        # TODO #1 determine a better cell height
        btn = Button(
            location,
            width=12,
            height=4
        )

        # Assign an event to a button with bind method
        btn.bind('<Button-1>', self.left_click_actions)  # Left click
        btn.bind('<Button-2>', self.right_click_actions)  # Right click

        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()

    def show_mine(self):
        pass

    def right_click_actions(self, event):
        print('I am right clicked!')

    @staticmethod
    # Doesn't belong to each instance, belongs globally to the class
    def randomize_mines():
        # Randomly pick values to be mines
        mines_cells = random.sample(Cell.all, 10)

        for picked_cell in mines_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        """
        Changes how the cells objects are represented
        """
        return f"Cell ({self.x}, {self.y})"
