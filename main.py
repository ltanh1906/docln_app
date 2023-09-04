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
from kivymd.uix.button import  MDRectangleFlatButton, MDIconButton
from kivymd.uix.list import ThreeLineAvatarListItem, TwoLineListItem
from kivymd.uix.imagelist import MDSmartTile
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.carousel import MDCarousel
from kivy.uix.carousel import Carousel
import StaticPages
import database_handler

from kivy.core.window import Window
Window.size = (380,675)

from screens.Strangchu import Strangchu
from screens.Slogin import Slogin
from screens.Strangdoc import Strangdoc
from screens.SinfoNovel import SinfoNovel



from kivy.factory import Factory

class ScreenManager(ScreenManager):
    pass

class Custom_menu(MDNavigationDrawer):
    pass

class DocLNApp(MDApp):
    def build(self):
        kvfile = Builder.load_file('main.kv')
        return kvfile
    # def on_start(self):
        # screen = self.root.get_screen('Strangchu')

if __name__ == '__main__':
    DocLNApp().run()


