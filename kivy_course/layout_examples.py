from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

Builder.load_file('layout_examples.kv')


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "rl-tb"
        for i in range(0, 100):
            size = dp(100) #+ i*10
            b = Button(text=str(i + 1),
                       size_hint=(None, None),
                       size=(size, size))
            self.add_widget(b)


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExampleSec2(BoxLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    """
    ################## SEZIONE 1 ######################
    def __init__(self, **kwargs): #**kwargs serve per kivy
        super().__init__(**kwargs) #richiama le proprietà della classe interna
        #questa dichiarazione seguirà la grandezza della pagina

        #orientation cambia come vede i widget, horizontal di default
        self.orientation = 'vertical' #horizontal
        b1 = Button(text='A')
        b2 = Button(text='B')
        b3 = Button(text='C')
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    ################## SEZIONE 1 FINE ######################
    """


class MainWidget(Widget):
    pass