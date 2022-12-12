import tkinter as tk
from tkinter import *
import tkinter.colorchooser
from PIL import Image
from tkinter import filedialog
from tkinter import filedialog

class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        
        self.color = 'red'
        self.brush_size = 2

        self.canvas_width = 512
        self.canvas_height = 512
        self.setUI()
        
        self.line_info = {'line'  , 'settings' }
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
      self.canv.coords(self.line[-1]['line'], *self.cords)

    def draw1(self, event):
      self.cords = [event.x, event.y, event.x, event.y]
      self.line.append({'line' : self.canv.create_line(self.cords, width=self.brush_size, fill=self.color),
        'settings' : [self.brush_size, self.color]})

    def deleting(self, event):

      self.buffer.append({'line' : self.canv.coords(self.line[-1]['line']), 
        'settings' : [ self.line[-1]['settings'][0], self.line[-1]['settings'][1]]})
      

      self.canv.delete(self.line[-1]['line'])
      self.line.pop()
      # print(self.line)
      # print(self.buffer)


    def returning(self, event):
      if len(self.buffer) > 0:
        self.line.append({'line' : self.canv.create_line(self.buffer[-1]['line'], width=self.buffer[-1]['settings'][0], fill=self.buffer[-1]['settings'][1]), 
          'settings' : [self.buffer[-1]['settings'][0], self.buffer[-1]['settings'][1]]})

        self.buffer.pop(-1)

    def pr(self,event):
      print((self.line))

    def Save(self, event):
      self.canv.postscript(file="my_dram.ps", colormode="color")
      assss = filedialogl.asksaveasfile()
      img = Image.open("my_dram.ps")
      img.save("my_dram.png", "png")

    def set_size(self, a, b):
        self.canvas_width = int(a)
        self.canvas_height = int(b)
        print(self.canvas_width)
        print(self.canvas_height)

        


    def setStartingPoint(self):
        self.parent.title("Введите размеры канваса")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(3, weight=1)
        self.rowconfigure(1, weight=1)

        entry_weight = Entry(self, width=10)
        entry_weight.grid(row=0, column=0)

        entry_height = Entry(self, width=10)
        entry_height.grid(row=0, column=1)

        red_btn = Button(self, text="Change color", width=10, command=lambda: self.set_size(entry_weight.get(), entry_height.get())) # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов), функция вызываемая при нажатии кнопки.
        red_btn.grid(row=0, column=2)
        

    def setUI(self):

        self.parent.title("Pythonicway PyPaint")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(7, weight=1)
        self.rowconfigure(3, weight=1)

        self.canv = Canvas(self, bg="white", width= self.canvas_width, height= self.canvas_height)  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.grid(row=3, column=1, columnspan=7, sticky=W+N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна

        self.canv.bind("<B1-Motion>", self.draw0) # Привязываем обработчик к канвасу. <B1-Motion> означает "при движении зажатой левой кнопки мыши" вызывать функцию draw
        self.canv.bind("<Button-1>", self.draw1)

        self.canv.bind_all('<Command-z>', self.deleting)
        self.canv.bind_all('<Command-y>', self.returning)
        self.canv.bind_all('<Command-x>', lambda x: self.canv.delete("all"))
        self.canv.bind_all('<Command-s>', self.Save)

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
                         command=lambda: self.returning(self))
        chetiri_btn.grid(row=0, column=3)

        

def main():
    root = Tk()
    root.geometry("850x500+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()