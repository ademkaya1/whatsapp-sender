import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)


# creating the App class
class MyApp(App):

    def build(self):
        Fl = FloatLayout()

        btn = Button(text='Hello world',
                     size_hint=(.3, .2),
                     pos=(300, 350))
        Fl.add_widget(btn)

        return Fl

if __name__ == "__main__":
    MyApp().run()