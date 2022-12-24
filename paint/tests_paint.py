import unittest

import paint as pipi


class test_paint(unittest.TestCase):

    def test_delete_fast_menu_bar(self):
        p = pipi.Paint(300, 300)
        p.state_t()
        p.delete_fast_menu_bar()

        self.assertEqual(p.fast_menu_bar, [])
        
    def test_set_size(self):
        p = pipi.Paint(300, 300)

        p.setUI()
        self.assertEqual([p.canvas_width, p.canvas_height], [512, 512])

        p.set_size(400,100)

        self.assertEqual([p.canvas_width, p.canvas_height], [400, 100])

    def test_validate(self):
        p = pipi.Paint(300, 300)

        self.assertEqual(p.validate('3'),True)
        self.assertEqual(p.validate('privet'),False)

    def test_set_text_color(self):
        p = pipi.Paint(300, 300)

        self.assertEqual(p.text_color, 'black')

        p.set_text_color((0, 255, 0))
        self.assertEqual(p.text_color, '#00ff00')

        p.set_text_color('')
        self.assertEqual(p.text_color, '#00ff00')

    def test_set_color(self):
        p = pipi.Paint(300, 300)

        self.assertEqual(p.brush_color, 'red')

        p.set_color((0, 255, 0))
        self.assertEqual(p.brush_color, '#00ff00')

        p.set_color('')
        self.assertEqual(p.brush_color, '#00ff00')

    def test_set_element_color(self):
        p = pipi.Paint(300, 300)
        self.assertEqual(p.figure_color, 'green')

        p.set_element_color((0,255,0))
        self.assertEqual(p.figure_color, '#00ff00')

        p.set_element_color('')
        self.assertEqual(p.figure_color, '#00ff00')

    def test_change_txt(self):
        p = pipi.Paint(300, 300)

        self.assertEqual(p.text, 'Hello World!')

        p.change_txt('Hello')
        self.assertEqual(p.text, 'Hello')

    def test_set_brush_size(self):
        p = pipi.Paint(300, 300)

        self.assertEqual(p.brush_size, 2)

        p.set_brush_size(30)
        self.assertEqual(p.brush_size, 30)

        p.set_brush_size('')
        self.assertEqual(p.brush_size, 30)

        p.set_brush_size(0)
        self.assertEqual(p.brush_size, 30)

    def test_change_state(self):
        p = pipi.Paint(300, 300)
        p.setUI()

        p.change_state(1, 't')
        self.assertEqual(p.state , 't')

        p.change_state(1, 'b')
        self.assertEqual(p.state , 'b')

        p.change_state(1, 'f')
        self.assertEqual(p.state , 'f')

    def test_set_insertion_type(self):
        p = pipi.Paint(300, 300)

        self.assertEqual(p.insert_element , 'rectangle')

        p.set_insertion_type('oval')
        self.assertEqual(p.insert_element , 'oval')


        p.set_insertion_type('rectangle')
        self.assertEqual(p.insert_element , 'rectangle')

if __name__ == '__main__':
    unittest.main()
