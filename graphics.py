from tkinter import Tk, BOTH, Canvas

### Creates the main window and line graphics for the program
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__running = False
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=self.width, height=self.height, background='white')
        self.canvas.pack(fill=BOTH, expand=1)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        self.__root.mainloop()
        print('Window closed...')

    def close(self):
        self.__running = False
        self.__root.destroy()

    def draw_line(self, line, fill_colour):
        line.draw(self.canvas, fill_colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_colour):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_colour, width=2)