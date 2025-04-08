from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QPushButton
from PyQt5.QtCore import Qt, QSize


class CustomItemWidget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.font_size = 16
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setAlignment(Qt.AlignVCenter)
        self.setLayout(self.main_layout)

        self.frame = QFrame()
        self.frame.setMinimumSize(QSize(100, 40))
        self.main_layout.addWidget(self.frame)

        self.h_layout = QHBoxLayout()
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setAlignment(Qt.AlignVCenter)
        self.h_layout.setSpacing(0)
        self.frame.setLayout(self.h_layout)

        self.label = QLabel(text)
        self.label.setObjectName("CustomItemLabel")

        self.button = QPushButton("删除")
        self.button.setMinimumHeight(25)
        self.button.setObjectName("CustomItemButton")
        self.button.setCursor(Qt.PointingHandCursor)

        self.h_layout.addWidget(self.label, 6, alignment=Qt.AlignVCenter)
        self.h_layout.addWidget(self.button, 1, alignment=Qt.AlignVCenter)

        self.setup_style()

    def get_size(self) -> QSize:
        return self.frame.minimumSize()

    def setup_style(self):
        self.setStyleSheet(f"""
            #CustomItemLabel {{
                font-size: {self.font_size}px;
                color: black;
                background-color: transparent;
                font-weight: normal;
            }}
            #CustomItemButton {{
                background-color: red;
                color: white;
                border-radius: 4px;
                font-size: {int(self.font_size)}px;
                font-weight: normal;
            }}
            #CustomItemButton:hover {{
                background-color: rgb(198, 122, 211);
            }}
            #CustomItemButton:pressed {{
                background-color: rgb(206, 200, 229);
            }}
        """)
