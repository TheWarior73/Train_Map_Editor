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
    QMainWindow, QApplication, QDialog
)
from PyQt6.QtGui import QAction, QKeySequence
# Custom imports
from src.nfr_utils import *
from Network import Network
from Node import Node

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
        self.showMaximized()

        ## Menu building

        # FILE MENU BAR
        new_project_button = self.createMenuButton("New Project", "Create a blanck Project", "Ctrl+Alt+N", self.newProject)

        open_project_button = self.createMenuButton('Open Project', "Select a project to open", "Ctrl+o", self.openProject)

        save_project_button = self.createMenuButton("Save Project", "Save your project and go touch some grass", 'Ctrl+S', self.saveProject)

        settings_button = self.createMenuButton('Settings', "Acces the software settings to customize it.", 'Ctrl+,', self.openSettings)

        # EDIT MENU BAR

        # VIEW MENU BAR

        # HELP MENU BAR
        help_button = self.createMenuButton('Get Help', "Go check the online tutorials on how to use the Map Editor !", 'F1', help_redirect)

        ## Top menu bar
        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addActions([new_project_button, open_project_button, save_project_button])
        file_menu.addSeparator()
        file_menu.addAction(settings_button)

        edit_menu = menu.addMenu("&Edit") # Not yet implemented #TODO

        view_menu = menu.addMenu("&View") # Not yet implemented #TODO

        help_menu = menu.addMenu("&Help")
        help_menu.addAction(help_button)

    def newProject(self):
        np_alert = CustomDialog(self, 'Create New Project ?', 'Creating a new project will erase data from current project if not saved.\nDo you wish to continue ?')
        if np_alert.exec() :
            print('Creating new project')
        else: print('Project Creation Canceled')

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


    def createMenuButton(self, name='', desc='', shortcut: str =None, conn_func=None) :
        """returns a menu button with the information given in parameter"""
        button = QAction(name, self)
        button.setStatusTip(desc)
        button.triggered.connect(conn_func)
        if shortcut is not None :
            button.setShortcut(QKeySequence(shortcut))
        return button

def help_redirect():
    import webbrowser
    webbrowser.open('https://github.com/TheWarior73/Train_Map_Editor')
    print('Redirected towards github repo')

def main():

    # Test data for saving purposes until I link the Network.py file with the app.py file.
    data = {'nodes': {'NFRC': [{'posX': None, 'posY': None, 'color': []}], 'SEP': [{'posX': None, 'posY': None, 'color': []}], 'MP': [{'posX': None, 'posY': None, 'color': []}], 'NH': [{'posX': None, 'posY': None, 'color': []}], 'RH': [{'posX': None, 'posY': None, 'color': []}], 'RC': [{'posX': None, 'posY': None, 'color': []}], 'RF': [{'posX': None, 'posY': None, 'color': []}], 'FC': [{'posX': None, 'posY': None, 'color': []}], 'S': [{'posX': None, 'posY': None, 'color': []}], 'SC': [{'posX': None, 'posY': None, 'color': []}]}}

    app = QApplication(sys.argv)

    with open("styles.css", 'r') as file :
        app.setStyleSheet(file.read())

    ex = MainWindow(data=data)
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()