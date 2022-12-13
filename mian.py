from tkinter import *
import tkinter.colorchooser
from PIL import Image
from tkinter import filedialog as fd

import io

from child_window import ChildWindow

class Paint:

	def __init__(self, width, height, title="Пеинт на минималках", resizable=(True, True), icon=None ):
		self.root = Tk()
		self.root.title(title)
		self.root.geometry(f"{width}x{height}+200+200")
		self.root.resizable(resizable[0],resizable[1])
		if icon:
			self.root.iconbitmap(icon)  

		self.Frame = Frame(self.root)
		
		self.color = 'red'
		self.brush_size = 2

		self.canvas_width = 512
		self.canvas_height = 512
		# self.setUI()
		
		self.line_info = {'line'  , 'settings' }
		self.cords = [0,0,0,0]
		self.line = list()
		self.buffer = list()


	def set_color(self, new_color):
		if new_color:
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
		if len(self.line):

			self.buffer.append({'line' : self.canv.coords(self.line[-1]['line']), 
			'settings' : [ self.line[-1]['settings'][0], self.line[-1]['settings'][1]]})


			self.canv.delete(self.line[-1]['line'])
			self.line.pop()

	def returning(self, event):
		if len(self.buffer):
			self.line.append({'line' : self.canv.create_line(self.buffer[-1]['line'], width=self.buffer[-1]['settings'][0], fill=self.buffer[-1]['settings'][1]), 
			'settings' : [self.buffer[-1]['settings'][0], self.buffer[-1]['settings'][1]]})

			self.buffer.pop(-1)

	def pr(self,event):
		print(event.x, event.y)

	def draw_label(self,event):
		# lbl = Label(self.canv, text = 'kinda sus', bg='yellow').place(x=event.x, y=event.y)
		self.canv.create_text(event.x, event.y, text="This text is kinda sus")

	def Save(self):
		file_name = fd.asksaveasfilename(filetypes=([("IMAGE files", ".png")]))
		if file_name:
			ps = self.canv.postscript(colormode='color')
			im = Image.open(io.BytesIO(ps.encode('utf-8')))
			im.save(file_name)
		print(file_name)
		
	def set_size(self, width, height):
		if width and height:
			self.canvas_width = width
			self.canvas_height = height
			self.canv.configure(width=width,height=height)


	def set_size_window(self):

		self.Frame1 = Frame(Toplevel())

		self.Frame1.pack(fill=BOTH, expand=1)

		self.Frame1.columnconfigure(7, weight=1)
		self.Frame1.rowconfigure(3, weight=1)

		width_label = Label(self.Frame1, text="Canvas width: ")
		width_label.grid(row=0, column=0, padx=6)

		height_label = Label(self.Frame1, text="Canvas height: ")
		height_label.grid(row=1, column=0, padx=6)

		width_entry = Entry(self.Frame1, width=10)
		width_entry.grid(row=0, column=1)

		height_entry = Entry(self.Frame1, width=10)
		height_entry.grid(row=1, column=1)

		except_btn = Button(self.Frame1, text="Ok", width=10, command=lambda: self.set_size(width_entry.get(), height_entry.get()))
		except_btn.grid(row=0, column=2) 

		cancel_btn = Button(self.Frame1, text="Cancel", width=10)
		cancel_btn.grid(row=1, column=2) 
		

	def setUI(self):

		self.draw_menu()

		self.Frame.pack(fill=BOTH, expand=1)

		self.Frame.columnconfigure(7, weight=1)
		self.Frame.rowconfigure(3, weight=1)

		self.canv = Canvas(self.Frame, bg="white", width=self.canvas_width, height=self.canvas_height)  # Создаем поле для рисования, устанавливаем белый фон
		self.canv.grid(row=3, column=1, columnspan=7)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна

		self.canv.bind("<B1-Motion>", self.draw0) # Привязываем обработчик к канвасу. <B1-Motion> означает "при движении зажатой левой кнопки мыши" вызывать функцию draw
		self.canv.bind("<Button-1>", self.draw1)
		self.canv.bind("<Button-2>", self.draw_label)

		self.canv.bind_all('<Command-z>', self.deleting)
		self.canv.bind_all('<Command-y>', self.returning)
		self.canv.bind_all('<Command-x>', lambda x: self.canv.delete("all"))
		self.canv.bind_all('<Command-s>', self.Save)

		color_lab = Label(self.Frame, text="Color: ") # Создаем метку для кнопок изменения цвета кисти
		color_lab.grid(row=0, column=0, padx=6) # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей

		red_btn = Button(self.Frame, text="Change color", width=10,
			 			command=lambda: self.set_color(tkinter.colorchooser.askcolor()[0])) # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов), функция вызываемая при нажатии кнопки.
		red_btn.grid(row=0, column=1) # Устанавливаем кнопки

		clear_btn = Button(self.Frame, text="Clear all", width=10,
			 			command=lambda: self.canv.delete("all"))
		clear_btn.grid(row=0, column=5, sticky=W)

		size_lab = Label(self.Frame, text="Brush size: ")
		size_lab.grid(row=1, column=0, padx=5)

		one_btn = Button(self.Frame, text="Change size", width=10,
			 			command=lambda: self.set_brush_size(entry))
		one_btn.grid(row=1, column=1)

		entry = Entry(self.Frame, width=10)
		entry.grid(row=1, column=2)

		tri_btn = Button(self.Frame, text="sus", width=10,
			 			command=lambda: self.deleting(self))
		tri_btn.grid(row=0, column=2)

		chetiri_btn = Button(self.Frame, text="antisus", width=10,
			 			command=lambda: self.returning(self))
		chetiri_btn.grid(row=0, column=3)

		



	def draw_menu(self):
		menu_bar = Menu(self.root)
		self.root.configure(menu=menu_bar)

		file_menu = Menu(menu_bar, tearoff=0)
		file_menu.add_command(label='Сохранить Файл', command=self.Save)
		file_menu.add_command(label='Изменить размеры канваса', command=self.set_size_window)

		menu_bar.add_cascade(label="Файл",
                     menu=file_menu)
	
	def create_window(self, width, height, title="Пеинт на минималках", resizable=(False, False), icon=None):
		ChildWindow(self.root, width, height, title, resizable, icon)

	def Run(self):
		self.setUI()
		self.root.mainloop()

def main():
	MainWindow = Paint(720, 720)
	# MainWindow.create_window(200, 200)
	MainWindow.Run()
	


if __name__ == '__main__':
	main()