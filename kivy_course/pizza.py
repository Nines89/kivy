from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import CoverBehavior

from models_pizza import Pizza


class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()

'''Mettiamo floatlayout perchè è come un widget ma anche come un layout
Tutto questo ci permette di lavorare con gli sfondi'''
class MainWidget(FloatLayout):
    #lo definiamo per poterne usare l'id
    recycleView = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizza = [
            Pizza("Margherita", "Pomodoro, mozzarella, basilico",
                                6, True),
            Pizza("Tonno e cipolla", "Pomodoro, mozzarella, tonno, cipolla",
                  7.5, False),
            Pizza("Bomba", "Pomodoro, mozzarella, wurstel, prosciutto, capperi, olive, salsiccia",
                  9, False)
        ]

    def on_parent(self, widget, parent):
        self.recycleView.data = [pizza.get_pizza_dict() for pizza in self.pizza]


with open("pizzascr.kv", encoding='utf8') as f:
    Builder.load_string(f.read())


class PizzaApp(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    PizzaApp().run()
