from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        button = Button(text='print this', #testo
                        size_hint=(0.2, 0.2), #dimensione rispetto allo schermo
                        font_size='20sp', #dimensione font
                        pos_hint={'center_x': 0.5, 'center_y': 0.5}, #posizione nello schermo
                        on_press=self.print_press,
                        on_release=self.print_release,
                        )
        return button

    def print_press(self, obj): #obj serve di default
        print("button press")

    def print_release(self, obj): #obj serve di default
        print("button release")

if __name__ == '__main__':
    ButtonApp().run()
