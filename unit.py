from tkinter import*
import random 
import new
import configure
import ctypes
import sys

class cell:
    all=[]
    cell_count = configure.CELL_COUNT
    cell_count_lable_object = None

    def __init__(self,is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_objecct = None
        self.is_opened = False
        self.is_mine_candidate = False
        self.x = x
        self.y= y
        cell.all.append(self)


def create_btn_object(self,location):
    btn = Button(
        location,
        width=-12,
        height=4,
    )
    btn.bind('<Button-1>',self left-click-actions)
    btn.bind('<Button-2',self right-click-actions)

    def left_click_action(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cell_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
                    self.show_cell()

                    if cell.cell_count == configure.MINES_COUNT:

                        ctype.windll.user32.MessageBoxW(0,"congratulations you won the game","Game Over",0)

                        self.cell_btn_object.unbind("<Button-1>")
                        self.cell_btn_object.unbind("<Button-3")

                    

    


    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.messageboxW(0,"you clicked on a mine","play again",0)
        sys.exit()
    def get_cell_by_axis(self,x,y):
        for cell in cell.all:
            if cell.x == x and cell.y == y:
                return cell 
    @property        
    def surrounded_cells(self):
         cells=[
            self.get_cell_by_axis(self.x-1, self.y-1),


            self.get_cell_by_axis(self.x-1 self.y)
            self.get_cell_by_axis(self.x-1 self.y+1)
            self.get_cell_by_axis(self.x self.y+1)
            ]
cells = [cell for cell in cell if cell is not None]
return cells



@property
def surrounded_cells_mines_length(self):
    counter = 0
    for cell in self.surrounded_cells:
        if cell.is_mine:
            counter +=1
    return counter

def show_cell(self):
    if not self.is_opened:
        Cell.cell_count-=1
        self.cell_btn_object.configure(text = self.surrounded-cells_mines_length)
        if Cell.cell_count_label_object:
            Cell.cell_count_lable_object.configure(text = f"cells Left:{Cell.cell_count}")
        self.cell_btn_object.configure(bg = "white")
        self.is_opentd = True


def right_click_actions(self,event):
    if not self.is_mine_candidate:
        self.cell_btn_object.configure(bg= "orange")
        self.is_mine_condidate = True
    else:
        self.cell_btn-object.configure(bg = "white")
        self.is_mine_condidate = False

@staticmethod
def randomize_mine():
    picked_cells= random.sample(Cell.all,configure.MINES_COUNT)
    for picked_cell.is_mine = True
    
def__repr__(self):
    return f"cell({self.x},{self.y})"

