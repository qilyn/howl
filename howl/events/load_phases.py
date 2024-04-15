from kivy.event import EventDispatcher
from kivy.properties import DictProperty


class PhaseEventManager(EventDispatcher):
    phase = DictProperty()
