from resources import Resource


class Route:

    @staticmethod
    def init_routes(app):
        app.router.add_get('/get_opc_node_data', Resource.get_opc_node_data, name='get_opc_node_data')
        app.router.add_get('/get_opc_data', Resource.get_opc_data, name='get_opc_data')
        app.router.add_get('/get_info', Resource.get_info, name='get_info')
        app.router.add_get('/', Resource.index)
