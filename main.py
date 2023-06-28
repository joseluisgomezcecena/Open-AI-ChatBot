import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLineEdit
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chatbot")
        self.setMinimumSize(700, 500)

        # Add chat area widget.
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(50, 50, 600, 300)
        self.chat_area.setReadOnly(True)

        # Add input field widget.
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(50, 380, 600, 50)

        # Add send button widget.
        self.button = QPushButton("Send Message", self)
        self.button.setGeometry(50, 450, 600, 30)
        #set button color
        self.button.setStyleSheet("background-color: #027de8;color: #ffffff;")


        self.show()

class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())