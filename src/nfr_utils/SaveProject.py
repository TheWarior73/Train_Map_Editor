"""Saves the project data to a .json file containing all the usefull information of the map (networks, nodes etc.)

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

class SaveProject(QFileDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.data_list = data


    def savepr(self):
        directory = str(Path.home())
        file_name = QFileDialog.getSaveFileName(self, 'Save Project', directory, filter='*.json')

        if file_name[0] :
            with open(file_name[0], 'w') as json_file_handler:
                json_file_handler.write(json.dumps(self.data_list, indent=2))
                print(f"Project saved in: {file_name[0]}")
