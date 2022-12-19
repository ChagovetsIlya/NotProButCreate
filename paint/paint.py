from tkinter import *
import tkinter.colorchooser
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter import font
import io


class Paint:
    '''!Class Paint is the main class, containing  a content of all project. This Class contains all functions which
are responsible for the working process of the project.'''
    def __init__(self, width, height, title="Paint", resizable=(True, True)):
        '''!Function init is responsible for declaration of all variables, creating of the main canvas we should work with.
               Constructs all the necessary attributes for the person object.

        @param width(int): Width of the canvas , @param height(int): Height of the canvas, @param title(str): The title of the program
               '''
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])


        self.Frame = Frame(self.root, bg='#d3d3d3')
        self.state = 'b'

        self.cords = [0, 0, 0, 0]
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

    def set_color(self, new_color):
        '''!Function set_color is responsible for choosing color in the color palette
         @param new_color: new color of the brush '''
        if new_color:
            # print(new_color)
            self.brush_color = "#%02x%02x%02x" % new_color
            # print(self.brush_color)

    def set_brush_size(self, new_size):
        '''!Function set_brush_size is responsible for setting size of the brush for painting
        @param new_size: new size of the brush'''
        if new_size:
            self.brush_size = new_size

    def draw0(self, event):
        '''!Function draw0 is responsible for movements of the mouse to draw
        @param event: acting by click'''
        self.cords.append(event.x)
        self.cords.append(event.y)
        self.canv.coords(self.created_items[-1]['line'], *self.cords)

    def draw1(self, event):
        '''!Function draw1 is responsible for  event on click (drawing via click)
        @param event: acting by click'''
        self.cords = [event.x, event.y, event.x, event.y]
        self.created_items.append({'type': 'line',
                                   'line': self.canv.create_line(self.cords, width=self.brush_size,
                                                                 fill=self.brush_color),
                                   'settings': [self.brush_size, self.brush_color]})

    def deleting(self, event):
        '''!Function deleting is responsible for deliting process.
        @param event: acting by click'''
        if len(self.created_items):
            if self.created_items[-1]['type'] == 'line':

                self.created_items_bufer.append({'type': self.created_items[-1]['type'],
                                                 'line': self.canv.coords(self.created_items[-1]['line']),
                                                 'settings': [self.created_items[-1]['settings'][0],
                                                              self.created_items[-1]['settings'][1]]})

                self.canv.delete(self.created_items[-1]['line'])
                self.created_items.pop()

            elif self.created_items[-1]['type'] == 'text':

                self.created_items_bufer.append({'type': self.created_items[-1]['type'],
                                                 'text': self.canv.coords(self.created_items[-1]['text']),
                                                 'settings': [self.created_items[-1]['settings'][0],
                                                              self.created_items[-1]['settings'][1],
                                                              self.created_items[-1]['settings'][2],
                                                              self.created_items[-1]['settings'][3]]})

                self.canv.delete(self.created_items[-1]['text'])
                self.created_items.pop()

            elif self.created_items[-1]['type'] == 'oval':

                self.created_items_bufer.append({'type': self.created_items[-1]['type'],
                                                 'oval': self.canv.coords(self.created_items[-1]['oval']),
                                                 'settings': [self.created_items[-1]['settings'][0],
                                                              self.created_items[-1]['settings'][1],
                                                              self.created_items[-1]['settings'][2], ]})

                self.canv.delete(self.created_items[-1]['oval'])
                self.created_items.pop()

            elif self.created_items[-1]['type'] == 'rectangle':

                self.created_items_bufer.append({'type': self.created_items[-1]['type'],
                                                 'rectangle': self.canv.coords(self.created_items[-1]['rectangle']),
                                                 'settings': [self.created_items[-1]['settings'][0],
                                                              self.created_items[-1]['settings'][1],
                                                              self.created_items[-1]['settings'][2], ]})

                self.canv.delete(self.created_items[-1]['rectangle'])
                self.created_items.pop()

            elif self.created_items[-1]['type'] == 'image':

                self.created_items_bufer.append({'type': self.created_items[-1]['type'],
                                                 'image': self.canv.coords(self.created_items[-1]['image']),
                                                 'settings': [self.created_items[-1]['settings'][0]]})

                self.canv.delete(self.created_items[-1]['image'])
                self.created_items.pop()

        # print(self.created_items_bufer)

    def returning(self, event):
        '''!Function returning is responsible for returning cancelled line.
        @param event: acting by click'''
        if len(self.created_items_bufer):
            if self.created_items_bufer[-1]['type'] == 'line':
                self.created_items.append({'type': self.created_items_bufer[-1]['type'],
                                           'line': self.canv.create_line(self.created_items_bufer[-1]['line'],
                                                                         width=self.created_items_bufer[-1]['settings'][
                                                                             0],
                                                                         fill=self.created_items_bufer[-1]['settings'][
                                                                             1]),
                                           'settings': [self.created_items_bufer[-1]['settings'][0],
                                                        self.created_items_bufer[-1]['settings'][1]]})

                self.created_items_bufer.pop(-1)


            elif self.created_items_bufer[-1]['type'] == 'text':

                self.created_items.append({'type': self.created_items_bufer[-1]['type'],
                                           'text': self.canv.create_text(self.created_items_bufer[-1]['text'],
                                                                         text=self.created_items_bufer[-1]['settings'][
                                                                             0],
                                                                         fill=self.created_items_bufer[-1]['settings'][
                                                                             1],
                                                                         font=[self.created_items_bufer[-1]['settings'][
                                                                                   2],
                                                                               self.created_items_bufer[-1]['settings'][
                                                                                   3]]),
                                           'settings': [self.created_items_bufer[-1]['settings'][0],
                                                        self.created_items_bufer[-1]['settings'][1],
                                                        self.created_items_bufer[-1]['settings'][2],
                                                        self.created_items_bufer[-1]['settings'][3]]})

                self.created_items_bufer.pop(-1)

            elif self.created_items_bufer[-1]['type'] == 'oval':

                self.created_items.append({'type': self.created_items_bufer[-1]['type'],
                                           'oval': self.canv.create_oval(self.created_items_bufer[-1]['oval'],
                                                                         fill=self.created_items_bufer[-1]['settings'][
                                                                             0],
                                                                         outline=""),
                                           'settings': [self.created_items_bufer[-1]['settings'][0],
                                                        self.created_items_bufer[-1]['settings'][1],
                                                        self.created_items_bufer[-1]['settings'][2]]})

                self.created_items_bufer.pop(-1)

            elif self.created_items_bufer[-1]['type'] == 'rectangle':

                self.created_items.append({'type': self.created_items_bufer[-1]['type'],
                                           'rectangle': self.canv.create_rectangle(
                                               self.created_items_bufer[-1]['rectangle'],
                                               fill=self.created_items_bufer[-1]['settings'][0],
                                               outline=""),
                                           'settings': [self.created_items_bufer[-1]['settings'][0],
                                                        self.created_items_bufer[-1]['settings'][1],
                                                        self.created_items_bufer[-1]['settings'][2]]})

                self.created_items_bufer.pop(-1)

            elif self.created_items_bufer[-1]['type'] == 'image':

                self.created_items.append({'type': self.created_items_bufer[-1]['type'],
                                           'image': self.canv.create_image(self.created_items_bufer[-1]['image'],
                                                                           image=
                                                                           self.created_items_bufer[-1]['settings'][0]),
                                           'settings': [self.created_items_bufer[-1]['settings'][0]]})

                self.created_items_bufer.pop(-1)

    # def pr(self,event):
    # 	print(event.x, event.y)

    def draw_label(self, event):
        '''!Function draw_label is responsible for creating a label filled with text. This label will appear
        in the place where you click.
        @param event: acting by click'''
        self.created_items.append({'type': 'text',
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
        '''!Function set_text_color set a new color of the text.
        @param new_color: set new color of the text
        '''
        if new_color:
            self.text_color = "#%02x%02x%02x" % new_color

    def set_text_font(self, font_settings):
        '''!Function set_text_color set a new font of the text.
        @param font_settings: set new font of the text
        '''
        if font_settings:
            self.text_font = font_settings[0]
            self.text_size = font_settings[0]

    def set_element_color(self, new_color):
        '''!Function set_element_color gives an opportunity to choose any color of the chosen element.
        @param new_color: new color of the element'''
        if new_color:
            self.figure_color = "#%02x%02x%02x" % new_color

    def set_insertion_type(self, new_type):
        '''!Function set_insertion_type change the type of the inserted element
        @param new_type: new type of the inserted element'''
        self.insert_element = new_type

        if self.insert_element == 'image':
            file_path = fd.askopenfilename(filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
            # print(self.new_image)

            self.new_image = ImageTk.PhotoImage(Image.open(file_path))

    def insert_element_0(self, event):
        '''!Function insert_element0 allows create ovals and rectangles, change their sizes
        @param event: act by click'''
        if self.insert_element == 'oval':
            self.canv.coords(self.created_items[-1]['oval'], self.figure_x, self.figure_y, event.x, event.y)
            self.created_items[-1]['settings'][1] = abs(self.figure_x - event.x)
            self.created_items[-1]['settings'][2] = abs(self.figure_y - event.y)

        elif self.insert_element == 'rectangle':
            self.canv.coords(self.created_items[-1]['rectangle'], self.figure_x, self.figure_y, event.x, event.y)
            self.created_items[-1]['settings'][1] = abs(self.figure_x - event.x)
            self.created_items[-1]['settings'][2] = abs(self.figure_y - event.y)

    def insert_element_1(self, event):
        '''!Function insert_element_1 allows change the color, size of the element.
         @param event: act by click'''
        self.figure_x = event.x
        self.figure_y = event.y

        if self.insert_element == 'oval':
            self.created_items.append({'type': 'oval',
                                       'oval': self.canv.create_oval(event.x,
                                                                     event.y,
                                                                     event.x,
                                                                     event.y,
                                                                     fill=self.figure_color,
                                                                     outline=""),
                                       'settings': [self.figure_color, self.figure_x, self.figure_y]})

        elif self.insert_element == 'rectangle':
            self.created_items.append({'type': 'rectangle',
                                       'rectangle': self.canv.create_rectangle(event.x,
                                                                               event.y,
                                                                               event.x,
                                                                               event.y,
                                                                               fill=self.figure_color,
                                                                               outline=""),
                                       'settings': [self.figure_color, self.figure_x, self.figure_y]})

        elif self.insert_element == 'image':
            self.created_items.append({'type': 'image',
                                       'image': self.canv.create_image(event.x,
                                                                       event.y,
                                                                       image=self.new_image),
                                       'settings': [self.new_image]})
            pass

    def Save(self):
        '''!Function Save is responsible for saving the canvas in the PNG format.'''
        file_name = fd.asksaveasfilename(filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
        # print(file_name)
        if file_name:
            ps = self.canv.postscript(colormode='color')
            im = Image.open(io.BytesIO(ps.encode('utf-8')))
            im.save(file_name)

    # print(file_name)

    def set_size(self, width, height):
        '''!Function set_size is responsible for choosing the size of the canvas. You can choose any height and width in pixels.
        @param height: height of the canvas in pixels, @param  width: width of the canvas in pixels'''
        if width:
            self.canvas_width = width
            self.canv.configure(width=width)
        if height:
            self.canvas_height = height
            self.canv.configure(height=height)

    def set_size_window(self):
        '''!Function set_size_window is responsible for setting a size of whole window. This function contains  2 buttons:
        OK button except written height and width and apply them to the window
        CANCEL button reject these written parameters.'''

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

        except_btn = Button(self.Frame1, text="Ok", width=10,
                            command=lambda: self.set_size(width_entry.get(), height_entry.get()))
        except_btn.grid(row=0, column=2)

        cancel_btn = Button(self.Frame1, text="Cancel", width=10, command=lambda: self.root2.destroy())
        cancel_btn.grid(row=1, column=2)

    def delete_fast_menu_bar(self):
        '''!Function delete_fast_menu_bar deletes elements from a menu bar.'''
        for element in self.fast_menu_bar:
            element.destroy()

        self.fast_menu_bar = list()

    def change_state(self, event, new_state):
        '''!Function change_state is responsible for changing current state to another:/n
        With press B a state will be 'drawing'/n
        With press T a state will be 'set text label on click'/n
        With press F a state will be ' inserting elements'/n
        This function gives an opportunity to speed up your work. You should not to switch the items by yourself,/n
        you can just press the required button and continue work/n

        @param event: act by click, @param new_state: replace the current state with a new one by pressing a button
                 '''
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




    def state_b(self):
        '''!Function state_b is responsible for the state on the button B: drawing with a brush'''

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
        '''!Function state_t is responsible for the state on the button T: a special menu bar for writing a text.'''
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
        '''!Function state_f is responsible for the state on the button F: a special menu bar for working with the elements (image/figure) appear.'''
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



    def return_font_settings(self, root, font_size, font_family):
        '''!Function return_font_settings changes the font and size of the inserted text.
        @param root: main canvas, @param font_size(int): size of the font, @param font_family: name of the family of the font.'''
        if font_family:
            self.text_font = font_family
        if font_size:
            self.text_size = font_size
        root.destroy()

    def validate(self, new_value):
        '''!Function validate checks if input is a number'''
        return new_value == "" or new_value.isnumeric()

    def font_chooser(self):
        '''!Function font_chooser allows to choose font family from the list. '''
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
                            command=lambda: self.return_font_settings(self.root2, font_size_entry.get(),
                                                                      font_family_listbox.get(
                                                                          font_family_listbox.curselection())))
        except_btn.grid(row=2, column=0)

        cancel_btn = Button(self.Frame1, text="Cancel", width=10, command=lambda: self.root2.destroy())
        cancel_btn.grid(row=2, column=1)

    def setUI(self):
        '''!Function setUI set all UI components: buttons, menu, grid.
        '''
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

        self.canv.bind_all('<Command-b>', lambda event: self.change_state(event, 'b'))
        self.canv.bind_all('<Command-t>', lambda event: self.change_state(event, 't'))
        # self.canv.bind_all('<Command-M>', lambda event: self.change_state(event,'m'))
        self.canv.bind_all('<Command-f>', lambda event: self.change_state(event, 'f'))

    def change_txt(self, t):
        '''!Function change_text is responsible for changing text in text label.
        @param t: change the state to the 't' state (mentioned above) '''
        # print(1, )
        self.text = t

    def draw_menu(self):
        '''!Function draw_menu is responsible for draw menu bar with functions like saving canvas, changing the canvas' size.'''
        menu_bar = Menu(self.root)
        self.root.configure(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Сохранить Файл', command=self.Save)
        file_menu.add_command(label='Изменить размеры канваса', command=self.set_size_window)

        menu_bar.add_cascade(label="Файл",
                             menu=file_menu)

    def Run(self):
        '''!Function Run puts all script into action. '''
        self.setUI()
        self.root.mainloop()


def main():
    '''!Function main runs the class Paint with all attributes.'''
    MainWindow = Paint(720, 720)
    MainWindow.Run()


if __name__ == '__main__':
    main()


