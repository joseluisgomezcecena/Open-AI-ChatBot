import sys
from backend import Chatbot
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLineEdit
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        chatbot = Chatbot()  # Create Chat-bot instance.
        self.setWindowTitle("Chatbot")
        self.setMinimumSize(700, 500)

        # Add chat area widget.
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(50, 50, 600, 300)
        self.chat_area.setReadOnly(True)

        # Add input field widget.
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(50, 380, 600, 50)
        self.input_field.returnPressed.connect(self.send_message)

        # Add send button widget.
        self.button = QPushButton("Send Message", self)
        self.button.setGeometry(50, 450, 600, 30)
        # set button color
        self.button.setStyleSheet("background-color: #027de8;color: #ffffff;")
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p>Me: {user_input}</p>")
        self.input_field.clear()

        # Create a thread to get response from the chatbot.
        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p>Open AI: {response}</p>")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
