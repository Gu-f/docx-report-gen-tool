import uuid

from PySide6.QtCore import QSize, QEventLoop, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import NavigationItemPosition, FluentWindow, SplashScreen
from qfluentwidgets import FluentIcon

from common.signal_bus import signalBus
from view.document_page import DocumentPageInterface
from view.home_page import HomePageInterface
from view.interface.base_interface import BaseInterface
from common import resource  # 引入资源
from view.settings_page import SettingsPageInterface

_ = resource


class MainWindow(FluentWindow):
    """ 主界面 """

    def __init__(self):
        super().__init__()
        self.init_window()

        # 创建界面接口
        self.homeInterface = HomePageInterface('主页界面', self)
        self.documentInterface = DocumentPageInterface('文档界面', self)

        self.settingInterface = SettingsPageInterface('设置界面', self)

        # 开启亚克力效果
        self.navigationInterface.setAcrylicEnabled(True)

        self.connect_signal_to_slot()

        # =====模拟事件循环显示开屏=====
        loop = QEventLoop(self)
        QTimer.singleShot(1000, loop.quit)
        loop.exec()
        # ===========================

        self.init_navigation()
        # 4. 隐藏启动页面
        self.splashScreen.finish()

    def connect_signal_to_slot(self):
        # todo 信号槽
        pass

    def init_navigation(self):
        self.addSubInterface(self.homeInterface, FluentIcon.HOME, '主页', NavigationItemPosition.TOP)
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.documentInterface, FluentIcon.DOCUMENT, '空白文档', NavigationItemPosition.SCROLL)

        self.navigationInterface.addItem(
            routeKey='add_document',
            icon=FluentIcon.ADD_TO,
            text="新增编辑框",
            onClick=self.on_add_document,
            selectable=False,
            tooltip="新增编辑框",
            position=NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(self.settingInterface, FluentIcon.SETTING, '设置', NavigationItemPosition.BOTTOM)

    def on_add_document(self):
        uid = uuid.uuid4().hex
        self.documentInterface = DocumentPageInterface(f'文档界面{uid}', self)
        self.addSubInterface(self.documentInterface, FluentIcon.DOCUMENT, '空白文档', NavigationItemPosition.SCROLL)
        # self.navigationInterface.addItem(
        #     routeKey=uid,
        #     icon=FIF.DOCUMENT,
        #     text=f"新增{uid}",
        #     onClick=self.on_add_document,
        #     selectable=False,
        #     tooltip=f"新增{uid}",
        #     position=NavigationItemPosition.SCROLL
        # )

    def init_window(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon(r'./resource/images/logo.png'))
        self.setWindowTitle('Docx报告生成器')

        # 1. 创建启动页面
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(200, 200))

        self.splashScreen.raise_()

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()

