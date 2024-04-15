# from kivymd.app import App
# from kivy.uix.screenmanager import Screen, ScreenManager
from kivy import platform
from kivy.lang import Builder
from kivy.storage import jsonstore
from kivymd.app import MDApp
from kivymd.uix.pickers import MDModalDatePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

from .events import load_phases

if platform == "android":
    from android.permissions import Permission, request_permissions
    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])


store = jsonstore.JsonStore('./test.json')


Builder.load_string('''
<MenuScreen>:
    MDGridLayout:
        rows: 4
        cols: 1
        MDLabel:
            text: "TEst"
        Button:
            style: "tonal"
            text: 'I see blood!'
            on_press: root.manager.current = 'create_quarter'
        Button:
            text: 'Show phase'
            # on_press: root.manager.current = 'show_active_state'
        Button:
            text: 'Salary report'

<CreateQuarter>:
    # name: str(createQuarter_startDate)
    # job: job_input
    MDGridLayout:
        cols: 2
        MDButton:
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_date_picker()
            # on_cancel: app.createQuarter_closePicker()
            # on_edit: app.createQuarter_edit()

            MDButtonText:
                text: "Open modal date picker dialog"
        Label:
            text: 'Job'
        TextInput:
            id: job_input
        Label:
            text: 'Salary'
        TextInput:
        Label:
            text: 'Date of Joining'
        TextInput:
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Save'
            on_press: app.save(createQuarter_startDate.text, job_input.text)
''')


class MenuScreen(MDScreen):
    pass

class CreateQuarter(MDScreen):
    pass


class TestApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        sm = MDScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CreateQuarter(name='create_quarter'))
        return sm

    def show_date_picker(self):
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_cancel=self.createQuarter_closePicker)
        date_dialog.open()

    def createQuarter_closePicker(self, instance_date_picker):
        instance_date_picker.is_open=False
        instance_date_picker.dismiss()

    def save(self, name, job):
        # fob = open('./test.txt','w')
        store.put(name, job=job)

    def on_start(self):
        def callback_load_phase(instance, value):
            print('My callback is call from', instance)
            print('and the a value changed to', value)

        ins = load_phases.PhaseEventManager()
        ins.bind(phase=callback_load_phase)