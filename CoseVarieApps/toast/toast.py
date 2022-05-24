from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton
from kivymd.uix.tooltip import MDTooltip

KV = '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        id: toolbar
        title: 'Test Toast'
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: '']]

    FloatLayout:
        
        TooltipMDIconButton:
            icon: 'dog-side'
            tooltip_text:'icon'
            pos_hint: {'center_x': .5, 'center_y': .8}

        TooltipMDRaisedButton:
            text: 'TEST KIVY TOAST'
            tooltip_text:'button'
            on_release: app.show_toast()
            pos_hint: {'center_x': .5, 'center_y': .5}

<TooltipMDRaisedButton@MDRaisedButton+MDTooltip>:

'''


class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass


class Test(MDApp):
    def show_toast(self):
        '''Displays a toast on the screen.'''

        toast('Test Kivy Toast')

    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    Test().run()
    
###   https://github.com/kivy/kivy/tree/master/examples
