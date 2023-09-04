from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import BoxLayout,MDBoxLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from functools import partial
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget,ImageLeftWidget,ThreeLineIconListItem
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.chip import MDChip
import database_handler
import encryption
import StaticPages

class SinfoNovel(MDScreen):
        
    def click_test(self):
        print(self.ids.separator.pos)
    def click_test1(post):
        print(post)

    def load_volume(self):
        self.ids.volume_list.clear_widgets()
        for i in range(3):
            box = MDBoxLayout(adaptive_height=True, orientation="vertical")
            item_texts = ["Mở đầu: Sự dối trá, hư cấu và lời tuyên bố khai chiến.", "Chương 1: Cuộc gặp gỡ của những kẻ dối trá và xung đột. (Part1)", "Chương 2: Sự ra đời của 7 sao giả. (Part1)"]

            for text in item_texts:
                list_item = OneLineIconListItem(
                    text=text,
                    on_release=lambda item_text=text: self.switch_to_screen(1)
                )
                icon_widget = IconLeftWidget(icon="image-area")
                list_item.add_widget(icon_widget)
                box.add_widget(list_item)

            expansion_panel = MDExpansionPanel(
                icon="book",
                content=box,
                panel_cls=MDExpansionPanelOneLine(text=f"[b]Volume 0{i+1}[/b]"),
            )

            # Thêm MDExpansionPanel vào layout_content bằng cách sử dụng self.ids.layout_content
            self.ids.volume_list.add_widget(expansion_panel)

    def switch_to_screen(self, item_text):
        StaticPages.chapter = 2
        setattr(self.manager, 'current', 'Strangdoc')
        print(self.manager)