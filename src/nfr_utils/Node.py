"""
This file creates a Node Object used by the Network, actions performed on the node are the following:
- set pos (x,y)
- set type

---

MIT License

Copyright (c) 2024 Th3_Warior & contributors

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. Please refer to the LICENCE file
"""

class Node:
    """Methods:\n
    - set_pos | sets the pos of the node in the grid
    - set_type | sets the type of node to display in the grid"""

    def __init__(self, name: str, colors=None):
        """A node is :
        - A name (str)
        - A list of connected nodes* / **
        - A list of colors (links between nodes) the node has (i.e. green and orange)
        - An x;y pos tuple on the grid for the node
        - the type of node

        * directly linked to the node
        ** List of Nodes names (str)"""
        self.colors = []
        if colors is not None : # We add the colors to the color list
            for col in colors :
                self.colors.append(col)
        self.name = name
        self.connected_nodes = []
        self.pos = ()
        self.node_type = ''

    def __str__(self):
        """Debuging function"""
        res = f'Node : {self.name} \nConnected Node.s:\n['
        if len(self.connected_nodes) != 0 :
            for p in self.connected_nodes :
                res += p + ', '
            res = res[:-2] + "]"
        else: res += 'None]'
        return res

    ## ===== Methods ===== ##
    def set_pos(self, x: int, y: int):
        """Set the node x;y position in the grid"""
        self.pos = (x, y)
        pass

    def set_type(self, type_of_node: str = 'station'):
        """Possible node types :\n
        - **"station"** a station node
        - **"interchange"** an interchange station node
        - **"end"** the end of line station node
        - **"continue_oob"** an end of line continuity out of bonds arrow station node
        - **"link"** a non_station node to link stations together **# TODO check if good idea or not**"""
        possible_node_list = ['station', 'interchange', 'end', 'continue_oob', 'link']
        if type_of_node in possible_node_list :
            self.node_type = type_of_node
            return None
        return -1
