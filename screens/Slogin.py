from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar, BaseSnackbar
import StaticPages
import database_handler
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

class Slogin(MDScreen):

    def login(self):
        # fetch login credentials from teh screen
        username = self.ids.username.text
        password = self.ids.password.text

        # check if the credentials are valid using the DB
        login_check = database_handler.check_password(username, password)

        if login_check == True:
            StaticPages.is_logged_in = True
            StaticPages.username = username
            self.dialog = MDDialog(
                text="Đăng nhập thàng công",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=self.close_dialog
                    ),
                ],
            )
            self.dialog.open()
        if login_check == False:
            StaticPages.is_logged_in = False
            StaticPages.username = ''
            self.dialog = MDDialog(
                text="Sai tên đăng nhập hoặc mật khẩu",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=self.close_dialog
                    ),
                ],
            )
            self.dialog.open()
        if login_check == 0:
            StaticPages.is_logged_in = False
            StaticPages.username = ''
            self.dialog = MDDialog(
                text="Kết nối mạng bị gián đoạn",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=self.close_dialog
                    ),
                ],
            )
            self.dialog.open()

    def close_dialog(self, instance):
        if self.dialog:
            self.dialog.dismiss()