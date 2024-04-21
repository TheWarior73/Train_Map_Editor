"""

---

MIT License

Copyright (c) 2024 Th3_Warior

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. Please refer to the LICENCE file
"""
## IMPORTS ##
import sys
# PYQT6
from PyQt6.QtWidgets import (
    QMainWindow, QApplication
)
from PyQt6.QtGui import QAction, QKeySequence
# Custom imports
from src.nfr_utils import *


## IMPORTS ##

class MainWindow(QMainWindow):

    def __init__(self, data):
        super(MainWindow, self).__init__()

        self.initUI()
        self.data = data


    def initUI(self):
        # general window parameters
        self.setWindowTitle("Train Map editor")

        # Min/Max Window Size
        self.setMinimumSize(1000, int(1000/1.7))
        self.setMaximumSize(1500, int(1500/1.7))

        ## Menu building

        # FILE MENU BAR
        open_project_button = QAction('Open Project', self)
        open_project_button.setStatusTip("Select a project to open")
        open_project_button.triggered.connect(self.openProject)

        save_project_button = QAction("Save Project", self)
        save_project_button.setStatusTip('Save your project and go touch some grass')
        save_project_button.triggered.connect(self.saveProject)
        save_project_button.setShortcut(QKeySequence('Ctrl+s'))

        settings_button = QAction("Settings", self)
        settings_button.setStatusTip("Acces the software settings to customize it.")
        settings_button.triggered.connect(self.openSettings)
        settings_button.setShortcut(QKeySequence('Ctrl+,'))

        # EDIT MENU BAR

        # VIEW MENU BAR

        # HELP MENU BAR
        help_button = QAction("Get Help", self)
        help_button.setStatusTip("Go check the online tutorials on how to use the Map Editor !")
        help_button.triggered.connect(help_redirect)
        help_button.setShortcut(QKeySequence("F1"))

        ## Top menu bar
        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addActions([open_project_button, save_project_button])
        file_menu.addSeparator()
        file_menu.addAction(settings_button)

        edit_menu = menu.addMenu("&Edit") # Not yet implemented #TODO

        view_menu = menu.addMenu("&View") # Not yet implemented #TODO

        help_menu = menu.addMenu("&Help")
        help_menu.addAction(help_button)

    def openProject(self):
        opn = OpenProject(self)
        project_data = opn.openpr()
        if project_data is not None :
            print('Project Opened with data :', project_data)
            print(f'Number of nodes on the network: {len(project_data["nodes"])}\n'
                  f'NodeList: ')
            nl = []
            for node in project_data["nodes"] :
                nl.append(node)
            print(nl)

    def saveProject(self):
        sv = SaveProject(parent=self, data=self.data)
        sv.savepr()

    def openSettings(self):
        ## Not yet implemented. #TODO
        print('tring to open settings')




def help_redirect():
    import webbrowser
    webbrowser.open('https://blank.page/')
    print('Redirected towards blank.Page (for now)')

def main():

    data = {'nodes': {'NFRC': [{'posX': None, 'posY': None, 'color': []}], 'SEP': [{'posX': None, 'posY': None, 'color': []}], 'MP': [{'posX': None, 'posY': None, 'color': []}], 'NH': [{'posX': None, 'posY': None, 'color': []}], 'RH': [{'posX': None, 'posY': None, 'color': []}], 'RC': [{'posX': None, 'posY': None, 'color': []}], 'RF': [{'posX': None, 'posY': None, 'color': []}], 'FC': [{'posX': None, 'posY': None, 'color': []}], 'S': [{'posX': None, 'posY': None, 'color': []}], 'SC': [{'posX': None, 'posY': None, 'color': []}]}}

    app = QApplication(sys.argv)
    ex = MainWindow(data=data)
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()