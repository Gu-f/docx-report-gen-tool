from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame

from qfluentwidgets import LineEdit


class SubDocWidget(QWidget):

    def __init__(self, widget: QWidget, stretch=0, parent=None):
        super().__init__(parent=parent)
        if widget is not None:
            self.widget = widget
        self.stretch = stretch

        self.content_area = QFrame(self)

        self.contentWidget = QFrame(self.content_area)
        self.input_text = LineEdit()

        self.vBoxLayout = QVBoxLayout(self)
        self.cardLayout = QVBoxLayout(self.content_area)
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QHBoxLayout(self.contentWidget)

        self.__initWidget()

    def __initWidget(self):
        self.__initLayout()

        self.content_area.setObjectName('content_area')
        self.contentWidget.setObjectName('contentWidget')

    def __initLayout(self):
        self.vBoxLayout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinimumSize)
        self.cardLayout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinimumSize)
        self.topLayout.setSizeConstraint(QHBoxLayout.SizeConstraint.SetMinimumSize)

        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.setContentsMargins(12, 12, 12, 12)
        self.bottomLayout.setContentsMargins(18, 18, 18, 18)
        self.cardLayout.setContentsMargins(0, 0, 0, 0)

        self.vBoxLayout.addWidget(self.content_area, 0, Qt.AlignmentFlag.AlignTop)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.cardLayout.setSpacing(0)
        self.cardLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.cardLayout.addLayout(self.topLayout, 0)
        self.cardLayout.addWidget(self.contentWidget, 0, Qt.AlignmentFlag.AlignBottom)

        self.widget.setParent(self.content_area)
        self.topLayout.addWidget(self.widget)
        if self.stretch == 0:
            self.topLayout.addStretch(1)

        self.widget.show()

        self.bottomLayout.addWidget(self.input_text, 0, Qt.AlignmentFlag.AlignLeft)
        self.bottomLayout.addStretch(1)
        self.bottomLayout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
