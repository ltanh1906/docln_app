from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from functools import partial
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget,ImageLeftWidget,ThreeLineIconListItem
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
import database_handler
import encryption

class Strangchu(MDScreen):
    def load_post(self):
        title = """[b][size=17]This is title of the book[/size][/b]"""
        description = """[size=12]"This is description of the book.This is description of the book.This is description of the book.This is description of the book."[/size]"""
        


