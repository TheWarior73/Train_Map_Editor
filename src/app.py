"""
This file runs the software using a UI

---

MIT License

Copyright (c) 2024 Th3_Warior & contributors

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. Please refer to the LICENCE file
"""
## IMPORTS ##
import sys
import webbrowser

# - PYQT6 - #
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QDialog,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QLabel, QWidget,
)
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtCore import Qt

# - NFR-Lib - #
from nfr_utils import *

## IMPORTS ##

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.project_network = None  # Project
        self.display_layout = None  # Project visualization Layout

        self.save_project_button = None
        self.me_map = QGridLayout() #map layout

        self.initUI() # last to initialize everything (or will be overwritten by the None objects)

    def initUI(self):
        # general window parameters
        self.setWindowTitle("Train Map editor")

        # Min/Max Window Size
        self.setMinimumSize(1000, int(1000/1.7))
        self.showMaximized()

        ## Menu building

        # FILE MENU BAR
        new_project_button = self.createMenuButton("New Project", "Create a blanck Project", "Ctrl+Alt+N", self.newProject)
        new_project_button.setDisabled(True) # Unavailable for now

        open_project_button = self.createMenuButton('Open Project', "Select a project to open", "Ctrl+o", self.openProject)

        self.save_project_button = self.createMenuButton("Save Project", "Save your project and go touch some grass", 'Ctrl+S', self.saveProject)

        settings_button = self.createMenuButton('Settings', "Acces the software settings to customize it.", 'Ctrl+,', self.openSettings)
        settings_button.setDisabled(True)

        # EDIT MENU BAR

        # VIEW MENU BAR

        # HELP MENU BAR
        help_button = self.createMenuButton('Get Help', "Go check the online tutorials on how to use the Map Editor !", 'F1', help_redirect)
        report_issue_button = self.createMenuButton('Issue Tracker', 'Report bugs and check existing ones on the GitHub',conn_func=issue_redirect)

        ## Top menu bar
        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addActions([new_project_button, open_project_button, self.save_project_button])
        file_menu.addSeparator()
        file_menu.addAction(settings_button)

        ## only here because some features are missing, will disapear of be modified in the future
        todo_button = self.createMenuButton("Comming soon", "feature is comming soon !", conn_func=help_redirect) #conn_func is needed, but won't be used since the button is disabled
        todo_button.setDisabled(True)

        edit_menu = menu.addMenu("&Edit") # Not yet implemented #TODO
        edit_menu.addAction(todo_button)

        view_menu = menu.addMenu("&View") # Not yet implemented #TODO
        view_menu.addAction(todo_button)

        help_menu = menu.addMenu("&Help")
        help_menu.addAction(help_button)
        help_menu.addAction(report_issue_button)

        ## Layouts
        main_win = QWidget() # Main window layout

        # Main Horizontal layout --> IS supposed to look like this : | 1.editing tools | 2.display |
        main_layout = QHBoxLayout(main_win)

        editing_tools_layout = QVBoxLayout()
        t = QLabel("Toolbox")
        t.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        t.setProperty('class', "layout_back_transparent")
        t.setMaximumSize(250, int(1920/1.7))
        editing_tools_layout.addWidget(t)




        dis_l = QLabel('Display')
        dis_l.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        dis_l.setMaximumHeight(20)
        dis_l.setProperty('class', 'layout_back_transparent')

        self.display_layout = QVBoxLayout()
        self.display_layout.addWidget(dis_l)

        map_widget = QWidget()
        map_widget.setLayout(self.me_map)
        self.display_layout.addWidget(map_widget)


        main_layout.addLayout(editing_tools_layout)
        main_layout.addLayout(self.display_layout)
        main_win.setLayout(main_layout)
        self.setCentralWidget(main_win)

    def newProject(self):
        np_alert = CustomDialog(self, 'Create New Project ?', 'Creating a new project will erase data from current project if not saved.\nDo you wish to continue ?')

        if np_alert.exec() :
            print('Creating new project')
        else: print('Project Creation Canceled')

    def openProject(self):
        opn = OpenProject(self)
        project_data = opn.openpr()

        if self.me_map.isEmpty() is False: # Save the project before opening a new one
            open_pr_alert = CustomDialog(parent=self ,window_title="You have an open Project", message="Would you like to save ?")

            if open_pr_alert.exec() :
                print("Saving Project")
                self.saveProject()
            else: print("Will not be saved.")

            # reset the map
            for i in reversed(range(self.me_map.count())):
                self.me_map.itemAt(i).widget().setParent(None)

        if project_data is not None :
            print('Project Opened with data :', project_data)
            # project_network is the network representation for the project, this is the var that will be modified by all the actions performed on the network.
            self.project_network = networkConstructor(project_data)

            #set the layout
            for node in self.project_network.network_node_list :
                if node.pos[0] is not None :
                    temp = QLabel(node.name)
                    temp.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    temp.setProperty('class', "node")

                    self.me_map.addWidget(temp, node.pos[0], node.pos[1])
            self.me_map.setProperty("class", 'node_layout')



            ## Console logging purposes
            print(f'Number of nodes on the network: {len(project_data["nodes"])}\n'
                  f'NodeList: ')
            nl = []
            for node in project_data["nodes"] :
                nl.append(node)
            print(nl)

    def saveProject(self):
        try :
            sv = SaveProject(parent=self, data=self.project_network.Get_json_dict())
            sv.savepr()
        except :
            save_error = CustomDialog(self, "No Oppened Project", 'Try oppening or creating a project before saving')
            save_error.show()
    def openSettings(self):
        ## Not yet implemented. #TODO (settings)
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
    webbrowser.open('https://github.com/TheWarior73/Train_Map_Editor')
    print('Redirected towards github repo')

def issue_redirect():
    webbrowser.open('https://github.com/TheWarior73/Train_Map_Editor/issues')
    print('Redirected towards the issue tracker on the official repo')

def main():
    app = QApplication(sys.argv)

    with open("styles.css", 'r') as file :
        app.setStyleSheet(file.read())

    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()