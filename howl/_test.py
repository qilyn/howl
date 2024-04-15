
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.pagelayout import PageLayout

"""
HOWL

Accept no data, show only record.
"""

class DetailPageLayout(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        self.but0ni = Button(
            text="Slide I"
        )
        self.add_widget(self.but0ni)
 
        self.but0ni2 = Button(
            text="Slide II"
        )
        self.add_widget(self.but0ni2)
 
        self.but0ni3 = Button(
            text="Slide III"
        )
        self.add_widget(self.but0ni3) 

 
class TrialApp(App):
    def build(self):
        return Label(
            text="Making an android app"
        )


class Format_float(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
 
        self.label = Label(
            text="Tap on Blue",
            size_hint=(0.1, -0.1),
            pos_hint = {"x": 0.3, "y": 0.7},
        )
        self.add_widget(self.label)
 
        self.button = Button(
            text="Press here",
            size_hint=(0.4, 0.1),
            pos_hint={"x":0.4,"y":0.5},
            background_color=(0.6, 25.3, 2),
            color=(1, 0, 1, 2)
        )
        self.add_widget(self.button)


class DemoApp(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x="left",
            anchor_y="top",
        )
        button = Button(
            text="Send",
            size_hint=(0.2, 0.1),
            background_color=(0.1, 25.86, 1),
            color=(0, 0, 0, 1)
        )
        layout.add_widget(button)
        return Format_float()
 
  
# demo=DemoApp()
# demo.run()
