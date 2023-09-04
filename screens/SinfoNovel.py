from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.label import Label
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import GridLayout,MDGridLayout
from kivymd.uix.boxlayout import BoxLayout,MDBoxLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from functools import partial
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget,ImageLeftWidget,ThreeLineIconListItem
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine, MDExpansionPanelTwoLine
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.chip import MDChip
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.utils import get_color_from_hex
from kivy.metrics import dp
import database_handler
import encryption
import StaticPages

class Content(MDBoxLayout):
    pass
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
                panel_cls=MDExpansionPanelTwoLine(text=f"[b]Volume 0{i+1}[/b]", secondary_text="Title of the volume"),
            )

            # Thêm MDExpansionPanel vào layout_content bằng cách sử dụng self.ids.layout_content
            self.ids.volume_list.add_widget(expansion_panel)

    def switch_to_screen(self, item_text):
        StaticPages.chapter = 2
        setattr(self.manager, 'current', 'Strangdoc')
        print(self.manager)

    def show_example_custom_bottom_sheet(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
        self.custom_sheet.open()

    def draw_review(self):
        self.ids.test_box.clear_widgets()
        box = MDGridLayout(adaptive_height=True, size_hint_y=None, cols=1)
        for i in range(3):
            grid = MDGridLayout(adaptive_height=True,cols=2)
            user_label = MDLabel(
                text="[b]User 0001[/b]",
                markup=True,
                padding=(dp(10), dp(0)),
                halign="left",
                size_hint_y=None,
                adaptive_height= True
            )
            grid.add_widget(user_label)
            # box.add_widget(grid)

            grid_child = MDGridLayout(adaptive_height=True,cols=5)
            for _ in range(5):
                star_icon = MDIcon(
                    icon="star",
                    theme_text_color="Custom",
                    text_color=get_color_from_hex("#f5ab00"),
                    adaptive_height= True
                )
                grid_child.add_widget(star_icon)
            grid.add_widget(grid_child)
            # MDLabel cho đánh giá
            review_label = MDLabel(
                text="Truyện oke, đọc giải trí ...",
                padding=(dp(10), dp(0)),
                halign="left",
                size_hint_y=None,
                adaptive_height= True
            )

            widget = Widget(size_hint_y= None,height= 30)
            box.add_widget(grid)
            box.add_widget(review_label)
            box.add_widget(widget)
        expansion_panel = MDExpansionPanel(
            icon="star",
            content=box,
            panel_cls=MDExpansionPanelOneLine(text=f"[b]Đánh giá[/b]"),
        )
        
        self.ids.test_box.add_widget(expansion_panel)
        expansion_panel.panel_expanded = True