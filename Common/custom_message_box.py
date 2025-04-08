from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5.QtCore import Qt


class CustomMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("提示")
        self.setIcon(QMessageBox.Question)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.Yes)
        self.set_style()

    def set_style(self):
        self.setStyleSheet("""
            QMessageBox {{
                background-color: white;
            }}
        """)

    def exec(self, title="提示", text="确定吗") -> int:
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(QMessageBox.Question)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.Yes)
        self.setEscapeButton(QMessageBox.No)

        buttons = self.findChildren(QPushButton)  # 获取所有按钮

        for button in buttons:
            # 设置按钮的大小
            button.setMinimumWidth(60)
            button.setMinimumHeight(20)
            button.setCursor(Qt.PointingHandCursor)

            if button.text() == "&Yes":  # Yes按钮
                button.setStyleSheet(f"""
                    QPushButton {{
                        background-color: #2196F3;
                        color: white;
                        font-size: 16px;
                        border-radius: 5px;
                    }}
                    QPushButton:hover {{
                        background-color: rgb(73, 170, 159);
                    }}
                    QPushButton:pressed {{
                        background-color: rgb(234, 208, 112);
                    }}
                """)
            elif button.text() == "&No":  # No按钮
                button.setStyleSheet(f"""
                    QPushButton {{
                        background-color: red;
                        color: white;
                        font-size: 16px;
                        border-radius: 5px;
                    }}
                    QPushButton:hover {{
                        background-color: rgb(198, 122, 211);
                    }}
                    QPushButton:pressed {{
                        background-color: rgb(206, 200, 229);
                    }}
                """)

        return self.exec_()
