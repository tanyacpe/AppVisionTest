from tkinter import *
from tkinter import ttk
from tkinter.tix import Form
from turtle import width
import customtkinter
from customtkinter import *

# from MessageBox import MessageBox
import Utilities

from loadconfig import *
# from SerialPort import *

import Utilities
from _thread import *
import time

from PIL import Image as Img
from PIL.ImageQt import ImageQt

from PySide6.QtCore import Qt,QThread,Signal,Slot
from PySide6 import QtWidgets,QtGui,QtCore
from PySide6.QtGui import QImage,QPixmap
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QFrame, QVBoxLayout, QWidget)


class Topbar_Qt(QWidget):
    update_status = True
    main_v_layout = QVBoxLayout()
    h_layout = QHBoxLayout()
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)        
        screen = QtWidgets.QApplication.screenAt(QtGui.QCursor.pos())
        screenGeo = screen.geometry()
        self.winfo_screenwidth = screenGeo.width()
        self.winfo_screenheight = screenGeo.height()

        self.headerSize = self.winfo_screenheight * 0.1
        self.redHeaderSize = int(self.winfo_screenheight * 0.01)

        self.setFixedHeight(self.headerSize+1)
        self.setStyleSheet("background-color: " + Utilities.text_rgb("#515151") + ";") 

        self.main_v_layout = QVBoxLayout()
        self.main_v_layout.setSpacing(0)
        self.main_v_layout.setContentsMargins(0,0,0,0)

        self.h_layout = QHBoxLayout()
        self.h_layout.setSpacing(0)
        self.h_layout.setContentsMargins(0,0,0,0)
        
        self.Ftop_bar = QFrame() 
        self.Ftop_bar.setLayout(self.h_layout)
        self.Ftop_bar.setObjectName("topBar")
        self.Ftop_bar.setContentsMargins(0,0,0,0)
        self.Ftop_bar.setFixedHeight(self.headerSize - self.redHeaderSize)

        # self.configure(height=self.headerSize+1)
        # self.configure(width=self.winfo_screenwidth)
        # self.configure(fg_color='#515151')
        # self.configure(bg_color='#515151')
        # self.configure(corner_radius=0)

        # self.frameRed = customtkinter.CTkFrame(master,
        #                                         width=self.winfo_screenwidth(),
        #                                         height=self.redHeaderSize,
        #                                         corner_radius=0,
        #                                         fg_color='#BE0E13')
        # self.frameRed.place(x=0, y=self.headerSize)

        # self.h_layout = QHBoxLayout()
        # self.main_v_layout = QVBoxLayout()
        #====================== Label title ==========================
        if not hasattr(self,"lblTitle"):
            font_title = 30
            if self.winfo_screenwidth <= 1370:
                font_title = 25
            self.tblTitlebar=QLabel("")
            self.tblTitlebar.setFixedHeight(self.headerSize - self.redHeaderSize)
            self.tblTitlebar.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            # self.tblTitlebar.setStyleSheet("font-size:"+str(30 if self.winfo_screenwidth>1366 else 20)+"px")
            self.tblTitlebar.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 25) + "px")
            palette = self.tblTitlebar.palette()
            palette.setColor(self.tblTitlebar.foregroundRole(), QtGui.QColor(255,255,255))
            self.tblTitlebar.setPalette(palette)
            self.h_layout.addWidget(self.tblTitlebar)
            self.main_v_layout.addLayout(self.h_layout)
            # self.lblTitle = customtkinter.CTkLabel(self,
            #                                        width=self.winfo_screenwidth() / 2,
            #                                        height=self.headerSize,
            #                                        fg_color="transparent",
            #                                        text_color="#FFFFFF",
            #                                        textvariable=self.lblTitleStr)
            # self.lblTitle.cget("font").configure(size=30)
            # self.lblTitle.place(x=(self.winfo_screenwidth() / 4) , y=0)
        #=============================================================
            
        self.frameRed = QFrame() 
        self.frameRed.setFixedHeight(self.redHeaderSize)
        self.frameRed.setStyleSheet("background-color: " + Utilities.text_rgb("#BE0E13") + ";") 
        self.main_v_layout.addWidget(self.frameRed)
        self.setLayout(self.main_v_layout)
        
        # #====================== Robot Status =========================
        if not hasattr(self,"frameStatus"):
            self.frameStatus = QFrame() 
            self.frameStatus.setFixedSize(self.winfo_screenwidth / 8,self.headerSize / 2)
            # self.frameRed.setFixedHeight( self.frameStatus.setFixedSize(self.winfo_screenwidth / 8,self.headerSize / 2))
            self.frameStatus.setStyleSheet("background-color: " + Utilities.text_rgb("#BE0E13") + ";") 
            self.main_v_layout.addWidget(self.frameStatus)
            self.setLayout(self.main_v_layout)
        

            # if not hasattr(self,"frameStatus"):
            # self.frameStatus = QWidget()
            # self.frameStatus.setFixedSize(self.winfo_screenwidth / 8,self.headerSize / 2)
            # self.frameStatus.setStyleSheet("background-color: " + Utilities.text_rgb("#BE0E13") + ";") 

            self.status_h_layout = QHBoxLayout()
            self.status_h_layout.setSpacing(0)
            self.status_h_layout.setContentsMargins(0,0,0,0)

            logo_size = int(self.headerSize / 2)
            self.imgLogo = QLabel("")
            qim = ImageQt(Img.open("resource/app_logo.png").resize((logo_size,logo_size)))
            self.imgLogo.setPixmap(QPixmap.fromImage(qim))
            self.imgLogo.setFixedSize(logo_size,logo_size)
            self.status_h_layout.addWidget(self.imgLogo)

            self.lblStatus = QLabel("Ready") 
            self.lblStatus.setFixedSize((self.winfo_screenwidth / 8) - logo_size,logo_size)
            self.lblStatus.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.lblStatus.setStyleSheet("font-size: " + str(25 if self.winfo_screenwidth > 1366 else 20) + "px")
            palette = self.lblStatus.palette()
            palette.setColor(self.lblStatus.foregroundRole(), QtGui.QColor(255,255,255))
            self.lblStatus.setPalette(palette)
            self.status_h_layout.addWidget(self.lblStatus,Qt.AlignLeft|Qt.AlignBottom )

            self.frameStatus.setLayout(self.status_h_layout)

      
        # #=============================================================

    @Slot(str)
    def setStatus(self, status_text):
        self.tblTitlebar.setText(status_text)

class Robot_update_thread(QThread):
    StatusText = Signal(str)
    update_robot_status = True
    exit_robot_thread = False

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.trained_file = None
        self.status = True
        self.cap = True

    def exit_thread(self):
        self.exit_robot_thread = True

    def run(self):
        while not self.exit_robot_thread:
            if self.update_robot_status:
                try:
                    text_status = ""
                    if Utilities.RobotIsRunning:
                        text_status = "Running"
                    else:
                        if Utilities.TCPNotMatch == True:
                            text_status = "Err:TCP not match."
                        else:
                            text_status = "Ready"

                    if "ROBOT_ON_OK" in Utilities.ControllerReadBuffer:
                        text_status = "Connecting..."
                    elif Utilities.RobotIsIdle == False and Utilities.RobotIsRunning == False and Utilities.RobotIsConnected == False:
                        text_status = "Disconnected"
                    self.StatusText.emit(text_status)
                except:
                    
                    break
            time.sleep(0.3)


