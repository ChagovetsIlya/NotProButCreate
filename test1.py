import tkinter as tk
from tkinter import *
import tkinter.colorchooser

class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = 'red'
        self.brush_size = 2
        self.setUI()
        
        self.cords = [0,0,0,0]
        self.line = list()
        self.buffer = list()

    def set_color(self, new_color):
        self.color = "#%02x%02x%02x" % new_color

    def set_brush_size(self, new_size):
        self.brush_size = int(new_size.get())

    def draw0(self, event):
      self.cords.append(event.x)
      self.cords.append(event.y)
      self.canv.coords(self.line[-1], *self.cords)

    def draw1(self, event):
      self.cords = [event.x, event.y, event.x, event.y]
      self.line.append(self.canv.create_line(self.cords, width=self.brush_size, fill=self.color))

    def deleting(self, event):
      self.buffer.append(self.canv.coords(self.line[-1]))
      self.canv.delete(self.line[-1])
      self.line.pop()
      print(self.line)
      print(self.buffer)


    def returning(self):
      if len(self.buffer) > 0:
        self.line.append(self.canv.create_line(self.buffer[-1] , width=self.brush_size, fill=self.color))
        self.buffer.pop(-1)

    def pr(self,event):
      print((self.line))
        

    def setUI(self):

        self.parent.title("Pythonicway PyPaint")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна

        self.canv.bind("<B1-Motion>", self.draw0) # Привязываем обработчик к канвасу. <B1-Motion> означает "при движении зажатой левой кнопки мыши" вызывать функцию draw
        self.canv.bind("<Button-1>", self.draw1)

        self.canv.bind_all('<Command-z>', self.deleting)

        color_lab = Label(self, text="Color: ") # Создаем метку для кнопок изменения цвета кисти
        color_lab.grid(row=0, column=0, padx=6) # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей

        red_btn = Button(self, text="Change color", width=10,
                         command=lambda: self.set_color(tkinter.colorchooser.askcolor()[0])) # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов), функция вызываемая при нажатии кнопки.
        red_btn.grid(row=0, column=1) # Устанавливаем кнопки

        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=5, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)

        one_btn = Button(self, text="Change size", width=10,
                         command=lambda: self.set_brush_size(entry))
        one_btn.grid(row=1, column=1)

        entry = Entry(self, width=10)
        entry.grid(row=1, column=2)

        tri_btn = Button(self, text="sus", width=10,
                         command=lambda: self.deleting(self))
        tri_btn.grid(row=0, column=2)

        chetiri_btn = Button(self, text="antisus", width=10,
                         command=lambda: self.returning())
        chetiri_btn.grid(row=0, column=3)

        

def main():
    root = Tk()
    root.geometry("850x500+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()