from kivy.app import App
from kivy.uix.image import AsyncImage


class ImmApp(App):
    def build(self):
        # img = Image(source='left.png') #importa immagine da locale
        img = AsyncImage(
            source='https://png.pngtree.com/png-clipart/20210502/original/pngtree-cute-pictures-png-image_6268821.png'
                        )         #importa immagine da link web (tasto dx --> copia l'indirizzo dell'immagine)
        return img


if __name__ == '__main__':
    ImmApp().run()
