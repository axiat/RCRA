from PyQt5.QtWidgets import QDialog
from trafficapp.uis.trafficui import Ui_Traffic


class WTrafficDialog(QDialog):
    def __init__(self):
        super(WTrafficDialog, self).__init__()
        self.ui = Ui_Traffic()
        self.ui.lbl_video_1.clicked.connect(self.switch_video1_main)
        self.ui.setupUi(self)

    # 其他交互与逻辑处理
    def switch_video1_main(self):
        print("切换接口的视频")

    def handle_video(self, btn_id):
        print("打开的按钮id: ", btn_id)
        if btn_id == 100:
            pass
        if btn_id == 101:
            pass
        if btn_id == 102:
            pass
        if btn_id == 103:
            pass

    def modify_bright(self, val):
        print("调整亮度值: ", val)