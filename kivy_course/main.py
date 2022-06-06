from kivy.app import App
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.properties import StringProperty, NumericProperty, Clock
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.metrics import dp

################## SEZIONE 10 ###################################
class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        '''Di default la windows size è 100x100, in questo momento, 
        nell'init, non esiste la finestra. Ecco perché dare la posizione o la size
        al rettangolo sotto non riempie tutta la finestra
        Nel canvas 5 viene mostrato un  esempio'''
        with self.canvas:
            Color(0, 0, 1)
            self.rect = Rectangle(pos=(300, 100), size=(50, 50))
            Color(1, 1, 0)
            Line(points=(200, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(500, 300, 80))

    def move_rect(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x+w)
        #ricordati che le proprietà sono tuple,
        # quindi non ci puoi accedere tipo self.rect.pos[0]
        if diff < inc:
            inc = diff

        x += inc
        self.rect.pos = (x, y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        with self.canvas:
            Color(0,0,0)
            self.bg = Rectangle(pos=self.pos, size=self.size)
            Color(1,1,1)
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
            self.vx = dp(3)
            self.vy = dp(3)
        # questa istruzione richiama la funzione update ogni tot, in questo caso ogni sessantesimo
        Clock.schedule_interval(self.update, 1/60) #questa istruzione richiama la funzione update ogni tot
    '''questa funzione viene chiamata ogni volta che si setta il size della finestra'''
    def on_size(self, *args):
        #print('On size: ' + str(self.width) + ', ' + str(self.height))
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

    def update(self, dt):
        x, y = self.ball.pos

        # x, y sono le coordinate dell'angolo in basso a sinistra
        limit_x = x + self.ball_size
        limit_y = y + self.ball_size
        # siccome l'angolo di riferimento è quello in basso a sx
        limit_x_0 = x #+ self.ball_size
        limit_y_0 = y #+ self.ball_size

        #se supera i limiti le cambio la direzione
        if limit_x >= self.width or limit_x_0 <= 0:
            self.vx = -self.vx

        if limit_y >= self.height or limit_y_0 <= 0:
            self.vy = -self.vy

        x += self.vx
        y += self.vy
        self.ball.pos = (x, y)

    class CanvasExample6(Widget):
        pass

    class CanvasExample7(Widget):
        pass

################ FINE SEZIONE 10 ################################

################## ESERCIZIO COUNTER ##################################
class CounterExample(GridLayout):
    my_text = StringProperty("0") #valore di default è MBARE
    slider_text = StringProperty("50")
    counter = 0
    input_text = StringProperty("foo")
    def on_button_click(self,tog):
        if tog.state == 'down':
            self.counter += 1
            self.my_text = str(self.counter)


    '''Gli passiamo a questo il bottone, così da poterlo abilitare
    o disabilitare a piacimento'''
    def on_toggle_botton_state(self, tog, incr):
        if tog.state == 'normal':
            tog.text = 'OFF'
            incr.disabled = True
        else:
            tog.text = 'ON'
            incr.disabled = False

    def on_switch_active(self, switch):
        '''Per lo switch ci serve string, perché è un booleano'''
        print("Switch: " + str(switch.active))

    def on_slider_value(self, slider):
        '''Per lo slider ci serve string, perché è un numero
        questo numero è un float, posso sistemarlo con int'''
        print("Switch: " + str(int(slider.value)))

    def display_slider(self, slider, label):
        self.slider_text = str(int(slider.value))
        label.text = self.slider_text

    def on_text_validate(self, input):
        '''grazie a questa funzione viene scritta nel label
        solo quando valido il testo, non prima'''
        self.input_text = input.text
################## FINE ESERCIZIO COUNTER ##################################

################## SEZIONE 8 ##################################
'''Dobbiamo deginire la classe della sezione 8 in py
in quanto il bottone deve interagire con qualcosa
questa interazione si fa qui'''

class WidgetExample(GridLayout):
    '''funzione per il bottone'''
    '''gestisce le funzionalità di una stringa'''
    my_text = StringProperty("MBARE") #valore di default è MBARE

    def on_button_click(self):
        '''stavolta uso self
        se non lo mettessi lo tratterebbe come una variabile locale alla funzione.
        NO self nella dichiarazione, SI self per l'utilizzo'''
        self.my_text = 'bravo sai cliccare'

    def on_toggle_botton_state(self, toggle):
        '''toggle è il toggleButton che ho passato come selg nel file .kv'''
        '''Lo stato è down se attivato e normal se disattivato'''
        '''Visto che stiamo già passando a questa specifica funzione 
        quello specifico Widget, io posso cambiargli il testo qui stesso'''
        if toggle.state == "normal":
            toggle.text = 'OFF'
        else:
            toggle.text = 'ON'
################## FINE SEZIONE 8 ##################################

# ################## SEZIONE 5 ##################################
# class StackLayoutExample(StackLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = "rl-tb"
#         #Questo bottone sarà il primo ad essere piazzato
#         #l'init è la prima cosa ad essere posizionata
#         for i in range(0, 100):
#             size = dp(100) #+ i*10
#             b = Button(text=str(i + 1),
#                        size_hint=(None, None),
#                        size=(size, size))
#             self.add_widget(b)
#
# ################## FINE SEZIONE 5 ##################################
#
# ################## SEZIONE 4 ##################################
# # class GridLayoutExample(AnchorLayout):
# #   pass
# '''Se non volessi utilizzare la classe dentro Python devo definirla
# all'interno del file .kv come mostrato nella sezione 4
# Più o meno lo sappiamo già come si fa'''
# ################## FINE SEZIONE 4 ##################################
#
#
# class AnchorLayoutExample(AnchorLayout):
#     pass
#
#
# class BoxLayoutExampleSec2(BoxLayout):
#     pass
#
#
# class BoxLayoutExample(BoxLayout):
#     pass
#     """
#     ################## SEZIONE 1 ######################
#     def __init__(self, **kwargs): #**kwargs serve per kivy
#         super().__init__(**kwargs) #richiama le proprietà della classe interna
#         #questa dichiarazione seguirà la grandezza della pagina
#
#         #orientation cambia come vede i widget, horizontal di default
#         self.orientation = 'vertical' #horizontal
#         b1 = Button(text='A')
#         b2 = Button(text='B')
#         b3 = Button(text='C')
#         self.add_widget(b1)
#         self.add_widget(b2)
#         self.add_widget(b3)
#     ################## SEZIONE 1 FINE ######################
#     """
#
#
# class MainWidget(Widget):
#     pass


class TheLabApp(MDApp):
    pass


if __name__ == "__main__":
    TheLabApp().run()