from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
###################### FILE ORGANIZATION ##########################################
from navigation_screen_manager import NavigationScreenManager

'''Vediamo come importare la roba in un'app
Qui come possiamo vedere Abbiamo solo il run dell'app.
Tutto il codice è nel file layout example (senza App().run()) 
e li stesso viene inserito il Builder del suo file .kv (vd riga 10)
mentre nel main file .kv di questo progetto bisogna
importare quel file .py:
#:import layout_examples layout_examples '''

class MyScreenManager(NavigationScreenManager):
    pass

class MainMenu(NavigationScreenManager):
    pass

class NavigationApp(MDApp):
    '''creiamo una proprietà'''
    manager = ObjectProperty(None) #object può essere qualunque cosa

    '''evitiamo di chiamare l'interfaccio principale dal fil .kv '''
    def build(self):
        self.manager = MainMenu()
        #adesso posso riferirmi a qualunque proprietà come app.manager.function()
        return self.manager


if __name__ == "__main__":
    NavigationApp().run()
