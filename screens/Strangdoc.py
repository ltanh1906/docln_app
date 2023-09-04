from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.image import Image, AsyncImage
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from functools import partial
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget,ImageLeftWidget,ThreeLineIconListItem
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDFloatingActionButton,MDRectangleFlatIconButton,MDRectangleFlatButton,MDIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
import database_handler
import encryption
import StaticPages

class Strangdoc(MDScreen):
    noidung = ""
    def set_item(self, text_item):
        self.ids.drop_item.set_item(text_item)
        self.menu.dismiss()

    def load_text(self):
        self.ids.layout_content.clear_widgets()
        font_array=['Times New Roman', 'Arial', 'Open Sans']
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{font_array[i]}",
                "height": dp(56),
                "on_release": lambda x=f"{font_array[i]}": self.set_item(x),
            } for i in range(3)
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu.bind()


        global noidung 
        noidung = """"A, Nikoru, chào cậu!"\n"Chào Runa! Nghe nói mai cậu về đây nhỉ? Xin lỗi vì tớ không đến được chỗ cậu nhé."\n"Không sao đâu, dù gì cậu cũng đã đến đây trước đó rồi mà! Với cả đã có Ryuuto rồi."\n"Phải rồi, cái tên đó. Thế nào rồi? Cậu ta thay đổi rồi phải không?"\n"|img=example_1.png|Ahaha, thay đổi là sao chứ?"\n"Nếu cậu ta có giở trò gì với cậu thì nói với tớ một tiếng, tớ sẽ đến bóp cổ cậu ta."\n"Không cần phải lo đâu."\n"Hôm trước cậu cũng nói thế, rồi cuối cùng cậu ta lại lén lút gặp em gái cậu đấy thôi?"\n"Do hoàn cảnh đưa đẩy thôi mà, sau cùng thì cậu ấy cũng không ngoại tình. Tớ nói rồi mà nhỉ?"\n"Đúng là thế, nhưng mà..."\n"Tớ mừng khi thấy Nikoru lo lắng cho tớ đấy. Cảm ơn nhé!"\n"...Mà tớ cũng không nghĩ cậu ta có gan đến mức đó đâu."\n"Ừ. Ryuuto không đời nào làm chuyện đó đâu."\n“Nhưng mà cái ‘thay lòng đổi dạ’ đó không hẳn là theo chiều hướng xấu đâu. Ít nhất nó không thể xảy ra trong một tháng được.”\n“Thay lòng đổi dạ không phải là theo chiều hướng xấu, Nikoo à.”\n“Ahaha, cô nói hay lắm.” \n“Dù vậy nhưng nếu điều đó xảy ra với em gái của cậu thì đúng là không thể tin nổi mà.”\n“Đã nói rồi, là do hoàn cảnh thôi.”\n“Ờ ừ… Ít nhiều gì tớ cũng hiểu mà.”\n“...Lúc trước mỗi khi xa cách bạn trai mình tớ luôn thấy lo lắng. Không biết rằng người đó đang làm gì, hay có kè kè bên cô nào không.”\n“Thì đúng là cậu bị cắm sừng mà.”\n“...Nhưng Ryuuto thì khác.”\n“Chẳng phải vì hai cậu ở cùng nhau suốt hai tuần sao? Đương nhiên cậu không lo lắng gì là phải rồi.”\n“Đúng là thế, nhưng tớ tin cậu ấy hoàn toàn khác với họ kể cả khi có về lại Tokyo.”\n“Sao cậu lại nghĩ thế?”\n“Là vì lần trước tớ không đủ mạnh mẽ. Tớ bảo rằng mình tin Ryuuto, nhưng đến cuối cùng vẫn nghi ngờ cậu ấy, tớ sợ phải đối diện với sự thật nên mới bỏ chạy… Nếu lúc đó tớ đủ dũng khí để đối mặt với Ryuuto thì tớ không cần phải lo lắng suốt hai tuần rồi.”\n“Vậy giờ cậu có còn yếu đuối nữa không?”\n“Đương nhiên là không… Dù có chuyện gì xảy ra giữa bọn tớ đi nữa, tớ sẽ không chạy trốn nữa đâu.”\n“...Vậy à.”\n“Hai tuần vừa qua bọn tớ nói chuyện nhiều lắm. Từ chuyện của bố mẹ tớ… hay về Maria. Kể cả chuyện bạn trai cũ của tớ nữa.”\n“Ừm…”\n“Tớ nghĩ cậu ấy hiểu rõ hơn bao giờ hết… Tớ cũng cảm nhận rõ tình cảm mà Ryuuto dành cho tớ. Nên là không sao đâu.”[marked_line]\nRuna vừa nói chuyện vừa nhìn vào chiếc nhẫn trên tay phải mình.\n“Vì từ giờ, dù không có cậu ấy ở bên thì trái tim bọn tớ vẫn sẽ gắn kết với nhau.”\nA, Nikoru, chào cậu!"\n"Chào Runa! Nghe nói mai cậu về đây nhỉ? Xin lỗi vì tớ không đến được chỗ cậu nhé."\n"Không sao đâu, dù gì cậu cũng đã đến đây trước đó rồi mà! Với cả đã có Ryuuto rồi."\n"Phải rồi, cái tên đó. Thế nào rồi? Cậu ta thay đổi rồi phải không?"\n"Ahaha, thay đổi là sao chứ?"\n"Nếu cậu ta có giở trò gì với cậu thì nói với tớ một tiếng, tớ sẽ đến bóp cổ cậu ta."\n"Không cần phải lo đâu."\n"Hôm trước cậu cũng nói thế, rồi cuối cùng cậu ta lại lén lút gặp em gái cậu đấy thôi?"\n"Do hoàn cảnh đưa đẩy thôi mà, sau cùng thì cậu ấy cũng không ngoại tình. Tớ nói rồi mà nhỉ?"\n"Đúng là thế, nhưng mà..."\n"Tớ mừng khi thấy Nikoru lo lắng cho tớ đấy. Cảm ơn nhé!"\n"...Mà tớ cũng không nghĩ cậu ta có gan đến mức đó đâu."\n"Ừ. Ryuuto không đời nào làm chuyện đó đâu."\n“Nhưng mà cái ‘thay lòng đổi dạ’ đó không hẳn là theo chiều hướng xấu đâu. Ít nhất nó không thể xảy ra trong một tháng được.”\n“Thay lòng đổi dạ không phải là theo chiều hướng xấu, Nikoo à.”\n“Ahaha, cô nói hay lắm.” \n“Dù vậy nhưng nếu điều đó xảy ra với em gái của cậu thì đúng là không thể tin nổi mà.”\n“Đã nói rồi, là do hoàn cảnh thôi.”\n“Ờ ừ… Ít nhiều gì tớ cũng hiểu mà.”\n“...Lúc trước mỗi khi xa cách bạn trai mình tớ luôn thấy lo lắng. Không biết rằng người đó đang làm gì, hay có kè kè bên cô nào không.”\n“Thì đúng là cậu bị cắm sừng mà.”\n“...Nhưng Ryuuto thì khác.”\n“Chẳng phải vì hai cậu ở cùng nhau suốt hai tuần sao? Đương nhiên cậu không lo lắng gì là phải rồi.”\n“Đúng là thế, nhưng tớ tin cậu ấy hoàn toàn khác với họ kể cả khi có về lại Tokyo.”\n“Sao cậu lại nghĩ thế?”\n“Là vì lần trước tớ không đủ mạnh mẽ. Tớ bảo rằng mình tin Ryuuto, nhưng đến cuối cùng vẫn nghi ngờ cậu ấy, tớ sợ phải đối diện với sự thật nên mới bỏ chạy… Nếu lúc đó tớ đủ dũng khí để đối mặt với Ryuuto thì tớ không cần phải lo lắng suốt hai tuần rồi.”\n“Vậy giờ cậu có còn yếu đuối nữa không?”\n“Đương nhiên là không… Dù có chuyện gì xảy ra giữa bọn tớ đi nữa, tớ sẽ không chạy trốn nữa đâu.”\n“...Vậy à.”\n“Hai tuần vừa qua bọn tớ nói chuyện nhiều lắm. Từ chuyện của bố mẹ tớ… hay về Maria. Kể cả chuyện bạn trai cũ của tớ nữa.”\n“Ừm…”\n“Tớ nghĩ cậu ấy hiểu rõ hơn bao giờ hết… Tớ cũng cảm nhận rõ tình cảm mà Ryuuto dành cho tớ. Nên là không sao đâu.”[marked_line]\nRuna vừa nói chuyện vừa nhìn vào chiếc nhẫn trên tay phải mình.\n“Vì từ giờ, dù không có cậu ấy ở bên thì trái tim bọn tớ vẫn sẽ gắn kết với nhau.”\nA, Nikoru, chào cậu!"\n"Chào Runa! Nghe nói mai cậu về đây nhỉ? Xin lỗi vì tớ không đến được chỗ cậu nhé."\n"Không sao đâu, dù gì cậu cũng đã đến đây trước đó rồi mà! Với cả đã có Ryuuto rồi."\n"Phải rồi, cái tên đó. Thế nào rồi? Cậu ta thay đổi rồi phải không?"\n"Ahaha, thay đổi là sao chứ?"\n"Nếu cậu ta có giở trò gì với cậu thì nói với tớ một tiếng, tớ sẽ đến bóp cổ cậu ta."\n"Không cần phải lo đâu."\n"Hôm trước cậu cũng nói thế, rồi cuối cùng cậu ta lại lén lút gặp em gái cậu đấy thôi?"\n"Do hoàn cảnh đưa đẩy thôi mà, sau cùng thì cậu ấy cũng không ngoại tình. Tớ nói rồi mà nhỉ?"\n"Đúng là thế, nhưng mà..."\n"Tớ mừng khi thấy Nikoru lo lắng cho tớ đấy. Cảm ơn nhé!"\n"...Mà tớ cũng không nghĩ cậu ta có gan đến mức đó đâu."\n"Ừ. Ryuuto không đời nào làm chuyện đó đâu."\n“Nhưng mà cái ‘thay lòng đổi dạ’ đó không hẳn là theo chiều hướng xấu đâu. Ít nhất nó không thể xảy ra trong một tháng được.”\n“Thay lòng đổi dạ không phải là theo chiều hướng xấu, Nikoo à.”\n“Ahaha, cô nói hay lắm.” \n“Dù vậy nhưng nếu điều đó xảy ra với em gái của cậu thì đúng là không thể tin nổi mà.”\n“Đã nói rồi, là do hoàn cảnh thôi.”\n“Ờ ừ… Ít nhiều gì tớ cũng hiểu mà.”\n“...Lúc trước mỗi khi xa cách bạn trai mình tớ luôn thấy lo lắng. Không biết rằng người đó đang làm gì, hay có kè kè bên cô nào không.”\n“Thì đúng là cậu bị cắm sừng mà.”\n“...Nhưng Ryuuto thì khác.”\n“Chẳng phải vì hai cậu ở cùng nhau suốt hai tuần sao? Đương nhiên cậu không lo lắng gì là phải rồi.”\n“Đúng là thế, nhưng tớ tin cậu ấy hoàn toàn khác với họ kể cả khi có về lại Tokyo.”\n“Sao cậu lại nghĩ thế?”\n“Là vì lần trước tớ không đủ mạnh mẽ. Tớ bảo rằng mình tin Ryuuto, nhưng đến cuối cùng vẫn nghi ngờ cậu ấy, tớ sợ phải đối diện với sự thật nên mới bỏ chạy… Nếu lúc đó tớ đủ dũng khí để đối mặt với Ryuuto thì tớ không cần phải lo lắng suốt hai tuần rồi.”\n“Vậy giờ cậu có còn yếu đuối nữa không?”\n“Đương nhiên là không… Dù có chuyện gì xảy ra giữa bọn tớ đi nữa, tớ sẽ không chạy trốn nữa đâu.”\n“...Vậy à.”\n“Hai tuần vừa qua bọn tớ nói chuyện nhiều lắm. Từ chuyện của bố mẹ tớ… hay về Maria. Kể cả chuyện bạn trai cũ của tớ nữa.”\n“Ừm…”\n“Tớ nghĩ cậu ấy hiểu rõ hơn bao giờ hết… Tớ cũng cảm nhận rõ tình cảm mà Ryuuto dành cho tớ. Nên là không sao đâu.”[marked_line]"""
        split_nd = noidung.split('|')
        for i in range(0, len(split_nd)):
            if "img=" in split_nd[i]:
                print(split_nd[i][4:])
                self.ids.layout_content.add_widget(
                    AsyncImage(
                        source=split_nd[i][4:],
                        size_hint= (1, None),
                        height= 380,
                    )
                )
            else:
                self.ids.layout_content.add_widget(
                    MDLabel(
                        id="textTest"+str(i),
                        padding= (dp(20), dp(0)),
                        text = split_nd[i],
                        font_size="50sp",
                        theme_text_color= "Secondary",
                        halign= "justify",
                        adaptive_height= True,
                        line_height=1.75,
                    )
                )

    def bookmark_pressed(self):
        children_list = self.ids.layout_content.children
        # Duyệt qua danh sách và thực hiện một thao tác trên từng con
        for child_widget in children_list:
            try:
                widget_id = child_widget.id
                if "textTest" in widget_id:
                    child_widget.font_size += 2
                    print(self.ids.scroll_view.height)
                    print(self.ids.scroll_view.scroll_y)
                print(f"The id of the child_widget is: {widget_id}")
            except AttributeError:
                print('error')

        return
    def scroll_to_marked_line(self):
        print(self.ids.scroll_view.scroll_y)
        # global noidung
        # text_label = noidung
        # lines = text_label.split('\n')
        # marked_line_index = 5
        # label_height = len(lines)*1.75
        # target_y = (1 - marked_line_index / len(lines)) * (label_height - self.ids.scroll_view.height)
        
        # # Đặt vị trí cuộn
        # num_img = 1
        # self.ids.scroll_view.scroll_y = (target_y / (label_height - self.ids.scroll_view.height))-(0.07*num_img)
        # print(self.ids.scroll_view.scroll_y)
        # return
        # lines[marked_line_index] = f"[b]{lines[marked_line_index]}[/b]"
        # text_label.text = '\n'.join(lines)

    def show_tooltip_dialog(self, content):
        content = content.split(':')
        self.dialog = MDDialog(
            title=content[0],
            text= content[1],
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

    def toogleSettings(self):
        if(StaticPages.setting == 1):
            StaticPages.setting = 0
            self.ids.widget_setting.opacity = 0
            self.ids.parent_setting.pos_hint = {'center_y': 0.5, 'center_x': 1.6}
            self.ids.parent_setting.disabled = True
        else:
            StaticPages.setting = 1
            self.ids.widget_setting.opacity = 1
            self.ids.parent_setting.pos_hint = {'center_y': 0.5, 'center_x': 0.5}
            self.ids.parent_setting.disabled = False

    touch_pos = (0,0)
    def toogleMenu(self):
            if(StaticPages.menu == 1):
                StaticPages.menu = 0
                self.ids.layout_content.disbled = False #enable sự kiện của scroll view khi menu đang hiện
                self.ids.bottom_menu.pos_hint = {'x': 1}
                self.ids.btn_bookmark.opacity = 0
                if(StaticPages.setting == 1):
                    StaticPages.setting = 0
                    self.ids.widget_setting.opacity = 0
                    self.ids.parent_setting.pos_hint = {'center_y': 0.5, 'center_x': 1.6}
                    self.ids.parent_setting.disabled = True
            else:
                StaticPages.menu = 1

                self.ids.layout_content.disbled = True #disbaled sự kiện của scroll view khi menu đang hiện
                self.ids.bottom_menu.pos_hint = {'x': 0}
                self.ids.btn_bookmark.opacity = 1

    def scroll_view_touch_down(self, instance, touch, *args):
        global touch_pos
        touch_pos = touch.pos

    def scroll_view_touch_up(self, instance, touch, *args):
        global touch_pos
        if touch_pos == touch.pos:
            self.toogleMenu()