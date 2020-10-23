from PyQt5.QtWidgets import QDialog
from trafficapp.uis.trafficui import Ui_Traffic
from trafficapp.uis.trafficdev import WTrafficDev
from PyQt5.QtGui import QImage, QPixmap

class WTrafficDialog(QDialog):
    def __init__(self):
        super(WTrafficDialog, self).__init__()
        self.ui = Ui_Traffic()
        self.ui.setupUi(self)
        self.ui.lbl_video_1.clicked.connect(self.switch_video1_main)
        self.ui.lbl_video_2.clicked.connect(self.switch_video2_main)
        self.ui.lbl_video_3.clicked.connect(self.switch_video3_main)
        self.ui.lbl_video_4.clicked.connect(self.switch_video4_main)
        self.ui.lbl_video_5.clicked.connect(self.switch_video5_main)
        self.ui.lbl_video_6.clicked.connect(self.switch_video6_main)
        self.ui.lbl_video_7.clicked.connect(self.switch_video7_main)
        # 创建线程
        self.th_1 = WTrafficDev(1, 0)
        self.th_2 = WTrafficDev(2, "交通视频.mp4")
        self.th_3 = WTrafficDev(3, "交通视频.mp4")
        self.th_4 = WTrafficDev(4, "交通视频.mp4")
        self.th_5 = WTrafficDev(5, "交通视频.mp4")
        self.th_6 = WTrafficDev(6, "交通视频.mp4")
        self.th_7 = WTrafficDev(7, "交通视频.mp4")
        # 绑定视频槽函数
        self.th_1.sign_video.connect(self.show_video)
        self.th_2.sign_video.connect(self.show_video)
        self.th_3.sign_video.connect(self.show_video)
        self.th_4.sign_video.connect(self.show_video)
        self.th_5.sign_video.connect(self.show_video)
        self.th_6.sign_video.connect(self.show_video)
        self.th_7.sign_video.connect(self.show_video)
        
        # 启动线程
        self.th_1.start()
        self.th_2.start()
        self.th_3.start()
        self.th_4.start()
        self.th_5.start()
        self.th_6.start()
        self.th_7.start()

    
    # 其他交互与逻辑处理
    def show_video(self, data, h, w, c, th_id):
        qimg = QImage(data, w, h, w*c, QImage.Format_RGB888)
        qpixmap = QPixmap.fromImage(qimg)
        
        if th_id == 1:
            self.show_video_in_label(self.ui.lbl_video_1,qpixmap)
        if th_id == 2:
            self.show_video_in_label(self.ui.lbl_video_2,qpixmap)
        if th_id == 3:
            self.show_video_in_label(self.ui.lbl_video_3,qpixmap)
        if th_id == 4:
            self.show_video_in_label(self.ui.lbl_video_4,qpixmap)
        if th_id == 5:
            self.show_video_in_label(self.ui.lbl_video_5,qpixmap)
        if th_id == 6:
            self.show_video_in_label(self.ui.lbl_video_6,qpixmap)
        if th_id == 7:
            self.show_video_in_label(self.ui.lbl_video_7,qpixmap)

    def show_video_in_label(self, component, img):
        component.setPixmap(img)
        component.setScaledContents(True)

    def switch_video1_main(self):
        print("切换街口的视频：", 1)
    def switch_video2_main(self):
        print("切换街口的视频：", 2)
    def switch_video3_main(self):
        print("切换街口的视频：", 3)
    def switch_video4_main(self):
        print("切换街口的视频：", 4)
    def switch_video5_main(self):
        print("切换街口的视频：", 5)
    def switch_video6_main(self):
        print("切换街口的视频：", 6)
    def switch_video7_main(self):
        print("切换街口的视频：", 7)
    

    def handle_video(self, btn_id):
        print("打开的按钮id：", btn_id)
        if btn_id == 100:
            pass
        if btn_id == 101:
            pass
        if btn_id == 102:
            pass
        if btn_id == 103:
            pass    

    def modify_bright(self, val):
        print("调整亮度值：", val)