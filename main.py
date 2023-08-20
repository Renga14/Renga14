from tkinter import*
import configure
import new
from unit import cell



root= Tk()
root.configure(bg="lightblue")
root.geometry(f'{configure.WIDTH}x{configure.HEIGHT}')
root.title("Minesweepar Game")
root.resizable(False,False)

top_frame = Frame(root,bg="gray",
                  width = configure.WIDTH,
                  height = new.height_prct(25))
top_frame.place(x=0,y=0)

game_title = Label(top_frame, bg = "gray", fg="white",
                  text = "R e n g a" ,
                  font = ('',25)
                  )
game_title.place(x= new.width_prct(20),y=0)


center_frame= Frame(root,bg="white",width=new.width_prct(75),
                    height = new.height_prct(75)
                    ).place(
                        x=new.width_prct(30),
                        y= new.height_prct(30)
                    )


for x in range(configure.GRID_SIZE):
    for y in range(configure.GRID_SIZE):
        c=Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column =x,row =y)


Cell.create_cell_count_lable(top_frame)
cell.cell_count_lable_object.place(
    x=new.width_prct(30),
    y=new.height_prct(15)
)        

cell.randamize_mines()
                 



root.mainloop()