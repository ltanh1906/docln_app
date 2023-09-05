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
        label = MDLabel(
                text="""[b][size=17]No game [ref=ABC:abc]no[/ref] life[/u]\nVolume 1 - Ch 1 - 3-1=Hopeless (3)\nĐộ dài: 518 từ - Cập nhật: 2 năm[/size][/b]""",
                padding= (dp(20), dp(10)),
                markup = True,
                valign= "middle",
                halign= "center",
                size_hint_y= None,
            )
        label.bind(on_ref_press=lambda *args: self.show_tooltip_dialog(args[1]))
        self.ids.layout_content.add_widget(label)

        global noidung 
        noidung = """
            —Rất, rất lâu về trước, có một thứ được gọi là 『Mặt trời』từng tồn tại.
            Tỏa ra ánh hào quang lửa trắng, nhuộm bầu trời với màu xanh trong – phải, thiên hạ đồn đại như vậy đấy.
            『Đại chiến 』giữa các vị thần và các sinh vật đã thiêu rụi mặt đất. Cả bầu trời trở thành một màn tro xám.
            Bầu trời chìm trong tro xám và những Năng lượng Hành tinh—Hành lang Tinh linh trào ra, xung khắc lẫn nhau, khiến cho ánh sáng tỏa ra nhuộm bầu trời trong màu đỏ rực.
            Cái sắc đỏ này bao trùm lên cảnh tượng giết chóc tang thương không ngừng trên mặt đất. Hay có lẽ, chính ngôi sao này đang khóc thương, rỉ ra thứ máu đỏ tươi đó –
            Trong bầu trời nhuốm máu này, chỉ có thứ tro màu lam ngọc kia tiếp tục rơi xuống.|img=asset/ngnl1.webp|
            …
            Ivan nhìn lên bầu trời màu đỏ và nhăn mặt.
            『Tro đen 』tỏa ra thứ ánh sáng màu lam ngọc rơi xuống mặt đất, bắt đầu chất đống lên.
            Ivan đứng ngây người suy nghĩ về những giới hạn về kiến thức mà con người nắm giữ.
            Loài người không thể cảm nhận được hạt tinh linh, nên họ không thể nào nhìn thấy thứ ánh sáng màu lam ngọc kia. Còn về lý do tại sao bầu trời bị nhuộm đỏ, thì có lẽ là bởi những ánh sáng phân cực hay lý do bí ẩn nào đó. Dẫu sao thì hạt tinh linh vốn mang màu xanh mà –
            Về phần tại sao con người lại có thể cảm nhận và kết nối được với Hành lang Tinh linh thì – chắc là có liên quan gì đó với ánh sáng cuối cùng tỏa ra từ Hành lang Tinh linh sau khi va chạm với thứ tro kia.
            —『Tinh linh Cốt』. Với hầu hết những sinh vật sống, bao gồm con người, đây chính là một thứ kịch độc chết người.
            Khi chạm vào, da sẽ nóng cháy. Khi rơi vào, mắt sẽ mù lòa. Nếu nuốt vào, nội tạng sẽ tan chảy.
            Cho dù thứ đó tỏa ra ánh sáng màu lam ngọc, thì nó vẫn được gọi là 『Tro đen』, bởi vì chính nó đã là biểu tượng cho cái chết.
            Có lẽ, cái thứ này cũng có lòng nhân từ —
            Mặt nạ chống bụi che hết đầu của anh ta. Bộ giáo lông thú được tạo ra để chống chịu với cái lạnh. Nếu bỏ hết những thứ này ra và cố tình nằm xuống mặt đất – mặt đất chứa đầy 『Tro đen』(Cái chết), thì sẽ mang lại cho người đó một cái chết nhẹ nhàng.
            (Mình muốn nghỉ ngơi. Làm việc cật lực từ sáng đến giờ. Cơ thể mình rệu rã cả rồi, mình muốn uống một bát súp nóng, rửa sạch đống tro này đi và rúc đầu vào ngực vợ mình rồi ngủ luôn – nếu mình không thể làm được thế vào ngày nào đó, thì giờ chắc mình nên –)
            Sự cám dỗ đó khiến Ivan bủn rủn, ý thức dừng lại hoàn toàn. Sinh ra trong cái thế giới như thế này, thì việc sinh tồn hay chết đi cũng chả có ý nghĩa gì –
            “—Ivan. Tro đen chui vào não rồi hả?”
            Ivan quay người lại sau khi anh nghe thấy lời càu nhàu của người đồng hành. Sau khi chớp chớp mắt vài cái, cậu nhìn hai người đồng đội đứng bên cạnh cậu.
            “…Chỉ là nghỉ ngơi chút thôi mà, Allei. Tôi cũng có tuổi rồi đấy nhỉ?”
        """
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
        StaticPages.touch_pos = touch.pos

    def scroll_view_touch_up(self, instance, touch, *args):
        touch_pos = StaticPages.touch_pos
        if touch_pos == touch.pos:
            self.toogleMenu()