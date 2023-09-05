from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader,
    MDNavigationDrawerLabel,
    MDNavigationDrawerDivider,
    MDNavigationDrawerItem,
)
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.button import  MDRectangleFlatButton, MDIconButton
from kivymd.uix.list import ThreeLineAvatarListItem, TwoLineListItem
from kivymd.uix.imagelist import MDSmartTile
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.carousel import MDCarousel
from kivy.uix.carousel import Carousel

from kivy.properties import ObjectProperty
import StaticPages
import database_handler

from kivy.core.window import Window
Window.size = (380,675)



from kivy.factory import Factory

class ScreenManager(ScreenManager):
    pass
class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
class DocLNApp(MDApp):
    def build(self):
        # Window.borderless = True
        kvfile = Builder.load_file('main.kv')
        return kvfile
    # def on_start(self):
        # screen = self.root.get_screen('Strangchu')
    def hide_top_app_bar(self):
        print(1)
        self.root.ids.topappbar.pos_hint = {"top":0}
    def show_top_app_bar(self):
        self.root.ids.topappbar.pos_hint = {"top":1}
    def show_search(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.SearchBox())
        self.custom_sheet.open()

if __name__ == '__main__':
    DocLNApp().run()


