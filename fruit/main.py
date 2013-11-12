import os

import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.loader import Loader
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.gridlayout import GridLayout

# class PeopScreen(GridLayout):
#     def __init__(self, **kwargs):
#         super(PeopScreen, self).__init__(**kwargs)
#         for i in xrange(10):
#             self.add_widget(Label(text='Hello%d' % i))
#             self.add_widget(Label(text='World%d' % i))


class FruitMainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(FruitMainScreen, self).__init__(**kwargs)
        self.image = self.load_image()
        btn = Button(text='Get products', size_hint=(.3,.1),
                             pos_hint={'center_x': .7, 'center_y':.8},
                             background_color=[238,238,0,1],
                             color=[0,0,0,1]
                             )
        self.add_widget(btn)
        label = Label(text='Welcome to the thing',
                              pos_hint={'center_x': .4, 'center_y':.5},
                              font_size=50
                              )
        self.add_widget(label)

    def _image_loaded(self, proxy_image):
        if proxy_image.image.texture:
            self.image.texture = proxy_image.texture

    def load_image(self):
        this_dir = os.path.dirname(__file__)
        jpg = os.path.join(this_dir,'sainsbury_s.jpeg')
        proxy_image = Loader.image(jpg)
        proxy_image.bind(on_load=self._image_loaded)
        return Image()

class Fruit(App):
    def build(self):
        return FruitMainScreen()

    # def on_touch_move(self, touch):
    #     print(touch.profile)
    #     return super(Peops, self).on_touch_move(touch)

    # def on_touch_down(self, touch):
    #     print(touch.profile)
    #     return super(Peops, self).on_touch_move(touch)

if __name__ == '__main__':
    Fruit().run()
