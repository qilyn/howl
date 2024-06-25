# from kivymd.app import App
# from kivy.uix.screenmanager import Screen, ScreenManager
from kivy import platform
from kivy.lang import Builder
from kivy.storage import jsonstore
from kivy.storage.jsonstore import JsonStore
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.pickers import MDModalDatePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.screenmanager import MDScreenManager

from events import load_phases

if platform == "android":
    from android.permissions import Permission, request_permissions
    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])


store = jsonstore.JsonStore('test.json')


Builder.load_string('''
<MenuScreen>:
    MDGridLayout:
        rows: 4
        cols: 1
        MDLabel:
            text: "TEst"
        MDButton:
            style: "tonal"
            on_press: root.manager.current = 'create_quarter'
            MDButtonText:
                text: 'I see blood!'
        Button:
            text: 'Show phase'
            # on_press: root.manager.current = 'show_active_state'
        Button:
            text: 'Salary report'

<CreateQuarter>:
    MDGridLayout:
        cols: 2
        MDButton:
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.show_date_picker()
            # on_cancel: app.createQuarter_closePicker()
            # on_edit: app.createQuarter_edit()

            MDButtonText:
                text: "Open modal date picker dialog"
        MDLabel:
            text: 'Job'
        MDTextField:
            id: 'test'
            mode: "filled"
            max_height: "200dp"
            multiline: True
    
            MDTextFieldHelperText:
                text: "multiline=True"
                mode: "persistent"
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Save'
            on_press: app.save()
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

    def createQuarter_startDate(self):
        pass

    def createQuarter_closePicker(self, instance_date_picker):
        instance_date_picker.is_open=False
        instance_date_picker.dismiss()

    def save(self, name, job):
        # fob = open('./test.txt','w')
        store.put(name, job=job)
        print(name, job)
        MDSnackbar(
            MDSnackbarText(
                text=f"saved {name}, {job}",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def on_start(self):
        def callback_load_phase(instance, value):
            print('My callback is call from', instance)
            print('and the a value changed to', value)

        ins = load_phases.PhaseEventManager()
        ins.bind(phase=callback_load_phase)

        MDSnackbar(
            MDSnackbarText(
                text="Text",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()