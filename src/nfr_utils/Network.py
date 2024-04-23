"""
Network object that represents a metro/train map

---

MIT License

Copyright (c) 2024 Th3_Warior

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. Please refer to the LICENCE file
"""

## Imports
from .Node import Node

##

class Network:
    """Class that represents a Network (Node Graph)

    Methods :\n
    - add_node()    --> Add a node to the network graph
    └─ add_nodes()\n
    - remove_node()   --> Remove a node from the network graph
    └─ remove_nodes()\n
    - link_node()     --> Link a tuple of two nodes together
    └─ link_nodes()\n
    - Get_node_index() --> Returns the index of the node given in parameter in the Get_nodes() list
    - Get_nodes()     --> Returns a list of all the nodes (names -> str) in the graph
    - Get_node_links() --> Return a list of links for the node in the graph
    - remove_link() --> removes a link between two nodes
    - Get_json_dict() --> returns a dict representing the Network, allowing it tobe parsed to Json

    """
    def __init__(self, nodeslist: list[str] = None):
        """The nodelist is a list of the names of the nodes, we are converting the names into actual node objects here
        :param nodeslist: A list of node names to create in the network
        :return None"""
        self.network_node_list = []
        self.colours = [] # List de tuples (id: int, couleur: str)
        if nodeslist is not None :
            for node_name in nodeslist :
                self.network_node_list.append(Node(node_name))

    def __str__(self):
        """Displays the graph node list in the console
        :return res: str """
        res = "Here is a table of the Network :\n"
        for elt in self.network_node_list :
            res += f"{elt.name} | cn - {[self.network_node_list[self.Get_node_index(node)].name for node in elt.connected_nodes]} | cl - {elt.colors}\n"
        return res

    ## ====== Methods ====== ##

    def Get_nodes(self) :
        """return the list of nodes of the network
        :return node_names: list[str]"""
        node_names = [elt.name for elt in self.network_node_list]
        return  node_names

    def Get_node_index(self, n : str):
        """Returns the index of the node n in the Get_nodes() list
        :param n: (str) -- A node name to find in the network"""
        nodes = self.Get_nodes()
        for i in range(len(nodes)) :
            if nodes[i] == n :
                return i
        return -1

    def is_node_in_network(self, node: str):
        """Checks if the node is in the network
        :param node: (str) -- A node name to check"""
        if self.Get_node_index(node) == -1 :
            return False
        return True

    def Get_node_links(self, n: str):
        """return the adjacent nodes (the ones it is connected to) of the node given in parameters
        :param n: (str) -- A node name to check"""
        index = self.Get_node_index(n)
        links = []
        if index != -1 :
            for elt in self.network_node_list[index].connected_nodes :
                links.append(elt)
            return links
        return None

    def remove_link(self, nodes: tuple[str, str]):
        """Removes a link between 2 nodes
        :param nodes: (tuple[str, str]) -- a tuple of node names to unlink"""
        # checks if the node is in the Network
        for elt in nodes :
            if self.is_node_in_network(elt) == False :
                return -1
        # removes the link
        try :
            self.network_node_list[self.Get_node_index(nodes[0])].connected_nodes.remove(nodes[1])
            self.network_node_list[self.Get_node_index(nodes[1])].connected_nodes.remove(nodes[0])
        except ValueError :
            pass

    def link_node(self, nodes: tuple[str, str]):
        """Links two nodes together to create a 'road' between them
        :param nodes: (tuple[str, str]) -- a tuple of node names to link"""
        node_1 = self.Get_node_index(nodes[0])
        node_2 = self.Get_node_index(nodes[1])
        # Checks if the nodes exists
        assert node_1 != -1, "Inexistant Node"
        assert node_2 != -1, "Inexistant Node"
        # Linking them
        self.network_node_list[node_1].connected_nodes.append(nodes[1])
        self.network_node_list[node_2].connected_nodes.append(nodes[0])
        pass

    def link_nodes(self, nodes: list[tuple[str, str]]):
        """Links a list of nodes tuples together, uses the method link node to link the tuples together
        :param nodes: (list[tuple[str, str]]) -- a list of tuple of node names to link"""
        for elt in nodes :
            try :
                self.link_node(elt)
            except AssertionError:
                print(f'Inexistant Node.s : {elt}')
        pass

    def add_node(self, name: str):
        """Add a node to the network
        :param name: (str) -- A node name to create and add to the network"""
        self.network_node_list.append(Node(name))
        pass

    def add_nodes(self, nodes: list[str]):
        """Add a list of nodes to the Network
        :param nodes: (list[str]) -- A list of node names to create and add to the network"""
        for node in nodes :
            self.add_node(node)
        pass

    def remove_node(self, name: str):
        """Removes a node from the network, it not only removes it, but also removes it from the other nodes connections"""
        # Checks if the node is in the Network
        if self.is_node_in_network(name) :
            # we break the link of the node to the others
            for linked_node in self.network_node_list[self.Get_node_index(name)].connected_nodes :
                self.remove_link((name, linked_node))
            # Finaly, we remove the node from the list
            self.network_node_list.remove(self.network_node_list[self.Get_node_index(name)])
        pass

    def remove_nodes(self, nodes: list[str]):
        """Removes a list of nodes from the Network using the remove_node function."""
        for node in nodes :
            self.remove_node(node)
        pass

    def Get_json_dict(self):
        """Returns a dict representing the Network, allowing it to be parsed by json"""
        res = {"nodes": {}}
        for node in self.network_node_list :
            res["nodes"][node.name] = [{"posX": None, "posY": None, "color": [color for color in node.colors], "connected": [node_name for node_name in node.connected_nodes]}]
        return res


def networkConstructor(network_dict: dict=None) :
    """Constructs the network based on a dictionary (json format)
    Usefull upon oppening a project"""
    if network_dict is None : # in case of a null paramn, return an empty Network
        return Network()
    net_res = Network()


    for node in network_dict["nodes"] :
        net_res.add_node(node)
        for elt in network_dict["nodes"][node] :
            cur_node = net_res.network_node_list[net_res.Get_node_index(node)]
            cur_node.set_pos(elt["posX"], elt["posY"])
            cur_node.connected_nodes = elt["connected"]

    return net_res

def test() :
    data = {'nodes': {'NFRC': [{'posX': None, 'posY': None, 'color': [], 'connected': ['SEP', 'MP']}], 'SEP': [{'posX': None, 'posY': None, 'color': [], 'connected': ['NFRC']}], 'MP': [{'posX': None, 'posY': None, 'color': [], 'connected': ['NFRC', 'NH']}], 'NH': [{'posX': None, 'posY': None, 'color': [], 'connected': ['MP', 'RH']}], 'RH': [{'posX': None, 'posY': None, 'color': [], 'connected': ['NH', 'RC']}], 'RC': [{'posX': None, 'posY': None, 'color': [], 'connected': ['RH', 'RF', 'S']}], 'RF': [{'posX': None, 'posY': None, 'color': [], 'connected': ['RC', 'FC']}], 'FC': [{'posX': None, 'posY': None, 'color': [], 'connected': ['RF']}], 'S': [{'posX': None, 'posY': None, 'color': [], 'connected': ['RC', 'SC']}], 'SC': [{'posX': None, 'posY': None, 'color': [], 'connected': ['S']}]}}
    network_map = networkConstructor(data)

    print(network_map.Get_json_dict())

    # display the map nodes
    print(network_map)

if __name__ == '__main__' :
    test()