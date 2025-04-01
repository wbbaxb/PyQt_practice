import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
                             QLabel, QGroupBox, QFileDialog, QTextBrowser)
from PyQt5.QtCore import Qt, QUrl


class FileDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog综合演示")
        self.resize(800, 600)
        self.move(300, 200)
        self.setup_ui()

    def setup_ui(self):
        # 创建主布局
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # 顶部标题
        title_label = QLabel("QFileDialog 文件对话框演示")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(
            "font-size: 18px; font-weight: bold; margin: 10px;")
        main_layout.addWidget(title_label)

        # 中间部分：左侧为功能按钮区，右侧为结果显示区
        middle_layout = QHBoxLayout()
        main_layout.addLayout(middle_layout)

        # 左侧功能区（占3/8宽度）
        left_layout = QVBoxLayout()
        middle_layout.addLayout(left_layout, 3)

        # 右侧显示区（占5/8宽度）
        self.result_browser = QTextBrowser()
        middle_layout.addWidget(self.result_browser, 5)

        # 创建静态方法分组
        static_group = QGroupBox("静态方法")
        static_layout = QVBoxLayout()
        static_group.setLayout(static_layout)

        # 添加静态方法按钮
        self.btn_get_open_file = QPushButton("打开单个文件(getOpenFileName)")
        self.btn_get_open_file.clicked.connect(self.show_get_open_file)
        static_layout.addWidget(self.btn_get_open_file)

        self.btn_get_open_files = QPushButton("打开多个文件(getOpenFileNames)")
        self.btn_get_open_files.clicked.connect(self.show_get_open_files)
        static_layout.addWidget(self.btn_get_open_files)

        self.btn_get_open_file_url = QPushButton("打开文件URL(getOpenFileUrl)")
        self.btn_get_open_file_url.clicked.connect(self.show_get_open_file_url)
        static_layout.addWidget(self.btn_get_open_file_url)

        self.btn_get_save_file = QPushButton("保存文件(getSaveFileName)")
        self.btn_get_save_file.clicked.connect(self.show_get_save_file)
        static_layout.addWidget(self.btn_get_save_file)

        self.btn_get_existing_dir = QPushButton("选择文件夹(getExistingDirectory)")
        self.btn_get_existing_dir.clicked.connect(self.show_get_existing_dir)
        static_layout.addWidget(self.btn_get_existing_dir)

        self.btn_get_existing_dir_url = QPushButton(
            "选择文件夹URL(getExistingDirectoryUrl)")
        self.btn_get_existing_dir_url.clicked.connect(
            self.show_get_existing_dir_url)
        static_layout.addWidget(self.btn_get_existing_dir_url)

        # 创建实例方法分组
        instance_group = QGroupBox("实例方法与属性")
        instance_layout = QVBoxLayout()
        instance_group.setLayout(instance_layout)

        # 添加实例方法按钮
        self.btn_accept_mode = QPushButton("接收模式(AcceptMode)")
        self.btn_accept_mode.clicked.connect(self.show_accept_mode)
        instance_layout.addWidget(self.btn_accept_mode)

        self.btn_file_mode = QPushButton("文件模式(FileMode)")
        self.btn_file_mode.clicked.connect(self.show_file_mode)
        instance_layout.addWidget(self.btn_file_mode)

        self.btn_name_filter = QPushButton("名称过滤器(NameFilter)")
        self.btn_name_filter.clicked.connect(self.show_name_filter)
        instance_layout.addWidget(self.btn_name_filter)

        self.btn_label_text = QPushButton("标签文本(LabelText)")
        self.btn_label_text.clicked.connect(self.show_label_text)
        instance_layout.addWidget(self.btn_label_text)

        # 创建信号分组
        signal_group = QGroupBox("信号演示")
        signal_layout = QVBoxLayout()
        signal_group.setLayout(signal_layout)

        # 添加信号按钮
        self.btn_file_signals = QPushButton("文件选择信号")
        self.btn_file_signals.clicked.connect(self.show_file_signals)
        signal_layout.addWidget(self.btn_file_signals)

        self.btn_directory_signals = QPushButton("目录信号")
        self.btn_directory_signals.clicked.connect(self.show_directory_signals)
        signal_layout.addWidget(self.btn_directory_signals)

        # 添加分组到左侧布局
        left_layout.addWidget(static_group)
        left_layout.addWidget(instance_group)
        left_layout.addWidget(signal_group)

        # 底部说明
        note_label = QLabel("点击左侧按钮尝试不同的文件对话框功能，结果将显示在右侧区域")
        note_label.setAlignment(Qt.AlignCenter)
        note_label.setStyleSheet("color: gray;")
        main_layout.addWidget(note_label)

    def log_result(self, title, result):
        """在结果区域显示结果"""
        self.result_browser.clear()
        self.result_browser.append(f'{title},{result}')

    # 静态方法演示函数
    def show_get_open_file(self):
        """打开单个文件对话框"""
        result = QFileDialog.getOpenFileName(
            self,  # 父窗口
            "选择一个文件",  # 对话框标题
            "./",  # 默认路径为当前目录
            "所有文件(*);;图片文件(*.png *.jpg);;Python文件(*.py)",  # 过滤器
            "Python文件(*.py)"  # 默认文件名
        )
        self.log_result("打开单个文件 (getOpenFileName)", result)

    def show_get_open_files(self):
        """打开多个文件对话框"""
        result = QFileDialog.getOpenFileNames(
            self,
            "选择多个文件",
            "./",
            "所有文件(*);;图片文件(*.png *.jpg);;Python文件(*.py)"
        )
        self.log_result("打开多个文件 (getOpenFileNames)", result)

    def show_get_open_file_url(self):
        """打开文件URL对话框"""
        result = QFileDialog.getOpenFileUrl(
            self,
            "选择一个文件URL",
            QUrl("./"),
            "所有文件(*);;图片文件(*.png *.jpg);;Python文件(*.py)"
        )
        self.log_result("打开文件URL (getOpenFileUrl)", result)

    def show_get_save_file(self):
        """保存文件对话框"""
        result = QFileDialog.getSaveFileName(
            self,
            "保存文件",
            "./untitled.txt",
            "文本文件(*.txt);;所有文件(*)"
        )
        self.log_result("保存文件 (getSaveFileName)", result)

    def show_get_existing_dir(self):
        """选择已存在的目录对话框"""
        result = QFileDialog.getExistingDirectory(
            self,
            "选择一个文件夹",
            "./"
        )
        self.log_result("选择文件夹 (getExistingDirectory)", result)

    def show_get_existing_dir_url(self):
        """选择已存在的目录URL对话框"""
        result = QFileDialog.getExistingDirectoryUrl(
            self,
            "选择一个文件夹URL",
            QUrl("./")
        )
        self.log_result("选择文件夹URL (getExistingDirectoryUrl)", result)

    # 实例方法演示函数
    def show_accept_mode(self):
        fd = QFileDialog(self, "接收模式演示", "./")
        fd.setNameFilter("所有文件(*);;Python文件(*.py)")

        fd.setAcceptMode(QFileDialog.AcceptSave)

        # 设置默认后缀名
        fd.setDefaultSuffix("txt")

        # 打开对话框
        fd.open()
        fd.fileSelected.connect(
            lambda file: self.log_result("接收模式-保存文件", file))

    def show_file_mode(self):
        """演示文件模式"""
        fd = QFileDialog(self, "文件模式演示", "./")

        # 设置文件模式为多选文件
        fd.setFileMode(QFileDialog.ExistingFiles)
        fd.setNameFilter("所有文件(*);;Python文件(*.py)")

        # 打开对话框
        fd.open()
        fd.filesSelected.connect(
            lambda files: self.log_result("文件模式-多选文件", files))

    def show_name_filter(self):
        """演示名称过滤器"""
        fd = QFileDialog(self, "名称过滤器演示", "./")

        # 设置多个名称过滤器
        fd.setNameFilters([
            "Python文件(*.py)",
            "图片文件(*.png *.jpg *.jpeg)",
            "文本文件(*.txt)",
            "所有文件(*)"
        ])

        # 打开对话框
        fd.open()
        fd.fileSelected.connect(lambda file: self.log_result("名称过滤器", file))
        fd.filterSelected.connect(
            lambda filter: self.log_result("选中的过滤器", filter))

    def show_label_text(self):
        """
        自定义标签文本，包括：
        QFileDialog.FileName 文件名
        QFileDialog.Accept 确定
        QFileDialog.Reject 取消
        QFileDialog.LookIn 查找位置
        QFileDialog.FileType 文件类型
        """
        fd = QFileDialog(self, "标签文本演示", "./")

        # 设置各种标签的文本
        fd.setLabelText(QFileDialog.FileName, "我的文件名")
        fd.setLabelText(QFileDialog.Accept, "确定选择")
        fd.setLabelText(QFileDialog.Reject, "取消选择")
        fd.setLabelText(QFileDialog.LookIn, "查找位置")

        # 如果是保存模式，设置文件类型标签
        fd.setAcceptMode(QFileDialog.AcceptSave)
        fd.setLabelText(QFileDialog.FileType, "文件格式")

        # 打开对话框
        fd.open()
        fd.fileSelected.connect(lambda file: self.log_result("自定义标签文本", file))

    # 信号演示函数
    def show_file_signals(self):
        fd = QFileDialog(self, "文件信号演示", "./")
        fd.setFileMode(QFileDialog.ExistingFiles)

        # 连接文件选择信号
        fd.fileSelected.connect(lambda file: self.log_result("单个文件被选中", file))
        fd.filesSelected.connect(
            lambda files: self.log_result("多个文件被选中", files))
        fd.urlSelected.connect(
            lambda url: self.log_result("单个URL被选中", url.toString()))
        fd.urlsSelected.connect(lambda urls: self.log_result(
            "多个URL被选中", [url.toString() for url in urls]))

        # 打开对话框
        fd.open()

    def show_directory_signals(self):
        fd = QFileDialog(self, "目录信号演示", "./")

        # 连接目录信号
        fd.currentChanged.connect(lambda path: self.log_result("当前路径改变", path))
        fd.currentUrlChanged.connect(
            lambda url: self.log_result("当前URL改变", url.toString()))
        fd.directoryEntered.connect(lambda dir: self.log_result("进入目录", dir))
        fd.directoryUrlEntered.connect(
            lambda url: self.log_result("进入目录URL", url.toString()))

        # 打开对话框
        fd.open()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileDialogDemo()
    window.show()
    sys.exit(app.exec())
