from PyQt5.QtWidgets import QApplication
from trafficapp.uis.trafficframe import WTrafficDialog
from trafficapp.uis.trafficloginframe import WTrafficLoginDialog


class WTrafficApp(QApplication):
    def __init__(self):
        super(WTrafficApp, self).__init__([])
        self. dlg = WTrafficDialog()
        self.dlg.show()
    
    # 可以增加应用层的处理 