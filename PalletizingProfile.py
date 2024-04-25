from PySide6.QtWidgets import (QMainWindow, QFileDialog, QListWidgetItem, QFrame, QVBoxLayout, QPushButton, QMessageBox, QLabel, QHBoxLayout, QWidget, QGridLayout, QLineEdit, QListWidget, QStackedLayout)
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon, QFont
from PIL.ImageQt import ImageQt
from PIL import Image as Img
from functools import partial
# from RobotMonitoring import *
from Utilities import *
from savejson  import *
from PopupPosition import *
from ManageJosnfiles import *
import json
import os
import numpy as np
import math
from math import atan2, cos, sin, sqrt, pi
from loadprofile import *
import matplotlib.pyplot as plt
from calpos import * 

class PalletizingProfile(QMainWindow):

    def __init__(self,exit_callback=None):
        super().__init__()     
        self.exit_callback=exit_callback
        #self.select_file()
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
        # self.pages = QStackedLayout()
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
        self.main_layout.addLayout(self.middle_layout)
        self.loadMenupage1()
        self.statusbar()

        self.test()


    def test(self):
        #Begin======================================== List Profile =====================================================
        print('')
        print(f'List palletizing profile: {loadprofile.ListAllProfile(profilecat="palletizing")}')#{self.ListAllProfile("palletizing")}
        print(f'List box profile: {loadprofile.ListAllProfile(profilecat="box")}')
        print(f'List pallet profile: {loadprofile.ListAllProfile(profilecat="pallet")}')
        #End========================================== List Profile =====================================================
        
        running_folder = os.getcwd()
        boxprofile_path = os.path.join(running_folder, "pallet_info","box")
        palletprofile_path = os.path.join(running_folder, "pallet_info","pallet")
        palletizingprofile_path = os.path.join(running_folder, "pallet_info","palletizing")
        pallet_pos_list = []
        with open(os.path.join(boxprofile_path, "1.dat"), "r") as file:
            data = json.load(file)
            size = data["size"]
            width, length, height = map(float, size)
            print("Return Box width, length, height: ", width, length, height)
        with open(os.path.join(palletprofile_path, "3.dat"), "r") as file:
            data = json.load(file)
            pallet_pos_list = data["size"]
            print("Return pallet_pos_list: ", pallet_pos_list)

        #Begin========================================== Input Profile =====================================================
        name = input("Input Profile Name): ")
        idx_pattern = int(input("Input index pattern type (0=block,1=brick,2=Pinwheel): "))
        print("Return index pattern type:", idx_pattern)
        num_layer = int(input("Input number of layer: "))
        print("Return number of layer", num_layer)
        num_box = int(input("Input number of box: "))
        print("Return number of box", num_box)
        gap_mm = float(input("Input gap .mm: "))
        print("Return gap .mm: ", gap_mm)
        #End========================================== Input Profile =====================================================

        if(idx_pattern == 0):
            print("Pattern type:", "block")
            item_position_list = cal_pos_arrange_box_pat0(pallet_pos_list,width,length,height,num_layer,num_box,gap_mm)
            print(f'item_position_list: {item_position_list}')





    def topbar(self):
        self.Ftop_bar = QFrame() 
        self.Ftop_bar.setObjectName("topBar")
        self.Ftop_bar.setContentsMargins(0,0,0,0)
        self.Ftop_bar.setFixedHeight(self.headerSize - self.redHeaderSize)
        
        self.cmdBack = QPushButton()
        self.cmdBack.setIcon(QIcon("resource/back.png"))
        self.cmdBack.setIconSize(QSize(self.logo_size,self.logo_size))
        self.cmdBack.clicked.connect(self.cmdBack_Click)
        self.cmdBack.setStyleSheet("background-color:#515151")
        self.cmdBack.setFlat(True)
        # self.positionclike=PositionDialog(self)
       
        self.tblTitlebar=QLabel("Palletizing Profile")
        self.tblTitlebar.setFixedHeight(self.headerSize - self.redHeaderSize)
        self.tblTitlebar.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        # self.tblTitlebar.setStyleSheet("font-size:"+str(30 if self.winfo_screenwidth>1366 else 20)+"px")
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
    def select_file(self):
        # file_name, _ = QFileDialog.getOpenFileName(self, "stylsheet.qss")
        with open('stylsheet.qss', 'r') as file:
            style_sheet = file.read()
            self.setStyleSheet(style_sheet)
       

            # self.setStyleSheet(stylesheet)

    @QtCore.Slot()
    def cmdCeate_Click(self):
        self.create_button.setParent(None)
        self.edit_button.setParent(None)
        self.delete_button.setParent(None)
        self.profile_list.setParent(None)
        self.loadMenupage2()

    @QtCore.Slot()
    def cmdBack_Click(self):
        self.showmainpage()
    
    def showmainpage(self):
        for i in range(1, 5): 
            
            self.labels[i].setParent(None)
            self.line_edits[i].setParent(None)
            self.line_edits[i].setText(None) 
            self.edit_buttons[i].setParent(None)

        self.cmdsave.setParent(None)  
        self.name_label.setParent(None)  
        self.name_line_edit.setParent(None) 
        self.pallet_graphic_label.setParent(None) 
        self.loadMenupage1()

    def cmdEdit_Click(self):
        # Get the currently selected item
        current_item = self.profile_list.currentItem()
        
        # print(str(intex))
        if current_item:
            # self.editor.setText()
            # You might want to open a new page or dialog here instead
            # For example, open a new dialog for editing
            self.create_button.setParent(None)
            self.edit_button.setParent(None)
            self.delete_button.setParent(None)
            self.profile_list.setParent(None)
            index =current_item.data(Qt.UserRole)
            self.loadMenupage2(index)
            # self.open_edit_page(current_item.text())
        else:
             QMessageBox.warning(self, "Selection Required", "กรุณาเลือกไอเท็มที่ต้องการแก้ไข.")
        
    
    def loadMenupage1(self) :
        
        self.new_page1_layout = QGridLayout()
        self.new_page1_layout.setContentsMargins(0,0,0,0)
        self.button_layout = QVBoxLayout()
        self.button_layout.setContentsMargins(0,0,0,0)
        button_size = int(self.headerSize )
        
        self.create_button = QPushButton("Create")
        self.create_button.setObjectName("darkGrayButton")
        self.create_button.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 16) + "px")
        #self.create_button.clicked.connect(self.cmdCeate_Click)

        self.edit_button = QPushButton("Edit")
        self.edit_button.setObjectName("grayButton")
        self.edit_button.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 16) + "px")
        #self.edit_button.clicked.connect(self.cmdEdit_Click)

        self.delete_button = QPushButton("Delete")
        self.delete_button.setObjectName("redButton")
        self.delete_button.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 16) + "px")
        #self.delete_button.clicked.connect(lambda: self.cmdDelete_Click(self.profile_list))

        # lambda: delete_selected_items(list_widget)

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
        self.addlistItem(loadprofile.ListAllProfile(profilecat="palletizing"))
        #self.addlistItem(Dojson.ListNameInfolder())
        self.profile_list.setFixedSize(self.winfo_screenwidth/2,self.winfo_screenheight/2)
        # self.profile_list.itemClicked.connect(self.showdata_Click)
        self.new_page1_layout.addWidget(self.profile_list, 0, 0, Qt.AlignVCenter)
        self.new_page1_layout.addLayout(self.button_layout, 0, 1,Qt.AlignVCenter)
       
       
        # Add the new page layout to the middle layout
        self.middle_layout.addLayout(self.new_page1_layout, 0, 0)

    def addlistItem (self,listitem):
        self.profile_list.clear()
        for name,index in listitem :
            
            item = QListWidgetItem(name)
            item.setData(Qt.UserRole,index)
            item.setFont(self.font)  # Apply the font to each item
            item.setSizeHint(QSize(self.headerSize, self.headerSize/2))  # Increase the height hint of the item
            self.profile_list.addItem(item)  # Add the item to the QListWidget

    def NeedReloadProfileInfo(self,saved):
        if saved:
            self.ReloadProfileInfo()
    
    def ReloadProfileInfo(self):
        total_profile = loadprofile.ListAllProfile(profilename="palletizing")
        # self.lblProfile.configure(text="  Total " + str(len(total_profile)) + " profile(s).")
        self.lblProfileStringVar.set("  Total " + str(len(total_profile)) + " profile(s).")

    #Unused
    def ListAllProfile(self,profilename):
        folder = os.getcwd()
        palletizingprofile_path = os.path.join(folder, "pallet_info",profilename)

        filelist = []
        names_list = []

        if(os.path.exists(palletizingprofile_path)):
            filelist = []
            for filename in os.listdir(palletizingprofile_path):
                if filename.endswith('.dat'):
                    name,ext = os.path.splitext(filename)
                    filelist.append(name)
                    file_path = os.path.join(palletizingprofile_path, filename)
                    try:
                        with open(file_path, 'r') as file:
                            data = json.load(file)
                            # Add the 'name' value to the list
                            names_list.append((data['name'], data['index']))
                
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from file {filename}")
                    except FileNotFoundError:
                        print(f"File {filename} not found")
                    except Exception as e:
                        print(f"An error occurred with file {filename}: {e}")
            
        return names_list

    