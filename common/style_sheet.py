from enum import Enum

from qfluentwidgets import StyleSheetBase, Theme


class StyleSheet(StyleSheetBase, Enum):
    """
    样式表
    """

    BASE_INTERFACE = "base_interface"

    def path(self, theme=Theme.AUTO):
        print(self.value)
        return f":/tool_res/qss/light/{self.value}.qss"
