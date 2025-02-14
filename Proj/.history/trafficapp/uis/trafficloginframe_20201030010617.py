from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from trafficapp.uis.loginui import Ui_Login
from trafficapp.uis.trafficlogindev import WTrafficLoginDev
from PyQt5.QtGui import QImage, QPixmap

class WTrafficLoginDialog(QDialog):
    def __init__(self, parent=None):
        # Qt.CustomizeWindowHint->Turns off the default window title hints.
        # Qt.WindowTitleHint->Gives the window a title bar.
        # https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.WindowType.html
        super(WTrafficLoginDialog, self).__init__(parent, Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        # super(WTrafficLoginDialog, self).__init__(parent,Qt.FramelessWindowHint)

        # setModal(False)非模态对话框
        # https://blog.csdn.net/fansofjava/article/details/71353019
        # 1，模态对话
        # （1）禁用父窗口；
        # （2）调用CDialog::DoModal创建对话框，；
        # （3）调用::EndDialog关闭对话框；
        # （4）无须指定WS_VISIBLE风格，会自动显示；
        # （5）生命周期短

        # 2，非模态对话框
        # （1）不禁用父窗口；
        # （2）调用CDialog::Create函数创建对话框；
        # （3）调用::DestroyWindow关闭；
        # （4）须指定WS_VISIBLE风格才能显示；
        # （5）生命周期长
        self.setModal(False)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        # 启动视频采集线程
        self.th = WTrafficLoginDev(0)
        self.th.sign_video.connect(self.show_video)
        self.th.start()
    
    def show_video(self, data, h, w, c, is_valid):
        qimg = QImage(data, w, h, w*c, QImage.Format_RGB888)
        qpixmap = QPixmap.fromImage(qimg)
        self.ui.lbl_video.setPixmap(qpixmap)
        self.ui.lbl_video.setScaledContents(True)
        if is_valid:
            # print("登录成功!")
            self.close() # 关闭登录窗体，显示主窗体
            self.parentWidget().show()
            self.parentWidget().init_dev()
            
        else:
            # print("登录中.........")
            pass
    
    def closeEvent(self, e):
        # 释放摄像头
        self.th.close()


