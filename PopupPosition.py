from PySide6.QtWidgets import (
    QApplication, QDialog, QPushButton, QLineEdit, QLabel,
    QVBoxLayout, QHBoxLayout, QGridLayout, QDialogButtonBox
)
from PySide6.QtCore import Qt

class PositionDialog(QDialog):
    def __init__(self, position_number=None, parent=None):
        super().__init__(parent)
        self.position_number = position_number or 1
        self.setWindowTitle(f'Position {self.position_number}')
        self.initUI()
        self.setLayout(self.layout)

    def initUI(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #7F7F7F;
            }
            QPushButton {
                background-color: #BE0E13;
                color: white;
                border-radius: 5px;
                padding: 5px 15px;
                margin: 5px;
                font-size: 16px;
            }
           
            QPushButton#okCancelBtn {
                background-color: #BE0E13;
                min-width: 80px;
            }
            QLineEdit {
                background-color: white;
                border-radius: 5px;
                padding: 5px;
                margin: 5px;
                min-width: 50px;
            }
            QLabel {
                color: white;
                margin: 5px;
            }
        """)

        self.layout = QVBoxLayout()
        tblTitlebar = QLabel(f"Position {self.position_number}")
        tblTitlebar.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(tblTitlebar)
        grid_layout = QGridLayout()
        labels = ['X:', 'Y:', 'Z:', 'Rx:', 'Ry:', 'Rz:']
        self.line_edits = {}
        for i, text in enumerate(labels):
            label = QLabel(text)
            line_edit = QLineEdit()
            line_edit.setFixedWidth(60)
            # line_edit.setText(str(i))
            self.line_edits[text.rstrip(':')] = line_edit
            grid_layout.addWidget(label, i // 3, 2 * (i % 3), alignment=Qt.AlignRight)
            grid_layout.addWidget(line_edit, i // 3, 2 * (i % 3) + 1)
        
        self.layout.addLayout(grid_layout)

        self.getCurrentPosButton = QPushButton('Get current position')
        self.getCurrentPosButton.clicked.connect(self.getCurrentPosition)
        self.moveToPosButton = QPushButton('Move to this position')
        self.moveToPosButton.clicked.connect(self.moveToPosition)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.getCurrentPosButton)
        button_layout.addWidget(self.moveToPosButton)
        
        self.layout.addLayout(button_layout)

        okCancelBtn = QDialogButtonBox()
        okBtn = okCancelBtn.addButton('OK', QDialogButtonBox.AcceptRole)
        cancelBtn = okCancelBtn.addButton('Cancel', QDialogButtonBox.RejectRole)
        okBtn.setObjectName('okCancelBtn')
        
        cancelBtn.setObjectName('okCancelBtn')
        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.reject)

         # Create a horizontal layout for the buttons
        okCancelLayout = QHBoxLayout()
        okCancelLayout.addStretch(1)  # Add stretchable space before the buttons
        okCancelLayout.addWidget(okBtn)  # Add the OK button
        okCancelLayout.addWidget(cancelBtn)  # Add the Cancel button
        okCancelLayout.addStretch(1)  # Add stretchable space after the buttons

    # Add the button layout to the main dialog layout
        self.layout.addLayout(okCancelLayout)

    # Set the main layout as the dialog's layout
        self.setLayout(self.layout)

    def getCurrentPosition(self):
        # You would fetch the current position here
        # For now, let's just fill the line edits with some dummy data
        for key in self.line_edits:
            self.line_edits[key].setText("0.0")

    def moveToPosition(self):
        # You would move to the specified position here
        # For now, we'll just print the desired position
        position = {key: edit.text() for key, edit in self.line_edits.items()}
        print("Moving to position:", position)

    def getValues(self):
        # Gather the values from the line edits to return them
        return {key: edit.text() for key, edit in self.line_edits.items()}

# Example usage
if __name__ == "__main__":
    app = QApplication([])

    dialog = PositionDialog(1)
    if dialog.exec():
        values = dialog.getValues()
        print(values)
