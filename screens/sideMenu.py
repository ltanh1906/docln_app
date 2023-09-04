from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from functools import partial
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget,ImageLeftWidget,ThreeLineIconListItem
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader,
    MDNavigationDrawerLabel,
    MDNavigationDrawerDivider,
    MDNavigationDrawerItem,
)
import database_handler
import encryption

class SideMenu(MDNavigationDrawer):
    id = "nav_drawer_doc"