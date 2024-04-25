from PySide6.QtWidgets import (QMainWindow,QFileDialog, QListWidgetItem,QFrame,QVBoxLayout,QPushButton,QLabel,QHBoxLayout,QWidget,QGridLayout,QLineEdit,QListWidget)
from PySide6 import QtCore,QtGui,QtWidgets
from PySide6.QtCore import Qt,QThread,Signal,Slot,QSize
from PySide6.QtGui import QPixmap,QIcon,QFont
from PIL.ImageQt import ImageQt
from PIL import Image as Img
from functools import partial
# from RobotMonitoring import *
from Utilities import *
#from savejson  import *
#from PopupPosition import *
#from NewPallet import *
import json

class NewBox(QMainWindow):
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
        # self.middle_layout.setContentsMargins(0,0,0,0) edit to 200 becase I want to move to the right 200
        self.middle_layout.setContentsMargins(200,0,0,0)

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
        self.showAllJSON()

        self.statusbar()
    # def loadMenupage1(self,listItem) :
    #     # self.cmdsave.hide()
    #     self.new_page1_layout = QGridLayout()
    #     self.new_page1_layout.setContentsMargins(0,0,0,0)
    #     self.button_layout = QVBoxLayout()
    #     self.button_layout.setContentsMargins(0,0,0,0)
    #     button_size = int(self.headerSize )
        
    #     self.create_button = QPushButton("Create")
    #     self.create_button.setObjectName("darkGrayButton")
    #     self.create_button.clicked.connect(self.cmdCreateEdit_Click)

    #     self.edit_button = QPushButton("Edit")
    #     self.edit_button.setObjectName("grayButton")
    #     self.edit_button.clicked.connect(self.cmdCreateEdit_Click)

    #     self.delete_button = QPushButton("Delete")
    #     self.delete_button.setObjectName("redButton")

    #     self.create_button.setFixedSize(button_size, button_size)
    #     self.edit_button.setFixedSize(button_size, button_size)
    #     self.delete_button.setFixedSize(button_size, button_size)
    #     # self.delete_button.setStyleSheet("background-color: red; color: white;")
    #     self.button_layout.setContentsMargins(0,0,0,0)
    #     self.button_layout.addWidget(self.create_button,alignment=Qt.AlignVCenter)
    #     self.button_layout.addWidget(self.edit_button,alignment=Qt.AlignVCenter )
    #     self.button_layout.addWidget(self.delete_button,alignment=Qt.AlignVCenter)
    #     # self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding) 
    #     # self.button_layout.addItem(self.verticalSpacer)
        
    #     self.profile_list = QListWidget()
    #     self.profile_list.setIconSize(QSize(64, 64))
    #     self.addlistItem(listItem)
    #     self.profile_list.setFixedSize(self.winfo_screenwidth/2,self.winfo_screenheight/2)
        
    #     self.new_page1_layout.addWidget(self.profile_list, 0, 0, Qt.AlignVCenter)
    #     self.new_page1_layout.addLayout(self.button_layout, 0, 1,Qt.AlignVCenter)
       
       
    #     # Add the new page layout to the middle layout
    #     self.middle_layout.addLayout(self.new_page1_layout, 0, 0)
    #     self.main_layout.addLayout(self.middle_layout)
    # @QtCore.Slot()
    # def cmdCreateEdit_Click(self):
    #     self.create_button.setParent(None)
    #     self.edit_button.setParent(None)
    #     self.delete_button.setParent(None)
    #     self.profile_list.setParent(None)
    #     # self.loadMenupage2()
    # def addlistItem (self,listitem):
    #     for text in listitem :
    #         pixmap = QPixmap("resource/app_logo.png").scaled(64, 64)  # Use the size you want for icons
    #         icon = QIcon(pixmap)
    #         item = QListWidgetItem(icon, text)
    #             # item = QListWidgetItem(text)
    #         item.setFont(self.font)  # Apply the font to each item
    #         item.setSizeHint(QSize(50, 80))  # Increase the height hint of the item
    #         self.profile_list.addItem(item)  # Add the item to the QListWidget
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
        # self.settexttopbar("Pallet Profile")
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

    def showAllJSON(self):
        # Set default path
        default_path = r"C:\\Users\\tanyawan\\Documents\\GitHub\\AppVisionTest\\pallet_info\\box"

        # Scan the directory for existing JSON files
        existing_files = [f for f in os.listdir(default_path) if f.endswith('.json')]

        # Retrieve screen dimensions
        # screen = QtWidgets.QApplication.screenAt(QtGui.QCursor.pos())
        # screenGeo = screen.geometry()
        # winfo_screenwidth = screenGeo.width()
        # winfo_screenheight = screenGeo.height()

        # Top bar
        #self.h_topbar = QtWidgets.QHBoxLayout()

        # self.cmdBack = QPushButton()
        # self.cmdBack.setIcon(QIcon("resource/back.png"))
        # self.cmdBack.setIconSize(QSize(self.logo_size,self.logo_size))
      
        # self.cmdBack.setStyleSheet("background-color:#515151")
        # self.cmdBack.setFlat(True)

        # self.top_layout.insertWidget(0,self.cmdBack,Qt.AlignLeft)

        # Add back button (old)
        # self.cmdBack = QtWidgets.QPushButton("Back")
        # self.cmdBack.clicked.connect(self.cmdBack_Click)
        # self.h_topbar.addWidget(self.cmdBack)

        # self.mainTitle = QtWidgets.QLabel("Box Profile")
        # self.mainTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.h_topbar.addWidget(self.mainTitle)

        self.settexttopbar("Box Profile")

        # Create a QTableView
        self.tableView = QtWidgets.QTableView()

        # Create a QStandardItemModel
        self.model = QtGui.QStandardItemModel()

        # Set column headers
        self.model.setHorizontalHeaderLabels(['Name', 'Size'])

        for file_name in existing_files:
            full_path = os.path.join(default_path, file_name)
            with open(full_path, 'r') as f:
                data = json.load(f)
                
                # Extracting size information from the 'size' key in the JSON data
                size_info = ', '.join(map(str, data['size']))  # Convert list to comma-separated string
                
                name_item = QtGui.QStandardItem("Box" + data['name'])
                size_item = QtGui.QStandardItem(size_info)  # Create an item for size information
                self.model.appendRow([name_item, size_item])  # Append both items to the row


        # Set the model to the QTableView
        #self.tableView.setModel(self.model)

        #self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Set the size and position of the QTableView
        #self.tableView.setFixedSize(self.winfo_screenwidth * 0.3, self.winfo_screenheight * 0.6)
        #self.tableView.move(self.winfo_screenwidth * 0.6, self.winfo_screenheight * 0.1)

        # Hide column headers
        #self.tableView.horizontalHeader().hide()

        # Hide row numbers
        #self.tableView.verticalHeader().hide()

        # Set the model to the QTableView
        self.tableView.setModel(self.model)

        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Set the size and position of the QTableView
        self.tableView.setFixedSize(self.winfo_screenwidth * 0.8, self.winfo_screenheight * 0.6)
        #self.tableView.move(self.winfo_screenwidth * 0.6, self.winfo_screenheight * 0.1)

         # Set the model to the QTableView
        # Set the model to the QTableView
        

        # Set column sizes
        self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)

        # Set fixed size for each column
        self.tableView.setColumnWidth(0, self.winfo_screenwidth * 0.8 / 5)  # Set width for the first column
        self.tableView.setColumnWidth(1, self.winfo_screenwidth * 4 * 0.8 / 5)  # Set width for the second column

        # Set content alignment to center for each column
        for row in range(self.model.rowCount()):
            for col in range(self.model.columnCount()):
                self.model.setData(self.model.index(row, col), Qt.AlignCenter, Qt.TextAlignmentRole)


        # Hide column headers
        self.tableView.horizontalHeader().hide()

        # Hide row numbers
        self.tableView.verticalHeader().hide()

        # Add view all JSON button
        # self.btnCreate = QtWidgets.QPushButton("Create")
        # self.btnCreate.clicked.connect(self.loadPalletMenu)
        # self.h_topbar.addWidget(self.btnCreate)

        # Layout setup
        # self.v_main_layout = QtWidgets.QVBoxLayout()
        # self.v_main_layout.addLayout(self.h_topbar)

        # Add space between top bar and QTableView
        # spacer = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        # self.v_main_layout.addItem(spacer)

        # Add the QTableView to the main layout
        # self.v_main_layout.addWidget(self.tableView)
        

        self.create_button = QPushButton("Create")
        self.create_button.setObjectName("darkGrayButton")
        self.create_button.clicked.connect(self.cmdCreateBox_Click)

        self.edit_button = QPushButton("Edit")
        self.edit_button.setObjectName("grayButton")
        self.edit_button.setVisible(False)  # Initially set to invisible
        self.edit_button.clicked.connect(self.cmdCreateEdit_Click)

        self.delete_button = QPushButton("Delete")
        self.delete_button.setObjectName("redButton")
        self.delete_button.setVisible(False)
        self.delete_button.clicked.connect(self.cmdDelete_Click)

        self.button_layout = QVBoxLayout()
        self.button_layout.setContentsMargins(0,0,0,0)
        button_size = int(self.headerSize)

        self.create_button.setFixedSize(button_size, button_size)
        self.edit_button.setFixedSize(button_size, button_size)
        self.delete_button.setFixedSize(button_size, button_size)
        # self.delete_button.setStyleSheet("background-color: red; color: white;")
        self.button_layout.setContentsMargins(0,0,0,0)
        self.button_layout.addWidget(self.create_button,alignment=Qt.AlignVCenter)
        self.button_layout.addWidget(self.edit_button,alignment=Qt.AlignVCenter )
        self.button_layout.addWidget(self.delete_button,alignment=Qt.AlignVCenter)

        self.middle_layout.addWidget(self.tableView,0,0,Qt.AlignVCenter|Qt.AlignRight)
        # self.main_layout.addLayout(self.middle_layout,Qt.AlignCenter|Qt.AlignVCenter)
        self.middle_layout.addLayout(self.button_layout,0,1,Qt.AlignVCenter|Qt.AlignLeft)
        self.main_layout.addLayout(self.middle_layout)

        

        # # Widget to hold the QTableView
        # widget = QtWidgets.QWidget()
        # widget.setLayout(self.v_main_layout)

        # # Set the central widget to hold both the top bar and the QTableView
        # main_layout = QtWidgets.QHBoxLayout()
        # main_layout.addWidget(widget)
        
        # central_widget = QtWidgets.QWidget()
        # central_widget.setLayout(main_layout)
        # self.setCentralWidget(central_widget)

        #  # Add edit button to top bar
        # self.btnEdit = QtWidgets.QPushButton("Edit")
        # self.btnEdit.clicked.connect(self.switchToEditPage)
        # self.btnEdit.setVisible(False)  # Initially set to invisible
        # self.h_topbar.addWidget(self.btnEdit)

        # self.btnDelete = QtWidgets.QPushButton("Delete")
        # self.btnDelete.clicked.connect(self.delete_json)
        # self.btnDelete.setVisible(False)  # Initially set to invisible
        # self.h_topbar.addWidget(self.btnDelete)

        # # Connect selectionChanged signal to showEditButton method
        self.tableView.selectionModel().selectionChanged.connect(self.showEditButton)

        print("viewwwwwwwwwwwwwwwwwwww")


    def showEditButton(self, selected, deselected):
        # Check if any row is selected
        if selected.indexes():
            # Show the Edit button
            self.edit_button.show()
            self.delete_button.show()
            
        else:
            # Hide the Edit button
            self.edit_button.hide()
            self.delete_button.hide()
            


    def cmdCreateEdit_Click(self):
        # Get the selected row index
        indexes = self.tableView.selectionModel().selectedIndexes()
        if indexes:
            row = indexes[0].row()

            # Retrieve the JSON data for the selected row
            file_name = self.model.item(row, 0).text().replace("Box", "") + ".json"  # Assuming the name item contains the file name
            self.loadSelectedJsonFileFromList(file_name, None)

            # Switch to the edit page
            #self.stacked_widget.setCurrentWidget(self.edit_page)

    def cmdDelete_Click(self):
        # Get the selected row index
        indexes = self.tableView.selectionModel().selectedIndexes()
        
        if indexes:
            row = indexes[0].row()

            # Retrieve the JSON data for the selected row
            file_name = self.model.item(row, 0).text().replace("Box", "") + ".json"  # Assuming the name item contains the file name
            full_path = os.path.join("C:\\Users\\USER\\Desktop\\AppVisionTest\\AppVisionTest\\pallet_info\\box", file_name)
            
            # Delete the file
            try:
                os.remove(full_path)
                print(f"Deleted file: {full_path}")
                
                # Remove the row from the model
                self.model.removeRow(row)
                
                # Clear the selection
                self.tableView.clearSelection()
                
                # Hide the Edit and Delete buttons
                self.btnEdit.hide()
                self.btnDelete.hide()
                
            except Exception as e:
                print(f"Error deleting file: {e}")


    def get_next_filename(self, default_path):
        # Scan the directory for existing JSON files
        existing_files = [int(f.split('.')[0]) for f in os.listdir(default_path) if f.endswith('.json') and f.split('.')[0].isdigit()]
        
        # Find the next sequential number
        next_number = 1
        while next_number in existing_files:
            next_number += 1
        
        return f"{next_number}.json"
    
    def cmdCreateBox_Click(self):

        self.tableView.setParent(None)
        self.create_button.setParent(None)
        self.edit_button.setParent(None)
        self.delete_button.setParent(None)
        
        self.next_number = self.get_next_filename("C:\\Users\\USER\\Desktop\\AppVisionTest\\AppVisionTest\\pallet_info\\box")
        
        # Top bar
        # self.h_topbar = QHBoxLayout()

        # Add back button
        # self.cmdBack = QPushButton("Back")
        # self.cmdBack.setFixedHeight(self.inputArea * 0.1)
        # self.cmdBack.setStyleSheet(
        #     "font-size: " + str(30 if self.winfo_screenwidth > 1366 else 20) + "px"
        # )
        # self.cmdBack.clicked.connect(self.cmdBack_Click)
        # self.h_topbar.addWidget(self.cmdBack)

        # self.mainTitle = QLabel("Box Profile")
        # self.mainTitle.setAlignment(Qt.AlignCenter)
        # self.h_topbar.addWidget(self.mainTitle)

        # Add view all JSON button
        self.btnSave = QPushButton("Save")
        self.btnSave.setObjectName("savebutton")
        # self.btnSave.setFixedHeight(self.inputArea * 0.1)
        self.btnSave.setFixedSize(self.headerSize,self.headerSize/3)
        self.btnSave.setStyleSheet(
            "font-size: " + str(30 if self.winfo_screenwidth > 1366 else 20) + "px"
        )
        self.btnSave.clicked.connect(self.saveDataToJson)
        # self.h_topbar.addWidget(self.btnViewAll)

        self.top_layout.addWidget(self.btnSave)

        # Main content
        self.label = QLabel("Hello World")

        # Text label
        self.camHeight = int(self.winfo_screenheight * 0.7)
        self.camWidth = int(self.camHeight / 0.8366)
        self.label.setFixedSize(self.camWidth, self.camHeight)
        self.label.setStyleSheet("background-color: grey; font-size: " + str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        palette = self.label.palette()
        palette.setColor(self.label.foregroundRole(), QtGui.QColor(255,255,255))
        self.label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.label.setPalette(palette)
        
        
        # Add image
        qim = ImageQt(Img.open("resource/pallet3d.png").resize((self.camWidth,self.camHeight)))
        self.label.setPixmap(QPixmap.fromImage(qim))
        self.middle_layout.addWidget(self.label,0,0,Qt.AlignCenter|Qt.AlignRight)
        
        #self.middle_layout.setContentsMargins(0,0,0,0)

        # Input width, height, lenght, Weight 
        # Before self.inputArea = self.winfo_screenwidth * 0.4
        self.inputArea = self.winfo_screenwidth * 0.3
        self.load_grid_layout = QGridLayout()
        self.middle_layout.addLayout(self.load_grid_layout,0,1,Qt.AlignCenter|Qt.AlignVCenter)
        self.lblPalletName = QLabel("Box Name: ")
        self.lblPalletName.setObjectName("Line")
        self.lblPalletName.setFixedSize(self.inputArea/2,40)
        self.lblPalletName.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletName, 1, 0)

        self.txtPalletName = QLabel()
        self.txtPalletName.setObjectName("Line")
        self.txtPalletName.setText("Box" + self.next_number)  # Corrected to use self.next_number
        self.txtPalletName.setFixedSize(self.inputArea/2, 40)
        self.txtPalletName.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.txtPalletName, 1, 1)

        self.lblPalletWidth = QLabel("Box Width: ")
        self.lblPalletWidth.setObjectName("Line")
        self.lblPalletWidth.setFixedSize(self.inputArea/2,40)
        self.lblPalletWidth.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletWidth, 2, 0)

        self.txtPalletWidth = QLineEdit("")
        self.txtPalletWidth.setObjectName("Linebtn")
        self.txtPalletWidth.setFixedSize(self.inputArea/2,40)
        self.txtPalletWidth.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.txtPalletWidth, 2, 1)

        self.lblPalletWidthUnit = QLabel("mm.")
        self.lblPalletWidthUnit.setObjectName("Line")
        self.lblPalletWidthUnit.setFixedSize(self.inputArea/2,40)
        self.lblPalletWidthUnit.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletWidthUnit, 2, 2)

        self.lblPalletLenght = QLabel("Box Lenght: ")
        self.lblPalletLenght.setObjectName("Line")
        self.lblPalletLenght.setFixedSize(self.inputArea/2,40)
        self.lblPalletLenght.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletLenght, 3, 0)

        self.txtPalletLenght = QLineEdit("")
        self.txtPalletLenght.setObjectName("Linebtn")
        self.txtPalletLenght.setFixedSize(self.inputArea/2,40)
        self.txtPalletLenght.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.txtPalletLenght, 3, 1)

        self.lblPalletLenghtUnit = QLabel("mm.")
        self.lblPalletLenghtUnit.setObjectName("Line")
        self.lblPalletLenghtUnit.setFixedSize(self.inputArea/2,40)
        self.lblPalletLenghtUnit.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletLenghtUnit, 3, 2)

        self.lblPalletHeight = QLabel("Box Height: ")
        self.lblPalletHeight.setObjectName("Line")
        self.lblPalletHeight.setFixedSize(self.inputArea/2,40)
        self.lblPalletHeight.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletHeight, 4, 0)

        self.txtPalletHeight = QLineEdit("")
        self.txtPalletHeight.setObjectName("Linebtn")
        self.txtPalletHeight.setFixedSize(self.inputArea/2,40)
        self.txtPalletHeight.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.txtPalletHeight, 4, 1)

        self.lblPalletHeightUnit = QLabel("mm.")
        self.lblPalletHeightUnit.setObjectName("Line")
        self.lblPalletHeightUnit.setFixedSize(self.inputArea/2,40)
        self.lblPalletHeightUnit.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletHeightUnit, 4, 2)



        self.lblPalletWeight = QLabel("Weight: ")
        self.lblPalletWeight.setObjectName("Line")
        self.lblPalletWeight.setFixedSize(self.inputArea/2,40)
        self.lblPalletWeight.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletWeight, 5, 0)

        self.txtPalletWeight = QLineEdit("")
        self.txtPalletWeight.setObjectName("Linebtn")
        self.txtPalletWeight.setFixedSize(self.inputArea/2,40)
        self.txtPalletWeight.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.txtPalletWeight, 5, 1)

        self.lblPalletWeightUnit = QLabel("g.")
        self.lblPalletWeightUnit.setObjectName("Line")
        self.lblPalletWeightUnit.setFixedSize(self.inputArea/2,40)
        self.lblPalletWeightUnit.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletWeightUnit, 5, 2)

        self.main_layout.addLayout(self.middle_layout)

        

    def saveDataToJson(self):        
        # Set default path
        #C:\\Users\\USER\\Desktop\\AppVisionTest\\AppVisionTest\\pallet_info\\box
        default_path = "C:\\Users\\USER\\Desktop\\AppVisionTest\\AppVisionTest\\pallet_info\\box"
        if not os.path.exists(default_path):
            os.makedirs(default_path)
        
        # Get the next sequential filename
        default_filename = self.get_next_filename(default_path)
        
        # Combine default path and default filename to create full file path
        full_file_path = os.path.join(default_path, default_filename)

        name_data = default_filename.split('.')[0]

        # Validate and convert pallet width to integer
        pallet_width_text = self.txtPalletWidth.text()
        pallet_width = int(pallet_width_text) if pallet_width_text.isdigit() else 0

        # Validate and convert pallet height to integer
        pallet_height_text = self.txtPalletHeight.text()
        pallet_height = int(pallet_height_text) if pallet_height_text.isdigit() else 0

        # Validate and convert pallet length to integer
        pallet_length_text = self.txtPalletLenght.text()
        pallet_length = int(pallet_length_text) if pallet_length_text.isdigit() else 0

        # Validate and convert weight to integer
        weight_text = self.txtPalletWeight.text()
        weight = int(weight_text) if weight_text.isdigit() else 0

        size_mix = [pallet_width, pallet_length, pallet_height]

        data = {
            "name": name_data,
            "size": size_mix,
            "weight": weight,
            "index": int(default_filename.split('.')[0]) 
        }

        # Serialize data to a formatted JSON string with 4-space indentation
        formatted_data = json.dumps(data, indent=4)

        # Write formatted JSON string to file
        with open(full_file_path, "w") as file:
            file.write(formatted_data)
        
        print(f"Data saved to {full_file_path}")

        # After saving, reset the UI to initial setup
        self.label.setParent(None)
        self.btnSave.setParent(None)
        self.lblPalletName.setParent(None)
        self.txtPalletName.setParent(None)
        self.lblPalletWidth.setParent(None)
        self.txtPalletWidth.setParent(None)
        self.lblPalletWidthUnit.setParent(None)
        self.lblPalletHeight.setParent(None)
        self.txtPalletHeight.setParent(None)
        self.lblPalletHeightUnit.setParent(None)
        self.lblPalletLenght.setParent(None)
        self.txtPalletLenght.setParent(None)
        self.lblPalletLenghtUnit.setParent(None)
        self.lblPalletWeight.setParent(None)
        self.txtPalletWeight.setParent(None)
        self.lblPalletWeightUnit.setParent(None)

        self.showAllJSON()
 
    def loadSelectedJsonFileFromList(self, file_name, previous_item):

        self.tableView.setParent(None)
        self.create_button.setParent(None)
        self.edit_button.setParent(None)
        self.delete_button.setParent(None)

        # Set default path
        default_path = "C:\\Users\\USER\\Desktop\\AppVisionTest\\AppVisionTest\\pallet_info\\box"
        
        # Load the selected JSON file
        with open(os.path.join(default_path, file_name), 'r') as file:
            data = json.load(file)
        
        self.next_number = self.get_next_filename("C:\\Users\\USER\\Desktop\\AppVisionTest\\AppVisionTest\\pallet_info\\box")

        self.btnSaveEdit = QPushButton("Save Edit")
        self.btnSaveEdit.setObjectName("savebutton")
        # self.btnSave.setFixedHeight(self.inputArea * 0.1)
        self.btnSaveEdit.setFixedSize(self.headerSize,self.headerSize/3)
        self.btnSaveEdit.setStyleSheet(
            "font-size: " + str(30 if self.winfo_screenwidth > 1366 else 20) + "px"
        )
        self.btnSaveEdit.clicked.connect(lambda: self.saveEditedJson(file_name))
        # self.h_topbar.addWidget(self.btnViewAll)

        self.top_layout.addWidget(self.btnSaveEdit)

        # Main content
        self.label = QLabel("Hello World")

        # Text label
        self.camHeight = int(self.winfo_screenheight * 0.7)
        self.camWidth = int(self.camHeight / 0.8366)
        self.label.setFixedSize(self.camWidth, self.camHeight)
        self.label.setStyleSheet("background-color: grey; font-size: " + str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        palette = self.label.palette()
        palette.setColor(self.label.foregroundRole(), QtGui.QColor(255,255,255))
        self.label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.label.setPalette(palette)
        
        
        # Add image
        qim = ImageQt(Img.open("resource/pallet3d.png").resize((self.camWidth,self.camHeight)))
        self.label.setPixmap(QPixmap.fromImage(qim))
        self.middle_layout.addWidget(self.label,0,0,Qt.AlignCenter|Qt.AlignRight)
        
        #self.middle_layout.setContentsMargins(0,0,0,0)

        # Input width, height, lenght, Weight 
        # Before self.inputArea = self.winfo_screenwidth * 0.4
        self.inputArea = self.winfo_screenwidth * 0.3
        self.load_grid_layout = QGridLayout()
        self.middle_layout.addLayout(self.load_grid_layout,0,1,Qt.AlignCenter|Qt.AlignVCenter)
        self.lblPalletName = QLabel("Box Name: ")
        self.lblPalletName.setObjectName("Line")
        self.lblPalletName.setFixedSize(self.inputArea/2,40)
        self.lblPalletName.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletName, 1, 0)

        self.txtPalletName = QLabel()
        self.txtPalletName.setObjectName("Linebtn")
        self.txtPalletName.setText("Box" + str(data['name']))  # Corrected to use self.next_number
        self.txtPalletName.setFixedSize(self.inputArea/2, 40)
        self.txtPalletName.setStyleSheet("font-size: " + str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.txtPalletName, 1, 1)

        self.lblPalletWidth = QLabel("Box Width: ")
        self.lblPalletWidth.setObjectName("Line")
        self.lblPalletWidth.setFixedSize(self.inputArea/2,40)
        self.lblPalletWidth.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletWidth, 2, 0)

        self.editPalletWidth = QLineEdit(str(data["size"][0]))
        self.editPalletWidth.setObjectName("Linebtn")
        self.editPalletWidth.setFixedSize(self.inputArea/2,40)
        self.editPalletWidth.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.editPalletWidth, 2, 1)

        self.lblPalletWidthUnit = QLabel("mm.")
        self.lblPalletWidthUnit.setObjectName("Line")
        self.lblPalletWidthUnit.setFixedSize(self.inputArea/2,40)
        self.lblPalletWidthUnit.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletWidthUnit, 2, 2)

        self.lblPalletLenght = QLabel("Box Lenght: ")
        self.lblPalletLenght.setObjectName("Line")
        self.lblPalletLenght.setFixedSize(self.inputArea/2,40)
        self.lblPalletLenght.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletLenght, 3, 0)

        self.editPalletLenght = QLineEdit(str(data["size"][1]))
        self.editPalletLenght.setObjectName("Linebtn")
        self.editPalletLenght.setFixedSize(self.inputArea/2,40)
        self.editPalletLenght.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.editPalletLenght, 3, 1)

        self.lblPalletLenghtUnit = QLabel("mm.")
        self.lblPalletLenghtUnit.setObjectName("Line")
        self.lblPalletLenghtUnit.setFixedSize(self.inputArea/2,40)
        self.lblPalletLenghtUnit.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletLenghtUnit, 3, 2)

        self.lblPalletHeight = QLabel("Box Height: ")
        self.lblPalletHeight.setObjectName("Line")
        self.lblPalletHeight.setFixedSize(self.inputArea/2,40)
        self.lblPalletHeight.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletHeight, 4, 0)

        self.editPalletHeight = QLineEdit(str(data["size"][2]))
        self.editPalletHeight.setObjectName("Linebtn")
        self.editPalletHeight.setFixedSize(self.inputArea/2,40)
        self.editPalletHeight.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.editPalletHeight, 4, 1)

        self.lblPalletHeightUnit = QLabel("mm.")
        self.lblPalletHeightUnit.setObjectName("Line")
        self.lblPalletHeightUnit.setFixedSize(self.inputArea/2,40)
        self.lblPalletHeightUnit.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletHeightUnit, 4, 2)

        self.lblPalletWeight = QLabel("Weight: ")
        self.lblPalletWeight.setObjectName("Line")
        self.lblPalletWeight.setFixedSize(self.inputArea/2,40)
        self.lblPalletWeight.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletWeight, 5, 0)

        self.editPalletWeight = QLineEdit(str(data['weight']))
        self.editPalletWeight.setObjectName("Linebtn")
        self.editPalletWeight.setFixedSize(self.inputArea/2,40)
        self.editPalletWeight.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.editPalletWeight, 5, 1)

        self.lblPalletWeightUnit = QLabel("g.")
        self.lblPalletWeightUnit.setObjectName("Line")
        self.lblPalletWeightUnit.setFixedSize(self.inputArea/2,40)
        self.lblPalletWeightUnit.setStyleSheet("front-size: "+ str(30 if self.winfo_screenwidth > 1366 else 20) + "px")
        self.load_grid_layout.addWidget(self.lblPalletWeightUnit, 5, 2)

        self.main_layout.addLayout(self.middle_layout)


    def saveEditedJson(self, file_name):
        # Set default path
        default_path = "C:\\Users\\USER\\Desktop\\AppVisionTest\\AppVisionTest\\pallet_info\\box"
        
        # Load the selected JSON file
        with open(os.path.join(default_path, file_name), 'r') as file:
            data = json.load(file)

        pallet_width_edit = self.editPalletWidth.text()
        pallet_width_edit = int(pallet_width_edit) if pallet_width_edit.isdigit() else 0

        pallet_Lenght_edit = self.editPalletLenght.text()
        pallet_Lenght_edit = int(pallet_Lenght_edit) if pallet_Lenght_edit.isdigit() else 0

        pallet_Height_edit = self.editPalletHeight.text()
        pallet_Height_edit = int(pallet_Height_edit) if pallet_Height_edit.isdigit() else 0

        weight_edit = self.editPalletWeight.text()
        weight_edit = int(weight_edit) if weight_edit.isdigit() else 0

        size_mix_edit = [pallet_width_edit , pallet_Lenght_edit , pallet_Height_edit]

        
        # Update the data with edited values
        data['size'] = size_mix_edit
        data['weight'] = weight_edit
        
        
        # Save the updated data back to the JSON file
        with open(os.path.join(default_path, file_name), 'w') as file:
            json.dump(data, file, indent=4)
        
        print(f"Data saved to {file_name}")

        # After saving, reset the UI to initial setup
        self.label.setParent(None)
        self.btnSaveEdit.setParent(None)
        self.lblPalletName.setParent(None)
        self.txtPalletName.setParent(None)
        self.lblPalletWidth.setParent(None)
        self.editPalletWidth.setParent(None)
        self.lblPalletWidthUnit.setParent(None)
        self.lblPalletHeight.setParent(None)
        self.editPalletHeight.setParent(None)
        self.lblPalletHeightUnit.setParent(None)
        self.lblPalletLenght.setParent(None)
        self.editPalletLenght.setParent(None)
        self.lblPalletLenghtUnit.setParent(None)
        self.lblPalletWeight.setParent(None)
        self.editPalletWeight.setParent(None)
        self.lblPalletWeightUnit.setParent(None)

        self.showAllJSON()

        # Switch back to the main page after saving
        #self.stacked_widget.setCurrentWidget(self.main_page)

    # ... (your other methods)
