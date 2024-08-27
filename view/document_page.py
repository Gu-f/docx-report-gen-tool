from PySide6.QtWidgets import QLabel
from qfluentwidgets import TitleLabel

from widgets.base_doc_widget import SubDocWidget
from widgets.command_bar import DocPageFuncCommandBar, DocPageBottomCommandBar
from view.interface.base_interface import BaseInterface


class DocumentPageInterface(BaseInterface):
    def __init__(self, text: str, parent=None):
        super().__init__(
            title="文档处理",
            subtitle='{{这是文档名占位符}}',
            parent=parent
        )
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName(text.replace(' ', '-'))

        label_command_menu = DocPageBottomCommandBar(parent=self)
        label = QLabel('鼠标右键点击此处新增组件', label_command_menu)
        label_command_menu.add_widget(label)
        self.doc_page_add_widget(label_command_menu, bottom=True)

    def doc_page_add_widget(self, widget, bottom=False):
        if bottom:
            self.vBoxLayout.addWidget(widget)
        else:
            if self.vBoxLayout.count() == 1:
                position = 0
            else:
                position = self.vBoxLayout.count() - 1
            self.vBoxLayout.insertWidget(position, widget)

    def __add_sub_widget(self, widget):
        func_command_menu = DocPageFuncCommandBar(parent=self)
        # widget没有指定父节点func_command_menu
        func_command_menu.add_widget(widget)
        self.doc_page_add_widget(func_command_menu, bottom=False)

    def add_sub_doc_widget(self, doc_widget_category):
        if doc_widget_category == 'InputWidget':
            widget = TitleLabel(text="标题")
            self.__add_sub_widget(SubDocWidget(widget))

    def delete_sub_doc_widget(self, sub_doc_widget):
        self.vBoxLayout.removeWidget(sub_doc_widget)  # 从布局中移除
        sub_doc_widget.deleteLater()  # 销毁对象
