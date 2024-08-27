from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from qfluentwidgets import ScrollArea, TitleLabel, CaptionLabel, BodyLabel, ComboBox
from common.style_sheet import StyleSheet


class TitleToolBar(QWidget):
    """
    标题工具栏
    """

    def __init__(self, title, subtitle, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = TitleLabel(title, self)
        self.subtitleLabel = CaptionLabel(subtitle, self)

        self.doc_template_label = BodyLabel(text="使用文档模板:", parent=self)

        self.comboBox = ComboBox()
        self.comboBox.addItems(['无', '模板1', '模板2'])
        self.comboBox.setCurrentIndex(0)
        self.comboBox.setMinimumWidth(210)
        self.comboBox.currentIndexChanged.connect(self.choice_combobox_action)

        self.vBoxLayout = QVBoxLayout(self)
        self.buttonLayout = QHBoxLayout()

        self.__initWidget()

    def __initWidget(self):
        self.setFixedHeight(138)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(36, 22, 36, 12)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.addWidget(self.subtitleLabel)
        self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.addLayout(self.buttonLayout, 1)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.buttonLayout.setSpacing(4)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.addWidget(self.doc_template_label, 0, Qt.AlignmentFlag.AlignLeft)
        self.buttonLayout.addWidget(self.comboBox, 0, Qt.AlignmentFlag.AlignLeft)
        self.buttonLayout.addStretch(1)
        # self.buttonLayout.addWidget(self.separator, 0, Qt.AlignRight)
        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

        self.subtitleLabel.setTextColor(QColor(96, 96, 96), QColor(216, 216, 216))

    def choice_combobox_action(self, index):
        print(f"combobox action {index}")


class BaseInterface(ScrollArea):
    def __init__(self, title: str, subtitle: str, parent=None):
        """
        基础页面接口
        :param title: 页面标题
        :param subtitle: 页面子标题
        :param parent:
        """
        super().__init__(parent=parent)
        self.view = QWidget(self)
        self.toolBar = TitleToolBar(title, subtitle, self)
        self.vBoxLayout = QVBoxLayout(self.view)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setViewportMargins(0, self.toolBar.height(), 0, 0)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setSpacing(0)  # vBoxLayout组件间距
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.vBoxLayout.setContentsMargins(25, 0, 25, 0)  # 左上右下

        self.view.setObjectName('view')
        StyleSheet.BASE_INTERFACE.apply(self)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.toolBar.resize(self.width(), self.toolBar.height())
