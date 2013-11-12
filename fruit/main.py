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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.screenmanager import SwapTransition
from kivy.uix.screenmanager import WipeTransition
from kivy.uix.screenmanager import FadeTransition


class FruitScreen(Screen):

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
        self.name = self.__class__.__name__

    # replace with .kv file
    def _update_rect(self, instance, value):
      self.rect.pos= instance.pos
      self.rect.size = instance.size

    def load_image(self, **kwargs):
        this_dir = os.path.dirname(__file__)
        jpg = os.path.join(this_dir,'sainsbury_s.jpeg')
        return Image(source=jpg, **kwargs)


class FruitMainScreen(FruitScreen):
    def __init__(self, **kwargs):

        super(FruitMainScreen, self).__init__(**kwargs)

        btn = Button(text='Get products', size_hint=(.3,.1),
                             pos_hint={'center_x': .7, 'center_y':.7},
                             background_color=[238,238,0,1],
                             color=[0,0,0,1],
                             on_release=self.on_release)
        self.add_widget(btn)

        label = Label(text='Welcome to the thing',
                              pos_hint={'center_x': .4, 'center_y':.45},
                              font_size=50,
                              color=[0,0,0,1])
        self.add_widget(label)

    def on_release(self, event):
        print self.manager.current
        self.manager.current = self.manager.next()
        print self.manager.current


class FruitListScreen(FruitScreen):
    def __init__(self, **kwargs):
        super(FruitListScreen, self).__init__(**kwargs)


class Fruit(App):
    def build(self):
        root = ScreenManager(transition=WipeTransition())
        root.add_widget(FruitMainScreen())
        root.add_widget(FruitListScreen())
        return root



if __name__ == '__main__':
    Fruit().run()
