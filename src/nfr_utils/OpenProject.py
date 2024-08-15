"""Opens a .json file that contains usefull information for the app

---

MIT License

Copyright (c) 2024 Th3_Warior & contributors

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. Please refer to the LICENCE file
"""

## IMPORTS ##
import json

# - PYQT6 - #
from PyQt6.QtWidgets import (QFileDialog)
from pathlib import Path

## IMPORTS ##

class OpenProject(QFileDialog):
    def __init__(self, parent=None):
        super().__init__(parent)


    def openpr(self):
        directory = str(Path.home())
        file_name = QFileDialog.getOpenFileName(self, 'Open Project', directory, filter='*.json')

        if file_name[0] :
            with open(file_name[0], 'r') as file_handler:
                data = file_handler.read()
                file_reader = json.loads(data)
            return file_reader
