import csv
import time

import openpyxl
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.properties import ObjectProperty

Window.size = (400, 600)

t = time.localtime(time.time())
localtime = time.asctime(t)
widget = Widget
input_file = 'devices.txt'
output_file = 'Survey.xlsx'

wb = openpyxl.Workbook()
ws = wb.worksheets[0]

kv = """
#:import MapSource kivy_garden.mapview.MapSource
#: import FadeTransition kivy.uix.screenmanager.FadeTransition


ScreenManager:
    transition: FadeTransition()
    id: screenMan
    name: "screen_Man"
    Screen:
        name: "main_SC"
        id: sm_main
        BoxLayout:
            orientation: "vertical"
            spacing: '5dp'
            padding: '5dp'
            pos_hint: {'center_x': .5, 'center_y': .5}
            GridLayout:
                id: lay
                cols: 1
                # size_hint_y: None
                # size_hint_x: 0.1
                # spacing: 30
                # padding: 50
                # height: self.minimum_height
                Button:
                    text:"Export to Excel"
                    size_hint: .3, .1
                    pos_hint: {'center_x': .5, 'center_y': .9}
                    on_press:app.Export_excel()
                MDLabel:
                    id: Existing
                    text:"Is it new building or new parcel?"
                    pos_hint: {'center_x': .1, 'center_y': .8}
                Button:
                    id: NB_NP
                    text:"New Buiding and New Parcel"
                    pos_hint: {'center_x': .1, 'center_y': .8}
                    size_hint: .3, .1
                    on_release: app.Existing_1(self)
                    # on_state: root.on_toggle_button_state(self)
                # CheckBox:
                #     id:CheckBox 
                #     text: 'New Buiding and New Parcel'
                #     active: False
                    
                # CheckBox:
                #     id:CheckBox2 
                #     text: 'New Buiding and New Parcel'
                #     active: False
                #     #on_state: root.on_toggle_button_state(self)
                Widget:
                Button:
                    id: NB_EP
                    text:"New Building in existing Parcel"
                    pos_hint: {'center_x': .1, 'center_y': .8}
                    size_hint: .3, .1
                    on_release: app.Existing_2()
                Widget:
                Button:
                    id: EB_EP
                    text:"Exising Building in existing Parcel"
                    pos_hint: {'center_x': .1, 'center_y': .8}
                    size_hint: .3, .1
                    on_release: app.Existing_3()
                Widget:
                Button:
                    id: EB_NP
                    text:"Exising Building in New Parcel"
                    pos_hint: {'center_x': .1, 'center_y': .8}
                    size_hint: .3, .1
                    on_release: app.Existing_4()
                Widget:
                MDLabel:
                    id: bldg_par_id
                    text:"Select building and parcel id?"
                    pos_hint: {'center_x': .1, 'center_y': .8}
                    
                Button:
                    text: "Building ID"
                    on_release: screenMan.current ='buldg_par_id'
                    size_hint: .3, .1
                    padding: 10
                    spacing: 10
                    disabled: not app.count_enabled
                Widget:
                Button:
                    text: "Parcel ID"
                    on_release: screenMan.current ='buldg_par_id'
                    size_hint: .3, .1
                    padding: 10
                    spacing: 10
                MDTextField:
                    id: new_Pid
                    text:"New Parcel ID"
                    icon_right:"rename-box"
                    size_hint_x: None
                    helper_text: "Write New Parcel ID"
                    #input_filter: 'int'
                    helper_text_mode: "on_focus"
                    # disabled: not CheckBox.active
                    width:300
                    padding: '5dp'
                MDTextField:
                    id: new_Pid
                    text:"New Building ID"
                    icon_right:"rename-box"
                    size_hint_x: None
                    helper_text: "Write New Building ID"
                    #input_filter: 'int'
                    helper_text_mode: "on_focus"
                    # disabled: not CheckBox.active
                    width:300
                    padding: '5dp'
                MDTextField:
                    id: time_lab1
                    text:"Family Size"
                    icon_right:"rename-box"
                    size_hint_x: None
                    helper_text: "Write the family member count"
                    input_filter: 'int'
                    helper_text_mode: "on_focus"
                    width:300
                    padding: '5dp'
                MDTextField:
                    id: time_lab
                    text:"House Number"
                    icon_right:"rename-box"
                    size_hint_x: None
                    helper_text: "Respondent House Number"
                    helper_text_mode: "on_focus"
                    input_filter: 'int'
                    width:300
                    padding: '5dp'
                
                
                MDRectangleFlatButton:
                    text: "next"
                    on_release: screenMan.current ='scend_sc'
                    pos_hint: {'center_x': .5, 'center_y': .2}

    Screen:
        name: "buldg_par_id"
        BoxLayout:
            ScrollView:
                MDList:
                    id: building_id
            # RightCheckbox:
            #         on_active: app.on_checkbox_active()
                    
        MDRectangleFlatButton:
            text: "next"
            on_release: screenMan.current ='main_SC'
            pos_hint: {'center_x': .5, 'center_y': .2}
    Screen:
        name: "scend_sc"
        id: sm_main
        GridLayout:
            id: lay
            cols: 1
            size_hint_y: None
            size_hint_x: 0.1
            spacing: 20
            padding: 50
            height: self.minimum_height
            MDLabel:
                id: time_n
                
            MDTextField:
                id: time_lab4
                text:"Your Name"
                icon_right:"rename-box"
                size_hint_x: None
                helper_text: "Question 4"
                helper_text_mode: "on_focus"
                width:300
                padding: '5dp'
            MDTextField:
                id: time_lab5
                text:"Your Name"
                icon_right:"rename-box"
                size_hint_x: None
                helper_text: "Question 5"
                helper_text_mode: "on_focus"
                width:300
                padding: '5dp'
            MDTextField:
                id: time_lab6
                text:"Your Name"
                icon_right:"rename-box"
                size_hint_x: None
                helper_text: "Question 6"
                helper_text_mode: "on_focus"
                width:300
                padding: '5dp'
            MDTextField:
                id: Q_last
                text:"Your Name"
                icon_right:"rename-box"
                size_hint_x: None
                helper_text: "Question last"
                helper_text_mode: "on_focus"
                width:300
                padding: '5dp'   
            MDRectangleFlatButton:
                text: "save"
                on_press: app.on_text_validate()
                pos_hint: {'center_x': .5, 'center_y': .3}
            MDRectangleFlatButton:
                text: "New_Form"
                pos_hint: {'center_x': .5, 'center_y': .2}
                on_release: screenMan.current ='main_SC'


"""


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''
    adaptive_width = True
    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''
    adaptive_width = True


class QuestionnerApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    count_enabled = ObjectProperty(False)


    def Existing_1(self, widget):
        self.root.ids.NB_NP.background_color = 0.0, 1.0, 0.0, 1.0
        NB_NP_label = self.root.ids.NB_NP.text
        if widget.state == "normal":
            widget.text = "Select Building ID"
            self.count_enabled = True
        else:
            widget.text = "OFF"
            self.count_enabled = False
        print(NB_NP_label)

    def Existing_2(self):
        self.root.ids.NB_EP.background_color = 0.0, 1.0, 0.0, 1.0
        NB_EP_label = self.root.ids.NB_EP.text
        print(NB_EP_label)

    def Existing_3(self):
        self.root.ids.EB_EP.background_color = 0.0, 1.0, 0.0, 1.0
        EB_EP_label = self.root.ids.EB_EP.text
        print(EB_EP_label)

    def Existing_4(self):
        self.root.ids.EB_NP.background_color = 0.0, 1.0, 0.0, 1.0
        EB_NP_label = self.root.ids.EB_NP.text
        print(EB_NP_label)

    def on_button_click(self):
        #print("Button Clicked")
        if self.count_enabled:
            Q3_label = self.root.ids.building_id
            print(Q3_label)

    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False

    def on_checkbox_active2(self):
        Q3_label = self.root.ids.building_id
        print(Q3_label)

    def on_start(self):
        icons = list(md_icons.keys())
        for i in range(100, 121):
            self.root.ids.building_id.add_widget(
                ListItemWithCheckbox(text=f"B_ {i}", icon=icons[i]))

    # def checked(self, obj):
    #     bldg_label = self.chech.text
    #     print(bldg_label)

    def on_text_validate(self):
        t = time.localtime(time.time())
        localtime = time.asctime(t)
        file = open("devices.txt", "a")

        file.write(self.root.ids.NB_NP.text + "/")
        file.write(self.root.ids.NB_EP.text + "/")
        file.write(self.root.ids.EB_EP.text + "/")
        file.write(self.root.ids.EB_NP.text + "/")
        file.write(self.root.ids.time_lab.text + "/")
        file.write(self.root.ids.time_lab1.text + "/")
        # file.write(self.root.ids.time_lab2.text + "/")
        # file.write(self.root.ids.time_lab3.text + "/")
        file.write(self.root.ids.time_lab4.text + "/")
        file.write(self.root.ids.time_lab5.text + "/")
        file.write(self.root.ids.time_lab6.text + "/")
        file.write(self.root.ids.time_n.text + "/")
        file.write(self.root.ids.Q_last.text + "\n")
        file.close()
        print("All done!")

    def Export_excel(self):
        with open(input_file, 'r') as data:
            reader = csv.reader(data, delimiter='\t')
            for row in reader:
                ws.append(row)

        wb.save(output_file)


QuestionnerApp().run()
