"""Creates a custom Dialog Alert

---

MIT License

Copyright (c) 2024 Th3_Warior & contributors

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. Please refer to the LICENCE file
"""
from PyQt6.QtWidgets import (
    QDialog, QDialogButtonBox,
    QVBoxLayout, QLabel
)


class CustomDialog(QDialog):
    def __init__(self, parent=None, window_title='', message=''):
        super().__init__(parent)

        self.setWindowTitle(window_title)

        btn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(btn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(message)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)