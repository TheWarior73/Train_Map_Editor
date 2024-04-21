"""Saves the project data to a .json file containing all the usefull information of the map (networks, nodes etc.)

---

MIT License

Copyright (c) 2024 Th3_Warior

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. Please refer to the LICENCE file
"""

from PyQt6.QtWidgets import (QFileDialog)
from pathlib import Path
import json

class SaveProject(QFileDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.data_list = data


    def savepr(self):
        directory = str(Path.home())
        file_name = QFileDialog.getSaveFileName(self, 'Open Project', directory, filter='*.json')

        if file_name[0] :
            with open(file_name[0], 'w') as json_file_handler:
                json_file_handler.write(json.dumps(self.data_list, indent=2))
