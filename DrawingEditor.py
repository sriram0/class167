from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title("Drawing Editor")
root.geometry("4000x2000")

data = [30, 30, 30, 30]

canv = Canvas(root, width=1000, height=500, highlightbackground="red")
img = ImageTk.PhotoImage(Image.open("start_point1.png"))
#canv.create_image(30, 30, image=img)
Label(root, text="Enter Color").pack()
inp = Entry(root, bg="lightblue")
inp.pack()
inp.insert(0, "black")

'''
def draw():
    global data
    col = inp.get()
    data[0],data[1]=data[2],data[3]
    def do(ndir):
       global data
       if ndir=="left":
           data[2]-=5
       elif ndir=="right":
           data[2]+=5
       elif ndir=="up":
           data[3]-=5
       elif ndir=="down":
           data[3]+=5
       nl=canv.create_line(data[0], data[1], data[2], data[3], width=2, fill=col)
    return lambda nd: do(nd)
lf=draw()("left")
'''

def draw(ndir):
    global data
    col = inp.get()
    data[0],data[1]=data[2],data[3]
    nl=canv.create_line(data[0], data[1], data[2], data[3], width=10, fill=col)
def lf(z):
    global data
    data[2]-=5
    print(z)
    draw("left")

canv.pack()
root.bind("<Left>", lf)
#root.bind("<Right>", rf)
#root.bind("<Up>", uf)
#root.bind("<Down>", df)

root.mainloop()
