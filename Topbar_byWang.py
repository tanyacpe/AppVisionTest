from PySide6.QtWidgets import (QMainWindow,QFileDialog, QListWidgetItem,QFrame,QVBoxLayout,QPushButton,QLabel,QHBoxLayout,QWidget,QGridLayout,QLineEdit,QListWidget)
from PySide6 import QtCore,QtGui,QtWidgets
from PySide6.QtCore import Qt,QThread,Signal,Slot,QSize
from PySide6.QtGui import QPixmap,QIcon,QFont
from PIL.ImageQt import ImageQt
from PIL import Image as Img
from functools import partial
# from RobotMonitoring import *
from Utilities import *
from savejson  import *
from PopupPosition import *
from NewPallet import *
class NewPallet(QMainWindow):
    def __init__(self,exit_callback=None):
        super().__init__()
        
        self.exit_callback=exit_callback
        self.select_file()
        screen=QtWidgets.QApplication.screenAt(QtGui.QCursor.pos())
        screenGeo=screen.geometry()
        self.winfo_screenwidth=screenGeo.width()
        self.winfo_screenheight=screenGeo.height()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        


        self.main_layout = QVBoxLayout(central_widget) 
        self.main_layout.setContentsMargins(0,0,0,0)


        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0,0,0,0)
       


        self.middle_layout = QGridLayout()
        self.middle_layout.setContentsMargins(0,0,0,0)

        self.font = QFont()
        self.font.setPointSize(25)
        
        self.headerSize = self.winfo_screenheight * 0.1
        self.logo_size = int(self.headerSize / 2)
        self.camHeight=int(self.winfo_screenheight*0.7)
        self.camWidth=int(self.camHeight/0.8366)
     
        self.redHeaderSize = int(self.winfo_screenheight * 0.01)
        self.inputArea=self.winfo_screenwidth*0.4
        self.topbar()
        # listItem=["Pocky", "Colon", "Pallet_Test", "Pallet_Demo","Pallet_Demo1"]
        # self.loadMenupage1(listItem)

        self.statusbar()
    def loadMenupage1(self,listItem) :
        # self.cmdsave.hide()
        self.new_page1_layout = QGridLayout()
        self.new_page1_layout.setContentsMargins(0,0,0,0)
        self.button_layout = QVBoxLayout()
        self.button_layout.setContentsMargins(0,0,0,0)
        button_size = int(self.headerSize )
        
        self.create_button = QPushButton("Create")
        self.create_button.setObjectName("darkGrayButton")
        self.create_button.clicked.connect(self.cmdCeateEdit_Click)

        self.edit_button = QPushButton("Edit")
        self.edit_button.setObjectName("grayButton")
        self.edit_button.clicked.connect(self.cmdCeateEdit_Click)

        self.delete_button = QPushButton("Delete")
        self.delete_button.setObjectName("redButton")

        self.create_button.setFixedSize(button_size, button_size)
        self.edit_button.setFixedSize(button_size, button_size)
        self.delete_button.setFixedSize(button_size, button_size)
        # self.delete_button.setStyleSheet("background-color: red; color: white;")
        self.button_layout.setContentsMargins(0,0,0,0)
        self.button_layout.addWidget(self.create_button,alignment=Qt.AlignVCenter)
        self.button_layout.addWidget(self.edit_button,alignment=Qt.AlignVCenter )
        self.button_layout.addWidget(self.delete_button,alignment=Qt.AlignVCenter)
        # self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding) 
        # self.button_layout.addItem(self.verticalSpacer)
        
        self.profile_list = QListWidget()
        self.profile_list.setIconSize(QSize(64, 64))
        self.addlistItem(listItem)
        self.profile_list.setFixedSize(self.winfo_screenwidth/2,self.winfo_screenheight/2)
        
        self.new_page1_layout.addWidget(self.profile_list, 0, 0, Qt.AlignVCenter)
        self.new_page1_layout.addLayout(self.button_layout, 0, 1,Qt.AlignVCenter)
       
       
        # Add the new page layout to the middle layout
        self.middle_layout.addLayout(self.new_page1_layout, 0, 0)
        self.main_layout.addLayout(self.middle_layout)
    @QtCore.Slot()
    def cmdCeateEdit_Click(self):
        self.create_button.setParent(None)
        self.edit_button.setParent(None)
        self.delete_button.setParent(None)
        self.profile_list.setParent(None)
        # self.loadMenupage2()
    def addlistItem (self,listitem):
        for text in listitem :
            pixmap = QPixmap("resource/app_logo.png").scaled(64, 64)  # Use the size you want for icons
            icon = QIcon(pixmap)
            item = QListWidgetItem(icon, text)
                # item = QListWidgetItem(text)
            item.setFont(self.font)  # Apply the font to each item
            item.setSizeHint(QSize(50, 80))  # Increase the height hint of the item
            self.profile_list.addItem(item)  # Add the item to the QListWidget
    def topbar(self):
        self.Ftop_bar = QFrame() 
        self.Ftop_bar.setObjectName("topBar")
        self.Ftop_bar.setContentsMargins(0,0,0,0)
        self.Ftop_bar.setFixedHeight(self.headerSize - self.redHeaderSize)
            
        self.cmdBack = QPushButton()
        self.cmdBack.setIcon(QIcon("resource/back.png"))
        self.cmdBack.setIconSize(QSize(self.logo_size,self.logo_size))
        
        self.cmdBack.setStyleSheet("background-color:#515151")
        self.cmdBack.setFlat(True)
            # self.positionclike=PositionDialog(self)
        
        self.tblTitlebar=QLabel()
        self.settexttopbar("Pallet Profile")
        self.tblTitlebar.setFixedHeight(self.headerSize - self.redHeaderSize)
        self.tblTitlebar.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        
        self.tblTitlebar.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 25) + "px")
        palette = self.tblTitlebar.palette()
        palette.setColor(self.tblTitlebar.foregroundRole(), QtGui.QColor(255,255,255))
        self.tblTitlebar.setPalette(palette)
        
        self.top_layout.addWidget(self.cmdBack,Qt.AlignLeft)
            # self.top_layout.addStretch()
        self.top_layout.addWidget(self.tblTitlebar,Qt.AlignCenter)
        
        
            
            # self.main_layout.addLayout(self.top_layout)
        self.Ftop_bar.setLayout(self.top_layout)
            
        self.main_layout.addWidget(self.Ftop_bar)
        self.setLayout(self.main_layout)
        
       
      
        # self.loadMenupage1(listItem)
    def settexttopbar(self,text):
        self.tblTitlebar.setText(text)
    def statusbar(self):
        #stausbar
        self.frameRed = QFrame() 
        self.frameRed.setFixedSize(self.winfo_screenwidth / 8,self.headerSize / 2)
            # self.frameRed.setFixedHeight( self.frameStatus.setFixedSize(self.winfo_screenwidth / 8,self.headerSize / 2))
        self.frameRed.setStyleSheet("background-color: #BE0E13") 
        self.main_layout.addWidget(self.frameRed)
        self.setLayout(self.main_layout)
        

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

        self.frameRed.setLayout(self.status_h_layout)
            
        # self.robot_thread = Robot_update_thread(self)
        # self.robot_thread.finished.connect(self.close)
        # self.robot_thread.StatusText.connect(self.setStatus)
        # self.robot_thread.start()

        # self.main_layout.addLayout(self.frameStatus)

        # central_widget = QWidget()
        # central_widget.setLayout(self.main_layout)
        # self.setCentralWidget(central_widget)
    def select_file(self):
        # file_name, _ = QFileDialog.getOpenFileName(self, "stylsheet.qss")
        with open('stylsheet.qss', 'r') as file:
            style_sheet = file.read()
            self.setStyleSheet(style_sheet)
       

            # self.setStyleSheet(stylesheet)
        
        # self.paht="main"
 
  