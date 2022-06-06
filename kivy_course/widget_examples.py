from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

Builder.load_file('widget_examples.kv')

class CounterExample(GridLayout):
    my_text = StringProperty("0")
    slider_text = StringProperty("50")
    counter = 0
    input_text = StringProperty("foo")

    def on_button_click(self, tog):
        if tog.state == 'down':
            self.counter += 1
            self.my_text = str(self.counter)

    def on_toggle_botton_state(self, tog, incr):
        if tog.state == 'normal':
            tog.text = 'OFF'
            incr.disabled = True
        else:
            tog.text = 'ON'
            incr.disabled = False

    def on_switch_active(self, switch):
        print("Switch: " + str(switch.active))

    def on_slider_value(self, slider):
        print("Switch: " + str(int(slider.value)))

    def display_slider(self, slider, label):
        self.slider_text = str(int(slider.value))
        label.text = self.slider_text

    def on_text_validate(self, input):
        self.input_text = input.text


class WidgetExample(GridLayout):
    my_text = StringProperty("MBARE")  # valore di default è MBARE

    def on_button_click(self):
        self.my_text = 'bravo sai cliccare'

    def on_toggle_botton_state(self, toggle):
        if toggle.state == "normal":
            toggle.text = 'OFF'
        else:
            toggle.text = 'ON'