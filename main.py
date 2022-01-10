from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivymd import app
from kivymd.app import *
from kivymd.uix.picker import *
from datetime import *
import pywhatkit as kit
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

class Whatsapp_Oto_Mesaj(App):
    def build(self):
        self.window = GridLayout()
        # self.window = FloatLayout(size=(900, 300))
        self.window.cols = 1
        self.window.size_hint = (0.5, 0.5)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.window.add_widget(Image(source="images\logo4.png"))
        # Window.clearcolor = (0, 0, 0, 0)



        self.ilgili_zaman = Label(text="Mesaj Gönderilecek Verileri Giriniz", font_size=18, color='#00FFCE')
        self.window.add_widget(self.ilgili_zaman)

        self.number = TextInput(multiline=False, padding_y=(10, 10), size_hint=(1, 0.5), input_filter='integer')
        self.window.add_widget(self.number)

        self.gonderim_saati = TextInput(multiline=False, padding_y=(10, 10), size_hint=(1, 0.5))
        self.window.add_widget(self.gonderim_saati)

        self.gonderim_dakikasi = TextInput(multiline=False, padding_y=(10, 10), size_hint=(1, 0.5))
        self.window.add_widget(self.gonderim_dakikasi)

        self.mesaj_icerik = TextInput(multiline=False, padding_y=(10, 10),
                                      size_hint=(1, 0.5))
        self.window.add_widget(self.mesaj_icerik)

        self.button = Button(text="Mesajı İlgili Saatte Yolla", size_hint=(0.5, 0.5), bold=True,
                             background_color='#00FFCE', pos=(450, 350), size=(200, 50))

        self.button.bind(on_press=self.gonder)

        self.window.add_widget(self.button)

        return self.window

    def gonder(self, instance):

        self.zaman = datetime.now()

        self.saat = self.gonderim_saati.text
        self.dakika = self.gonderim_dakikasi.text
        self.number_deneme = "+" + self.number.text
        self.ilgili_zaman.text = "Mesajınızın Gönderim Zamanı" + "  " + self.gonderim_saati.text + ":" + self.gonderim_dakikasi.text
        self.mesaj_icerikleri = self.mesaj_icerik.text


        try:
            kit.sendwhatmsg(self.number_deneme, self.mesaj_icerikleri, int(self.saat), int(self.dakika))
            print("Gönderdim abi")

        except:
            print("hata aldım  abi yollayamıyorum")


if __name__ == "__main__":
    Whatsapp_Oto_Mesaj().run()
