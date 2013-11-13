import os
import weakref

import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.loader import Loader
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ListProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import FadeTransition


PAGE_BACKGROUND_COLOR=[.7,.8,1,1]
BUTTON_COLOR = [2,.95,.2,1]
BLACK = [0,0,0,1]

STORAGE={'apples':  {'price':1.99, 'description': 'nice and juicy'},
                    'oranges': {'description': 'round and tea-mobile'},
                    'pears': {},
                    'bananas': {},
                    'strawberries': {},
                    'pineapples': {},
                    'lychees' :{},
                    'guavas': {},
                    'raspberries': {},
                    'mangoes': {},
                    'clementines':{},
                    'satsumas': {},
                    'pomegranates': {},

                    }


class FruitScreen(Screen):

    def __init__(self, **kwargs):
        super(FruitScreen, self).__init__(**kwargs)
        # to put into .kv file:
        with self.canvas.before:
            Color(*PAGE_BACKGROUND_COLOR)
            self.rect=Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        sainsburys = self.load_image(pos_hint={'center_x': .5, 'center_y':.9},
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

        btn = Button(text='List products', size_hint=(.28,.08),
                             pos_hint={'center_x': .5, 'center_y':.5},
                             background_color=BUTTON_COLOR,
                             color=BLACK,
                             on_release=self.on_release)
        self.add_widget(btn)


    def on_release(self, event):
        self.manager.current = self.manager.next()


class FruitListScreen(FruitScreen):
    def __init__(self, **kwargs):
        super(FruitListScreen, self).__init__(**kwargs)

        btn = Button(text='back', size_hint=(.15,.07),
                             pos_hint={'center_x': .2, 'center_y':.9},
                             background_color=BUTTON_COLOR,
                             color=BLACK,
                             on_release=self.on_release)
        self.add_widget(btn)

        list_widget = FruitListWidget(size_hint=(1, .8),
                                                pos_hint = {'center_x': .5, 'center_y':.4})
        self.add_widget(list_widget)

    def on_release(self, event):
        self.manager.current = self.manager.previous()


class FruitDetailScreen(FruitScreen):
    fruit_name='unset'
    def __init__(self, **kwargs):
        super(FruitDetailScreen, self).__init__(**kwargs)

        btn = Button(text='back', size_hint=(.15,.07),
                             pos_hint={'center_x': .2, 'center_y':.9},
                             background_color=BUTTON_COLOR,
                             color=BLACK,
                             on_release=self.on_release)

        self.add_widget(btn)
        self.slate = FloatLayout(size_hint=(1, .8))
        self.add_widget(self.slate)

    def on_enter(self):
        details = Label(text=self.fruit_name)
        self.slate.add_widget(details)

    def on_leave(self):
        self.slate.clear_widgets()
        self.fruit_name='unset'

    def on_release(self, event):
        self.manager.current = self.manager.previous()


class FruitListWidget(ScrollView):

    def __init__(self, **kwargs):
        super(FruitListWidget, self).__init__(**kwargs)
        self.build_grid()

    def get_names(self):
        return sorted(STORAGE)

    def build_grid(self):

        grid = BoxLayout(orientation='vertical')
        #grid.bind(minimum_height=grid.setter('height'))
        for name in self.get_names():
            btn = FruitNameButton(text=name,
                                                  color=BLACK,
                                                  background_color=[2,2,2,1],
                                                  text_size=(700,None),
                                                  )
            grid.add_widget(btn)

        self.add_widget(grid)


class FruitNameButton(Button):
    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos

        super(FruitNameButton, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        screen_manager = self.parent.parent.parent.manager
        screen_manager.current = screen_manager.next()
        screen_manager.current_screen.fruit_name = instance.text


class Fruit(App):
    def build(self):
        root = ScreenManager(transition=FadeTransition())
        root.add_widget(FruitMainScreen())
        root.add_widget(FruitListScreen())
        root.add_widget(FruitDetailScreen())
        return root


if __name__ == '__main__':
    Fruit().run()
