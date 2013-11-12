import os

import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.loader import Loader
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle


class FruitScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(FruitScreen, self).__init__(**kwargs)
        # to put into .kv file:
        with self.canvas.before:
            Color(.7,.8,1,1)
            self.rect=Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        sainsburys = self.load_image(pos_hint={'center_x': .7, 'center_y':.9},
                                                        size_hint=(.3,0))
        self.add_widget(sainsburys)

    # replace with .kv file
    def _update_rect(self, instance, value):
      self.rect.pos= instance.pos
      self.rect.size = instance.size

    def _image_loaded(self, proxy_image):
        if proxy_image.image.texture:
            self.image.texture = proxy_image.texture

    def load_image(self, **kwargs):
        this_dir = os.path.dirname(__file__)
        jpg = os.path.join(this_dir,'sainsbury_s.jpeg')
        return Image(source=jpg, **kwargs)
        # proxy_image = Loader.image(jpg)
        # proxy_image.bind(on_load=self._image_loaded)
        # return Image()


class FruitMainScreen(FruitScreen):
   def __init__(self, **kwargs):
        super(FruitMainScreen, self).__init__(**kwargs)

        btn = Button(text='Get products', size_hint=(.3,.1),
                             pos_hint={'center_x': .7, 'center_y':.7},
                             background_color=[238,238,0,1],
                             color=[0,0,0,1])
        self.add_widget(btn)

        label = Label(text='Welcome to the thing',
                              pos_hint={'center_x': .4, 'center_y':.45},
                              font_size=50,
                              color=[0,0,0,1])
        self.add_widget(label)



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
