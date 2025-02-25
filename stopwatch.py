from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtCore import QTimer, Qt
from datetime import timedelta
from PyQt6.QtGui import QIcon
import sys


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Focusing")
        self.setFixedSize(110, 60)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Set icon
        self.setWindowIcon(QIcon('сlock.ico'))

        # Mani layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(1)

        self.time = timedelta()
        self.running = False
        self.always_on_top = False

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.setInterval(100)

        # Time
        self.time_label = QLabel("00:00:00")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 16px;
            font-family: 'Segoe UI';
            color: white;
            padding: 0px;
        """)
        layout.addWidget(self.time_label)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(1)

        button_style = """
            QPushButton {
                background-color: #2b2b2b;
                border: none;
                color: white;
                padding: 0px;
                min-width: 20px;
                min-height: 20px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #3b3b3b;
            }
        """

        # Symbols for buttons
        # ▶ ⏸ ⭘ 📌 ⏵ ⏯ ⏹ 📍 ► ❚❚ ■ 🔝 ❯ ‖ □ 💠 ➤ ⫾ ⊡ 🖈

        # Start/Pause button
        self.start_button = QPushButton("▶")
        self.start_button.clicked.connect(self.start_stop)
        self.start_button.setStyleSheet(button_style)
        button_layout.addWidget(self.start_button)

        # Reset button
        self.reset_button = QPushButton("■")
        self.reset_button.clicked.connect(self.reset)
        self.reset_button.setStyleSheet(button_style)
        button_layout.addWidget(self.reset_button)

        # Pin button
        self.pin_button = QPushButton("💠")
        self.pin_button.clicked.connect(self.toggle_always_on_top)
        self.pin_button.setStyleSheet(button_style)
        button_layout.addWidget(self.pin_button)

        layout.addLayout(button_layout)

        self.old_pos = None
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
            }
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = None

    def start_stop(self):
        if self.running:
            self.timer.stop()
            self.running = False
            self.start_button.setText("▶")
        else:
            self.timer.start()
            self.running = True
            self.start_button.setText("⏸")

    def reset(self):
        self.timer.stop()
        self.running = False
        self.time = timedelta()
        self.time_label.setText("00:00:00")
        self.start_button.setText("▶")

    def toggle_always_on_top(self):
        self.always_on_top = not self.always_on_top
        if self.always_on_top:
            self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
            self.pin_button.setStyleSheet("""
                QPushButton {
                    background-color: #404040;
                    border: none;
                    color: white;
                    padding: 0px;
                    min-width: 20px;
                    min-height: 20px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #4a4a4a;
                }
            """)
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowStaysOnTopHint)
            self.pin_button.setStyleSheet("""
                QPushButton {
                    background-color: #2b2b2b;
                    border: none;
                    color: white;
                    padding: 0px;
                    min-width: 20px;
                    min-height: 20px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #3b3b3b;
                }
            """)
        self.show()

    def update_time(self):
        self.time += timedelta(milliseconds=100)
        time_str = str(self.time).split('.')[0]
        if len(time_str.split(':')[0]) == 1:
            time_str = '0' + time_str
        self.time_label.setText(time_str)


def main():
    app = QApplication(sys.argv)
    window = Stopwatch()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()