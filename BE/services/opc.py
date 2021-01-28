from opcua import Client
import opcua
from opcua.ua.uaerrors import BadAttributeIdInvalid


class OpcClient:

    def __init__(self, config):
        if config['clients']['opc']['host']:
            self.client = Client(config['clients']['opc']['host'])
            self.settings = config['clients']['opc']['settings']
            self.params = config['clients']['opc']['params']

    # не знаю пока зачем
    # TODO: Добавить проверку на наличие соединения
    def check_connect(self):
        if self.client.connect():
            self.client.disconnect()
            return True
        else:
            self.client.disconnect()
            return False

    @staticmethod
    def get_data_node(parent_node, settings, params, data):
        if parent_node.get_children():
            node_name = parent_node.get_display_name().Text
            data[node_name] = {}
            for child_node in parent_node.get_children():
                child_name = child_node.get_display_name().Text
                if child_name in settings:
                    if child_name in params:
                        data[node_name][child_name] = child_node.get_value()
                    OpcClient.get_data_node(child_node, settings, params, data)

    @staticmethod
    def get_all_data(parent_node, data):
        if parent_node.get_children():
            node_name = parent_node.get_display_name().Text
            if node_name == 'Types':
                return
            data[node_name] = dict()
            for child_node in parent_node.get_children():
                child_name = child_node.get_display_name().Text
                if child_name == 'Types':
                    continue
                try:
                    value = child_node.get_value()
                    if not isinstance(value, int) or not isinstance(value, float)\
                            or not isinstance(value, bool):
                        value = str(value)
                        value = value.replace('{', '')
                        value = value.replace('}', '')
                    data[node_name][child_name] = value
                except BadAttributeIdInvalid:
                    data[node_name][child_name] = 'UNAVAILABLE'
                OpcClient.get_all_data(child_node, data[node_name]) # [child_name])

    def exec(self):
        self.client.connect()
        root = self.client.get_root_node()
        data = dict()
        OpcClient.get_data_node(root, self.settings, self.params, data)
        self.client.disconnect()
        return data

    def get_full_data(self):
        self.client.connect()
        root = self.client.get_root_node()
        data = dict()
        OpcClient.get_all_data(root, data)
        self.client.disconnect()
        return data

    def get_data_by_nodeid(self, param):
        """
        По входному параметру находит нужную ноду и возвращает ее имя и значение.
        Если нода имеет дочерние ноды, возвращает все информацию по ноде и все дочерним нодам.
        Входной параметр param является обязятельным.
        :param param: str
        :return: dict
        """
        self.client.connect()
        data = dict()
        node = self.client.get_node(param)
        if not node.get_children():
            node_name = node.get_display_name().Text
            node_value = node.get_value()
            print('________________________')
            print(node.get_path())
            print('________________________')
            data = {
                node_name: node_value
            }
        else:
            OpcClient.get_all_data(node, data)
            print('________________________')
            print(node.get_path())
            print('________________________')
        self.client.disconnect()
        return data







