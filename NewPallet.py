from PySide6.QtWidgets import (QMainWindow, QFileDialog, QListWidgetItem, QFrame, QVBoxLayout, QPushButton, QMessageBox, QLabel, QHBoxLayout, QWidget, QGridLayout, QLineEdit, QListWidget, QStackedLayout)
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon, QFont
from PIL.ImageQt import ImageQt
from PIL import Image as Img
from functools import partial
from Utilities import *
from ManageJosnfiles import *
from PopupPosition import *
class NewPallet(QMainWindow):
    def __init__(self,exit_callback=None):
        super().__init__()
        self.index=None
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
        
        # self.Ftop_bar = QFrame() 
        # self.Ftop_bar.setObjectName("topBar")
        # self.Ftop_bar.setContentsMargins(0,0,0,0)
        # self.Ftop_bar.setFixedHeight(self.headerSize - self.redHeaderSize)
        
        # self.cmdBack = QPushButton()
        # self.cmdBack.setIcon(QIcon("resource/back.png"))
        # self.cmdBack.setIconSize(QSize(logo_size,logo_size))
        # self.cmdBack.clicked.connect(self.cmdBack_Click)
        # self.cmdBack.setStyleSheet("background-color:#515151")
        # self.cmdBack.setFlat(True)
        # # self.positionclike=PositionDialog(self)
       
        # self.tblTitlebar=QLabel("Pallet Profile")
        # self.tblTitlebar.setFixedHeight(self.headerSize - self.redHeaderSize)
        # self.tblTitlebar.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        # # self.tblTitlebar.setStyleSheet("font-size:"+str(30 if self.winfo_screenwidth>1366 else 20)+"px")
        # self.tblTitlebar.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 25) + "px")
        # palette = self.tblTitlebar.palette()
        # palette.setColor(self.tblTitlebar.foregroundRole(), QtGui.QColor(255,255,255))
        # self.tblTitlebar.setPalette(palette)
       
        # self.top_layout.addWidget(self.cmdBack,Qt.AlignLeft)
        # # self.top_layout.addStretch()
        # self.top_layout.addWidget(self.tblTitlebar,Qt.AlignCenter)
       
       
        
        # # self.main_layout.addLayout(self.top_layout)
        # self.Ftop_bar.setLayout(self.top_layout)
        
        # self.main_layout.addWidget(self.Ftop_bar)
        # self.setLayout(self.main_layout)
        self.topbar()
        self.main_layout.addLayout(self.middle_layout)
        self.loadMenupage1()
        self.statusbar()
        
       

       
        # self.frameRed = QFrame() 
        # self.frameRed.setFixedSize(self.winfo_screenwidth / 8,self.headerSize / 2)
        # # self.frameRed.setFixedHeight( self.frameStatus.setFixedSize(self.winfo_screenwidth / 8,self.headerSize / 2))
        # self.frameRed.setStyleSheet("background-color: #BE0E13") 
        # self.main_layout.addWidget(self.frameRed)
        # self.setLayout(self.main_layout)
       

        

        # self.status_h_layout = QHBoxLayout()
        # self.status_h_layout.setSpacing(0)
        # self.status_h_layout.setContentsMargins(0,0,0,0)

        # logo_size = int(self.headerSize / 2)
        # self.imgLogo = QLabel("")
        # qim = ImageQt(Img.open("resource/app_logo.png").resize((logo_size,logo_size)))
        # self.imgLogo.setPixmap(QPixmap.fromImage(qim))
        # self.imgLogo.setFixedSize(logo_size,logo_size)
        # self.status_h_layout.addWidget(self.imgLogo)

        # self.lblStatus = QLabel("Ready") 
        # self.lblStatus.setFixedSize((self.winfo_screenwidth / 8) - logo_size,logo_size)
        # self.lblStatus.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        # self.lblStatus.setStyleSheet("font-size: " + str(25 if self.winfo_screenwidth > 1366 else 20) + "px")
        # palette = self.lblStatus.palette()
        # palette.setColor(self.lblStatus.foregroundRole(), QtGui.QColor(255,255,255))
        # self.lblStatus.setPalette(palette)
        # self.status_h_layout.addWidget(self.lblStatus,Qt.AlignLeft|Qt.AlignBottom )

        # self.frameRed.setLayout(self.status_h_layout)
            
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
       
        self.tblTitlebar=QLabel("Pallet Profile")
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
    def select_file(self):
        # file_name, _ = QFileDialog.getOpenFileName(self, "stylsheet.qss")
        with open('stylsheet.qss', 'r') as file:
            style_sheet = file.read()
            self.setStyleSheet(style_sheet)
       

            # self.setStyleSheet(stylesheet)
        
        # self.paht="main"
    def addlistItem (self,listitem):
        self.profile_list.clear()
        for name,index in listitem :
            
            item = QListWidgetItem(name)
            item.setData(Qt.UserRole,index)
            item.setFont(self.font)  # Apply the font to each item
            item.setSizeHint(QSize(self.headerSize, self.headerSize/2))  # Increase the height hint of the item
            self.profile_list.addItem(item)  # Add the item to the QListWidget

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
        # for i in range(1, 5): 
            
        #     self.labels[i].setParent(None)
        #     self.line_edits[i].setParent(None)
        #     self.line_edits[i].setText(None) 
        #     self.edit_buttons[i].setParent(None)

        # self.cmdsave.setParent(None)  
        # self.name_label.setParent(None)  
        # self.name_line_edit.setParent(None) 
        # self.pallet_graphic_label.setParent(None) 
        # self.loadMenupage1()
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
        # self.profile_list
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
        
    @QtCore.Slot()
    def cmdEditPosition_Click(self,positon):
        self.ps = PositionDialog(positon,self)
    
    # แสดงป๊อปอัพด้วยการเรียก exec_()
        self.ps.exec_()
        # app = QApplication(sys.argv)
        # dialog = PositionDialog()
        # dialog.show()
        # sys.exit(app.exec())
    @QtCore.Slot()
    def cmdsave_Click(self):
        if not self.name_line_edit.text().strip():
            QMessageBox.warning(self, "ข้อมูลไม่ครบ", "กรุณาใส่ชื่อ ก่อนบันทึก.")
            return

        size = self.collect_positions()
        if size is not None:  # ตรวจสอบว่า size ไม่เป็น None (คือผ่านการตรวจสอบค่าว่าง)
            Dojson.save_pallet_profile(self.name_line_edit.text(), size, self.index)
            self.showmainpage()
        # else:
        #     # แสดงข้อความหรือดำเนินการอื่น ๆ หากพบว่ามีค่าว่าง
        #     QMessageBox.warning(self, "การบันทึกไม่สำเร็จ", "ไม่สามารถบันทึกข้อมูลที่มีค่าว่างได้.")
        # size = self.collect_positions()
        # Dojson.save_pallet_profile(self.name_line_edit.text(),size,self.index)
        # self.showmainpage()
    @QtCore.Slot()
    def cmdDelete_Click(self,list_widget):
        current_item = self.profile_list.currentItem()

        if current_item:
            index = current_item.data(Qt.UserRole)

            # สร้าง MessageBox สำหรับยืนยันการลบ
            reply = QMessageBox.question(self, 'ยืนยันการลบ',
                                        "คุณแน่ใจว่าต้องการลบไอเท็มนี้หรือไม่?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                # ถ้าผู้ใช้กด Yes, ทำการลบไฟล์
                success = Dojson.delete_specific_dat_file('D:\Cobo_AppVision\AppVisionTest\pallet_info\pallet', index)

                if success:
                    # ลบ item ออกจาก QListWidget
                    # for item in list_widget.selectedItems():
                    row = list_widget.row(current_item)
                    list_widget.takeItem(row)
                    # self.showmainpage()
                else:
                    QMessageBox.warning(self, "การลบล้มเหลว", "ไม่สามารถลบไอเท็มได้.")
            else:
                # ถ้าผู้ใช้กด No, ไม่ทำอะไรเลย
                pass
        else:
            QMessageBox.warning(self, "Selection Required", "กรุณาเลือกไอเท็มที่ต้องการลบ.")
       
    def collect_positions(self):
        size = []
        for i in range(1, 5):  # สมมุติว่ามี 4 ตำแหน่ง
            position_strs = self.line_edits[i].text().split(',')
                
                # ตรวจสอบว่าข้อมูลมีครบ 6 ตัวและไม่มีค่าว่างใดๆ
            if len(position_strs) != 6 or any(not x.strip() for x in position_strs):
                QMessageBox.warning(self, "ข้อมูลไม่ครบถ้วน", f"ตำแหน่งที่ {i} ต้องมี 6 ค่าครบถ้วนและไม่มีค่าว่าง.")
                return None  # หยุดการทำงานและส่งกลับ None เมื่อพบข้อผิดพลาด
                
                # แปลงสตริงเป็น float โดยลบช่องว่างและตรวจสอบความถูกต้องของข้อมูล
            try:
                position_values = [float(x.strip()) for x in position_strs]
            except ValueError:
                QMessageBox.warning(self, "ข้อมูลไม่ถูกต้อง", f"ตำแหน่งที่ {i} มีค่าที่ไม่สามารถแปลงเป็นตัวเลขได้.")
                return None
                
            size.append(position_values)
        return size
       
    def loadMenupage1(self) :
        # self.cmdsave.hide()
        self.new_page1_layout = QGridLayout()
        self.new_page1_layout.setContentsMargins(0,0,0,0)
        self.button_layout = QVBoxLayout()
        self.button_layout.setContentsMargins(0,0,0,0)
        button_size = int(self.headerSize )
        
        self.create_button = QPushButton("Create")
        self.create_button.setObjectName("darkGrayButton")
        self.create_button.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 16) + "px")
        self.create_button.clicked.connect(self.cmdCeate_Click)

        self.edit_button = QPushButton("Edit")
        self.edit_button.setObjectName("grayButton")
        self.edit_button.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 16) + "px")
        self.edit_button.clicked.connect(self.cmdEdit_Click)

        self.delete_button = QPushButton("Delete")
        self.delete_button.setObjectName("redButton")
        self.delete_button.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 16) + "px")
        self.delete_button.clicked.connect(lambda: self.cmdDelete_Click(self.profile_list))

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
        self.addlistItem(Dojson.ListNameInfolder())
        self.profile_list.setFixedSize(self.winfo_screenwidth/2,self.winfo_screenheight/2)
        # self.profile_list.itemClicked.connect(self.showdata_Click)
        self.new_page1_layout.addWidget(self.profile_list, 0, 0, Qt.AlignVCenter)
        self.new_page1_layout.addLayout(self.button_layout, 0, 1,Qt.AlignVCenter)
       
       
        # Add the new page layout to the middle layout
        self.middle_layout.addLayout(self.new_page1_layout, 0, 0)
        # self.main_layout.addLayout(self.middle_layout)
        # self.pages.setCurrentIndex(0)

    def loadMenupage2(self,index=None) :
      
        if index  is None:
            pass
        else :
            self.datalist=Dojson.find_pallet_profile(index)
            self.index=index
        # Set up the new page layout as per the provided image
        # print(self.datalist)
        self.cmdsave = QPushButton("Save")
        self.cmdsave.setObjectName("savebutton")
        # self.cmdsave.setStyleSheet("background-color:#BE0E13")
        self.cmdsave.setFixedSize(self.headerSize, self.headerSize/3)
        self.cmdsave.setStyleSheet("font-size: " + str(25 if self.winfo_screenwidth > 1366 else 16) + "px")
        self.cmdsave.clicked.connect(self.cmdsave_Click)
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.cmdsave,Qt.AlignRight)
        
        self.new_page2_layout = QGridLayout()
        
        # Create a placeholder for pallet graphic display
        self.pallet_graphic_label = QLabel()
        self.pallet_graphic_label = QLabel()
        # qim = ImageQt(Img.open("resource/pallet2d.png").resize((int(self.winfo_screenwidth//3), int(self.winfo_screenwidth//3))), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pixmap = QPixmap("resource/pallet2d.png").scaled(self.winfo_screenwidth//3.5, self.winfo_screenwidth//3.5, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pallet_graphic_label.setPixmap(pixmap)
        self.pallet_graphic_label.setAlignment(Qt.AlignVCenter|Qt.AlignCenter)
        self.pallet_graphic_label.setStyleSheet("background-color: #D3D3D3;")  # Placeholder color

        # Create form layout for the pallet information
        self.form_layout = QGridLayout()
        self.name_label = QLabel("Name :")
        self.name_line_edit = QLineEdit()
        self.form_layout.setContentsMargins(0,0,0,0)
        if index  is None:
            self.name_line_edit.setText("") 
        else :
            self.name_line_edit.setText( self.datalist['name']) 
            
        # self.name_line_edit.setText("Pallet_Test")  # Example default name
        self.name_label.setObjectName("Line")
        self.name_line_edit.setObjectName("Line")
        self.name_line_edit.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 18) + "px")
        self.name_label.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 18) + "px")
        self.form_layout.addWidget(self.name_label, 0, 0,Qt.AlignRight)
        self.form_layout.addWidget(self.name_line_edit, 0, 1,Qt.AlignCenter)

        self.edit_buttons = {}
        self.labels = {}
        self.line_edits = {}

        for i in range(1, 5):  # สร้างสำหรับแต่ละตำแหน่ง
            # สร้าง QLabel
            label = QLabel(f"Position {i} :")
            label.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 18) + "px")
            self.labels[i] = label
            self.labels[i].setObjectName("Line")
            self.form_layout.addWidget(label, i, 0,Qt.AlignRight)

            # สร้าง QLineEdit
            line_edit = QLineEdit()
            line_edit.setReadOnly(True)
            line_edit.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 18) + "px")
            self.line_edits[i] = line_edit
            self.line_edits[i].setObjectName("Line")
            
            self.form_layout.addWidget(line_edit, i, 1,Qt.AlignCenter)

            # สร้าง QPushButton
            edit_button = QPushButton(f"Edit")
            edit_button.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 18) + "px")
            self.edit_buttons[i] = edit_button
            self.edit_buttons[i].setObjectName("Linebtn")
            edit_button.clicked.connect(partial(self.openPositionDialog,i))
            self.form_layout.addWidget(edit_button, i, 2,Qt.AlignLeft)
        if index  is None:
           pass
        else :
            # self.name_line_edit.setText( self.datalist['name']) 
            positions = [", ".join(map(str, pos)) for pos in self.datalist['size']]
            for idx, position in enumerate(positions, start=1):
                # print(f"Position{idx}: {position}")
                self.line_edits[idx].setText(str(position)) 

        self.new_page2_layout.addWidget(self.pallet_graphic_label, 0, 0,Qt.AlignVCenter|Qt.AlignRight)
        self.new_page2_layout.addLayout(self.form_layout, 0, 1,Qt.AlignVCenter|Qt.AlignLeft)

      
        # Add the new page layout to the middle layout
        self.middle_layout.addLayout(self.new_page2_layout, 0, 0)
        # self.pages.setCurrentIndex(1)
       
    def openPositionDialog(self, position):
        positionDialog = PositionDialog(position)
        # เรียก exec_() และตรวจสอบว่าผู้ใช้กด OK หรือไม่
        if positionDialog.exec_() == QDialog.Accepted:
            # ดึงค่าที่ผู้ใช้ป้อนจาก PositionDialog
            values = positionDialog.getValues()
            
            # ทำการอัปเดต UI หรือข้อมูลใน NewPallet ตามค่าที่ได้รับ
            # ตัวอย่าง: อัปเดต QLineEdit สำหรับแสดงค่าที่ได้จาก PositionDialog
            # สมมติว่าคุณมี QLineEdit ใน NewPallet เพื่อแสดงค่าเหล่านี้
            self.updatePositionFields(position, values)
    def updatePositionFields(self, position, values):
        # ตัวอย่างเมธอดนี้แสดงวิธีอัปเดตค่าใน QLineEdit สำหรับแต่ละ position
        # คุณต้องปรับแต่งเพื่อให้ตรงกับโครงสร้าง UI ของคุณ
        position_string = "{},{},{},{},{},{}".format(values["X"], values["Y"], values["Z"], values["Rx"], values["Ry"], values["Rz"])
        self.line_edits[position].setText(str(position_string))
        
           
           
    
   
   
    
    


