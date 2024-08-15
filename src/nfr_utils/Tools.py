"""The editing tools available to modify the Network
This fils links the UI and the backend

---

MIT License

Copyright (c) 2024 Th3_Warior & contributors

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. Please refer to the LICENCE file
"""
# TODO Ui


## IMPORTS ##

# - NFR-Lib - #
if __name__ == "__main__" : # Debug
    from Node import Node
    from Network import Network
else : 
    from nfr_utils import Node, Network

## IMPORTS ##

def create_node(posX: int, posY: int, nodelist: list[Node]):
    """Creates a Node in the network, at a given PosX/Y with a default name name: 'Enter A Name'\n
    Params: posX (int)\n
            posY (int)\n
            nodelist (list[Node])
    Output: new_node (Node) | None\n
    Will return None if the Node cannot be placed\n
    Will return Node object otherwise"""
    for node in nodelist :
        # Checking if the node can be placed here
        if node.pos[0] == posX and node.pos[1] == posY :
            return None
    # Placing node
    new_node = Node("Enter A name")
    new_node.pos = (posX, posY)
    return new_node


def remove_node(node: Node, network: Network):
    """Removes a node from the network and the display\n
    Will return the Node object if sucessfull\n
    Will return None Otherwise"""
    pass


def add_link():
    pass

def remove_link(node_a: str, node_b: str):
    pass

def set_color(color: str, node : Node):
    """Sets the colour of a Node
    - Either give a color using str, like 'white' or 'red' or 'blue'
    - Or give a color using hex values like '#000000' or '#ffffff' (the # is required)
    
    Params: color (str)
            node (Node)
    Output: None"""

    ## TODO change the colours to be a more pleasing palette instead of this fairly basic one
    color_list = [{'name':'red','color':'#ff0000'},
                  {'name':'green','color':'#00ff00'},
                  {'name':'blue','color':'#0000ff'},
                  {'name':'yellow','color':'#ffff00'},
                  {'name':'cyan','color':'#00ffff'},
                  {'name':'magenta','color':'#ff00ff'},
                  {'name':'brown','color':'#a52a2a'},
                  {'name':'white','color':'#ffffff'},
                  {'name':'black','color':'#000000'}]
    
    if type(color) is str : 
        if color[0] != '#' :
            for elt in color_list :
                if color == elt['name'] :
                    node.colors.append(elt["color"])
        else :
            node.colors.append(color)
    pass

def set_pos(x: int, y: int, node: Node):
    """Sets the pos of a Node and update it on the grid
    Params :x (int)
            y (int)
            node (Node)
    Output: None"""
    

