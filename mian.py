from tkinter import *
from math import *
import tkinter.colorchooser
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter import font
import io

# from child_window import ChildWindow

class Paint:
	def __init__(self, width, height, title="Пеинт на минималках", resizable=(True, True), icon=None ):
		self.root = Tk()
		self.root.title(title)
		self.root.geometry(f"{width}x{height}+200+200")
		self.root.resizable(resizable[0],resizable[1])

		if icon:
			self.root.iconbitmap(icon)  

		self.Frame = Frame(self.root)
		self.state = 'b'

		self.cords = [0,0,0,0]
		self.brush_color = 'red'
		self.brush_size = 2

		self.canvas_width = 512
		self.canvas_height = 512

		self.created_items = list()
		self.created_items_bufer = list()

		self.fast_menu_bar = list()

		self.text = 'Hello World!'
		self.text_color = 'black'
		self.text_font = 'TimesNewRoman'
		self.text_size = 12


		self.figure_color = 'green'
		self.insert_element = 'rectangle'
		self.figure_x = 0
		self.figure_y = 0
		self.new_image = ''

		self.movable = False
		self.movable_elements = []


	def set_color(self, new_color):
		if new_color:
			self.brush_color = "#%02x%02x%02x" % new_color
			

	def set_brush_size(self, new_size):
		if new_size:
			self.brush_size = new_size

	def draw0(self, event):
		self.cords.append(event.x)
		self.cords.append(event.y)
		self.canv.coords(self.created_items[-1]['line'], *self.cords)

	def draw1(self, event):
		self.cords = [event.x, event.y, event.x, event.y]
		self.created_items.append({'type': 'line',
								'line' : self.canv.create_line(self.cords, width=self.brush_size, fill=self.brush_color),
								'settings' : [self.brush_size, self.brush_color]})

	def deleting(self, event):
		if len(self.created_items):
			if self.created_items[-1]['type'] == 'line':

				self.created_items_bufer.append({'type': self.created_items[-1]['type'],
												'line' : self.canv.coords(self.created_items[-1]['line']), 
												'settings' : [ self.created_items[-1]['settings'][0], 
															self.created_items[-1]['settings'][1]]})


				self.canv.delete(self.created_items[-1]['line'])
				self.created_items.pop()

			elif self.created_items[-1]['type'] == 'text':

				self.created_items_bufer.append({'type': self.created_items[-1]['type'],
												'text' : self.canv.coords(self.created_items[-1]['text']), 
												'settings' : [ self.created_items[-1]['settings'][0], 
															self.created_items[-1]['settings'][1], 
															self.created_items[-1]['settings'][2],
															self.created_items[-1]['settings'][3]]})


				self.canv.delete(self.created_items[-1]['text'])
				self.created_items.pop()

			elif self.created_items[-1]['type'] == 'oval':

				self.created_items_bufer.append({'type': self.created_items[-1]['type'],
												'oval' : self.canv.coords(self.created_items[-1]['oval']), 
												'settings' : [ self.created_items[-1]['settings'][0], 
															self.created_items[-1]['settings'][1], 
															self.created_items[-1]['settings'][2],]})


				self.canv.delete(self.created_items[-1]['oval'])
				self.created_items.pop()

			elif self.created_items[-1]['type'] == 'rectangle':

				self.created_items_bufer.append({'type': self.created_items[-1]['type'],
												'rectangle' : self.canv.coords(self.created_items[-1]['rectangle']), 
												'settings' : [ self.created_items[-1]['settings'][0], 
															self.created_items[-1]['settings'][1], 
															self.created_items[-1]['settings'][2],]})


				self.canv.delete(self.created_items[-1]['rectangle'])
				self.created_items.pop()

			elif self.created_items[-1]['type'] == 'image':

				self.created_items_bufer.append({'type': self.created_items[-1]['type'],
												'image' : self.canv.coords(self.created_items[-1]['image']), 
												'settings' : [ self.created_items[-1]['settings'][0]]})


				self.canv.delete(self.created_items[-1]['image'])
				self.created_items.pop()

			# print(self.created_items_bufer)

	def returning(self, event):

		if len(self.created_items_bufer):
			if self.created_items_bufer[-1]['type'] == 'line':
				self.created_items.append({'type' : self.created_items_bufer[-1]['type'],
										'line' : self.canv.create_line(self.created_items_bufer[-1]['line'], 
																	width=self.created_items_bufer[-1]['settings'][0], 
																	fill=self.created_items_bufer[-1]['settings'][1]), 
										'settings' : [self.created_items_bufer[-1]['settings'][0], self.created_items_bufer[-1]['settings'][1]]})

				self.created_items_bufer.pop(-1)
				

			elif self.created_items_bufer[-1]['type'] == 'text':
				
				self.created_items.append({'type' : self.created_items_bufer[-1]['type'],
										'text' : self.canv.create_text(self.created_items_bufer[-1]['text'], 
																	text=self.created_items_bufer[-1]['settings'][0],
																	fill=self.created_items_bufer[-1]['settings'][1],
																	font=[self.created_items_bufer[-1]['settings'][2], self.created_items_bufer[-1]['settings'][3]]), 
										'settings' : [self.created_items_bufer[-1]['settings'][0], 
													self.created_items_bufer[-1]['settings'][1], 
													self.created_items_bufer[-1]['settings'][2], 
													self.created_items_bufer[-1]['settings'][3]]})

				self.created_items_bufer.pop(-1)

			elif self.created_items_bufer[-1]['type'] == 'oval':
				
				self.created_items.append({'type' : self.created_items_bufer[-1]['type'],
										'oval' : self.canv.create_oval(self.created_items_bufer[-1]['oval'], 
																	fill=self.created_items_bufer[-1]['settings'][0],
																	outline=""), 
										'settings' : [self.created_items_bufer[-1]['settings'][0], 
													self.created_items_bufer[-1]['settings'][1], 
													self.created_items_bufer[-1]['settings'][2]]})

				self.created_items_bufer.pop(-1)

			elif self.created_items_bufer[-1]['type'] == 'rectangle':
				
				self.created_items.append({'type' : self.created_items_bufer[-1]['type'],
										'rectangle' : self.canv.create_rectangle(self.created_items_bufer[-1]['rectangle'], 
																	fill=self.created_items_bufer[-1]['settings'][0],
																	outline=""), 
										'settings' : [self.created_items_bufer[-1]['settings'][0], 
													self.created_items_bufer[-1]['settings'][1], 
													self.created_items_bufer[-1]['settings'][2]]})

				self.created_items_bufer.pop(-1)

			elif self.created_items_bufer[-1]['type'] == 'image':
				
				self.created_items.append({'type' : self.created_items_bufer[-1]['type'],
										'image' : self.canv.create_image(self.created_items_bufer[-1]['image'], 
																	image=self.created_items_bufer[-1]['settings'][0]), 
										'settings' : [self.created_items_bufer[-1]['settings'][0]]})

				self.created_items_bufer.pop(-1)

	# def pr(self,event):
	# 	print(event.x, event.y)

	def draw_label(self,event):
		self.created_items.append({'type' : 'text',
								'text': self.canv.create_text(event.x, 
															event.y, 
															text=self.text, 
															fill=self.text_color, 
															font=[self.text_font, self.text_size]), 
								'settings': [self.text,
											self.text_color, 
											self.text_font, 
											self.text_size]})


	def set_text_color(self, new_color):
		if new_color:
			self.text_color = "#%02x%02x%02x" % new_color

	def set_text_font(self, font_settings):
		if font_settings:
			self.text_font = font_settings[0]
			self.text_size = font_settings[0]

	def set_element_color(self, new_color):
		if new_color:
			self.figure_color = "#%02x%02x%02x" % new_color

	def set_insertion_type(self, new_type):
		self.insert_element = new_type

		if self.insert_element == 'image':
			file_path = fd.askopenfilename(filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
			# print(self.new_image)

			self.new_image = ImageTk.PhotoImage(Image.open(file_path))


	def insert_element_0(self, event):

		if self.insert_element == 'oval':
			self.canv.coords(self.created_items[-1]['oval'], self.figure_x, self.figure_y, event.x, event.y)
			self.created_items[-1]['settings'][1] = abs(self.figure_x - event.x)
			self.created_items[-1]['settings'][2] = abs(self.figure_y - event.y)

		elif self.insert_element == 'rectangle':
			self.canv.coords(self.created_items[-1]['rectangle'], self.figure_x, self.figure_y, event.x, event.y)
			self.created_items[-1]['settings'][1] = abs(self.figure_x - event.x)
			self.created_items[-1]['settings'][2] = abs(self.figure_y - event.y)



	def insert_element_1(self, event):
		self.figure_x = event.x
		self.figure_y = event.y

		if self.insert_element == 'oval':
			self.created_items.append({'type' : 'oval',
									'oval': self.canv.create_oval(event.x, 
																event.y,
																event.x,
																event.y,
																fill=self.figure_color,
																outline=""), 
									'settings': [self.figure_color, self.figure_x, self.figure_y]})

		elif self.insert_element == 'rectangle':
			self.created_items.append({'type' : 'rectangle',
									'rectangle': self.canv.create_rectangle(event.x, 
																event.y,
																event.x,
																event.y,
																fill=self.figure_color,
																outline=""), 
									'settings': [self.figure_color, self.figure_x, self.figure_y]})

		elif self.insert_element == 'image':
			self.created_items.append({'type' : 'image',
								'image': self.canv.create_image(event.x, 
															event.y, 
															image=self.new_image), 
								'settings': [self.new_image]})
			pass	

	def Save(self):
		file_name = fd.asksaveasfilename(filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
		if file_name:
			ps = self.canv.postscript(colormode='color')
			im = Image.open(io.BytesIO(ps.encode('utf-8')))
			im.save(file_name)
		# print(file_name)
		
	def set_size(self, width, height):
		if width:
			self.canvas_width = width
			self.canv.configure(width=width)
		if height:
			self.canvas_height = height
			self.canv.configure(height=height)


	def set_size_window(self):

		self.root2 = Toplevel(self.root)
		self.root2.resizable(False, False)

		self.Frame1 = Frame(self.root2)

		self.Frame1.pack(fill=BOTH, expand=1)

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

		cancel_btn = Button(self.Frame1, text="Cancel", width=10, command=lambda:self.root2.destroy())
		cancel_btn.grid(row=1, column=2) 

	def delete_fast_menu_bar(self):
		for element in self.fast_menu_bar:
			element.destroy()

		self.fast_menu_bar = list()

	def change_state(self, event, new_state):
		self.state = new_state
		# print(self.state)

		if self.state == 'b':
			self.canv.bind("<B1-Motion>", self.draw0) 
			self.canv.bind("<Button-1>", self.draw1)
			self.state_b()

		if self.state == 't':
			# print(123)
			self.canv.bind("<Button-1>", self.draw_label)
			self.canv.unbind("<B1-Motion>") 
			self.state_t()

		if self.state == 'f':
			self.canv.bind("<B1-Motion>", self.insert_element_0) 
			self.canv.bind("<Button-1>", self.insert_element_1)
			self.state_f()

		if self.state == 'm':
			self.canv.unbind("<B1-Motion>") 
			self.canv.unbind("<Button-1>")
			self.state_m()

	def start_movement(self, event, a):
		widget = event.widget
		x, y = widget.coords(a)
		widget.dx, widget.dy = event.x-x, event.y-y

	def movement(self, event, a):
		widget = event.widget
		widget.coords(a, (event.x-widget.dx, event.y-widget.dy))
		# print(a)

	def move_figure(self, event, a, width, height):
	    self.canv.coords(a, event.x - width//2, event.y - height//2, event.x + width//2, event.y + height//2)


	def state_b(self):

		self.delete_fast_menu_bar()

		self.fast_menu_bar.append(Button(self.Frame, 
										text="Change color", 
										width=10,
										command=lambda: self.set_color(tkinter.colorchooser.askcolor()[0])))
		self.fast_menu_bar[0].grid(row=0, column=0)

		self.fast_menu_bar.append(Button(self.Frame, 
										text="Change size", 
										width=10,
			 							command=lambda: self.set_brush_size(self.fast_menu_bar[2].get())))
		self.fast_menu_bar[1].grid(row=0, column=1)

		self.fast_menu_bar.append(Scale(self.Frame,
										from_=1, 
										to=50,
										orient=HORIZONTAL, 
										width=10))
		self.fast_menu_bar[2].grid(row=0, column=2)

	def state_t(self):

		self.delete_fast_menu_bar()

		self.fast_menu_bar.append(Button(self.Frame, 
										text="Change text", 
										width=10,
			 							command=lambda: self.change_txt(self.fast_menu_bar[1].get())))

		self.fast_menu_bar[0].grid(row=0, column=0)

		self.fast_menu_bar.append(Entry(self.Frame, 
										width=10))
		self.fast_menu_bar[1].grid(row=0, column=1)

		self.fast_menu_bar.append(Button(self.Frame, 
										text="Change color", 
										width=10,
										command=lambda: self.set_text_color(tkinter.colorchooser.askcolor()[0])))
		self.fast_menu_bar[2].grid(row=0, column=2)

		self.fast_menu_bar.append(Button(self.Frame, 
										text="Change font", 
										width=10,
										command=lambda: self.font_chooser()))
		self.fast_menu_bar[3].grid(row=0, column=3)

	def state_f(self):

		self.delete_fast_menu_bar()

		self.fast_menu_bar.append(Button(self.Frame, 
										text="Insert Image", 
										width=10,
										command=lambda: self.set_insertion_type('image')))
		self.fast_menu_bar[0].grid(row=0, column=0)

		self.fast_menu_bar.append(Button(self.Frame, 
										text="Insert Oval", 
										width=10,
										command=lambda: self.set_insertion_type('oval')))
		self.fast_menu_bar[1].grid(row=0, column=1)

		self.fast_menu_bar.append(Button(self.Frame, 
										text="Insert Rectangle", 
										width=10,
										command=lambda: self.set_insertion_type('rectangle')))
		self.fast_menu_bar[2].grid(row=0, column=2)

		self.fast_menu_bar.append(Button(self.Frame, 
										text="Change color", 
										width=10,
										command=lambda: self.set_element_color(tkinter.colorchooser.askcolor()[0])))
		self.fast_menu_bar[3].grid(row=0, column=3)

	# def state_m(self):

	# 	self.delete_fast_menu_bar()

	# 	for elem in self.created_items:
	# 		# print(elem)
	# 		if elem['type'] == 'text':
	# 			self.movable_elements.append([self.canv.tag_bind(elem['text'],"<Button-1>", lambda event: self.start_movement(event, elem['text'])),
	# 										self.canv.tag_bind(elem['text'],'<B1-Motion>', lambda event: self.movement(event, elem['text'] ))])

	# 		elif elem['type'] == 'oval':
	# 			self.movable_elements.append(self.canv.tag_bind(elem['oval'], '<B1-Motion>', lambda event: self.move_figure(event, elem['oval'], elem['settings'][1], elem['settings'][2])))


	def return_font_settings(self, root, font_size, font_family):
		if font_family:
			self.text_font = font_family
		if font_size:
			self.text_size = font_size
		root.destroy()

	def validate(self, new_value):                                                  
		return new_value == "" or new_value.isnumeric()

	def font_chooser(self):

		self.root2 = Toplevel(self.root)
		self.root2.resizable(False, False)

		self.Frame1 = Frame(self.root2)

		self.Frame1.pack(fill=BOTH, expand=1)

		save_font_size = ''
		save_font_family = ''

		only_int = (self.root2.register(self.validate), '%P')

		font_size_label = Label(self.Frame1, text="font size: ")
		font_size_label.grid(row=0, column=0, padx=6)

		font_size_entry = Entry(self.Frame1, width=10, validate='key', validatecommand=only_int)
		font_size_entry.grid(row=0, column=1)

		font_family_listbox = Listbox(self.Frame1, selectmode=SINGLE, width=20)
		font_family_listbox.grid(row=1, column=0)

		for f in font.families():
			font_family_listbox.insert('end', f)

		except_btn = Button(self.Frame1, 
							text="Ok", 
							width=10, 
							command=lambda: self.return_font_settings(self.root2, font_size_entry.get(), font_family_listbox.get(font_family_listbox.curselection())))
		except_btn.grid(row=2, column=0) 

		cancel_btn = Button(self.Frame1, text="Cancel", width=10, command=lambda:self.root2.destroy())
		cancel_btn.grid(row=2, column=1) 

	def setUI(self):

		self.draw_menu()

		self.Frame.pack(fill=BOTH, expand=1)

		self.Frame.columnconfigure(7, weight=2)
		self.Frame.rowconfigure(3, weight=1)

		self.canv = Canvas(self.Frame, bg="white", width=self.canvas_width, height=self.canvas_height) 
		self.canv.grid(row=3, column=1, columnspan=7, rowspan=3)  

		if self.state == 'b':
			self.canv.bind("<B1-Motion>", self.draw0) 
			self.canv.bind("<Button-1>", self.draw1)
			self.state_b()

		self.canv.bind_all('<Command-z>', self.deleting)
		self.canv.bind_all('<Command-y>', self.returning)
		self.canv.bind_all('<Command-x>', lambda x: self.canv.delete("all"))
		self.canv.bind_all('<Command-s>', self.Save)

		self.canv.bind_all('<Command-Shift-B>', lambda event: self.change_state(event,'b'))
		self.canv.bind_all('<Command-Shift-T>', lambda event: self.change_state(event,'t'))
		# self.canv.bind_all('<Command-M>', lambda event: self.change_state(event,'m'))
		self.canv.bind_all('<Command-Shift-F>', lambda event: self.change_state(event,'f'))
		
	def change_txt(self, t):
		# print(1, )
		self.text = t

	def draw_menu(self):
		""" docstring"""
		menu_bar = Menu(self.root)
		self.root.configure(menu=menu_bar)

		file_menu = Menu(menu_bar, tearoff=0)
		file_menu.add_command(label='Сохранить Файл', command=self.Save)
		file_menu.add_command(label='Изменить размеры канваса', command=self.set_size_window)

		menu_bar.add_cascade(label="Файл",
                     menu=file_menu)

	def Run(self):
		self.setUI()
		self.root.mainloop()

def main():
	MainWindow = Paint(720, 720, icon='images/paint.png')
	# MainWindow.create_window(200, 200)
	MainWindow.Run()

if __name__ == '__main__':
	main()