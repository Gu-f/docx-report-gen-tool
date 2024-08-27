from PySide6.QtWidgets import QFrame, QVBoxLayout
from qfluentwidgets import FluentIcon, MenuAnimationType
from qfluentwidgets import RoundMenu, Action


class DocPageCommandBarBase(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setStyleSheet('QLabel{font-size: 20px}')

    def add_widget(self, widget):
        self.layout.addWidget(widget)


class DocPageFuncCommandBar(DocPageCommandBarBase):
    def contextMenuEvent(self, event):
        main_menu = RoundMenu(parent=self.parent)

        delete_action = Action(FluentIcon.DELETE, '删除该组件')
        delete_action.triggered.connect(lambda: self.menu_action_delete(self.parent))
        main_menu.addAction(delete_action)

        main_menu.exec(event.globalPos(), aniType=MenuAnimationType.DROP_DOWN)

    def menu_action_delete(self, parent):
        parent.delete_sub_doc_widget(self)


class DocPageBottomCommandBar(DocPageCommandBarBase):
    def contextMenuEvent(self, e):
        main_menu = RoundMenu(parent=self.parent)

        # 子菜单
        sub_menu = RoundMenu(title="新增", parent=self.parent)

        # 动作
        input_widget_action = Action(FluentIcon.ADD, '输入框')
        input_widget_action.triggered.connect(lambda: self.menu_action_add_input(parent=self.parent))
        sub_menu.addAction(input_widget_action)

        main_menu.addMenu(sub_menu)

        # 展示主菜单
        main_menu.exec(e.globalPos(), aniType=MenuAnimationType.DROP_DOWN)

    def menu_action_add_input(self, parent=None):
        parent.add_sub_doc_widget("InputWidget")
