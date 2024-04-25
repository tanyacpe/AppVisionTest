from PySide6.QtWidgets import (QMainWindow,QFileDialog, QListWidgetItem,QFrame,QVBoxLayout,QPushButton,QLabel,QHBoxLayout,QWidget,QGridLayout,QLineEdit,QListWidget)
from PySide6 import QtCore,QtGui,QtWidgets
from PySide6.QtCore import Qt,QThread,Signal,Slot,QSize
from PySide6.QtGui import QPixmap,QIcon,QFont
from PySide6.QtCore import QCoreApplication
import NewPallet
import Topbar_byWang
# from RobotMonitoring import *
import NewBox
from PalletizingProfile import PalletizingProfile
import os
import json

class RunMain():
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if not QtWidgets.QApplication.instance():
            self.run_qt_app=QtWidgets.QApplication([])
        else:
            self.run_qt_app=QtWidgets.QApplication.instance()
        self.NewWindow =NewPallet.NewPallet()
        # self.NewWindow =NewBox.NewBox()
        # self.NewWindow = PalletizingProfile() #PalletizingProfile(self,save_callback=self.NeedReloadProfileInfo)
        self.NewWindow.show()
        self.NewWindow.showFullScreen()
        print("Qt window started.")
        self.run_qt_app.exec()
    
    
     
    # def exit_Program(self):
    #     print("Run_Qt : close_run_window")
    #     self.NewWindow.close()
    #     self.run_qt_app.quit()
    #     QCoreApplication.quit()

# Robot_Thread=Robot_update_thread()
# Robot_Thread.start()

app=RunMain()