from aiohttp import web
from services import opc
from config import Config

# TODO: Добавить метод возвращающий иерархию адресов нод
# TODO: Доработать метод авторизации

class Resource:

    @staticmethod
    async def index(request):
        client = opc.OpcClient(Config.get_config())
        data = client.exec()
        return web.json_response(data,
                                 headers={'Accept': 'application/json',
                                          'Access-Control-Allow-Origin': '*',
                                          'Access-Control-Allow-Methods': '*',
                                          'Access-Control-Allow-Headers': '*'}
                                 )

    @staticmethod
    async def get_info(request):
        message = 'OPC UA клиент.' \
                  'Предостовляемые методы: ' \
                  '\n/get_opc_data -- полный список параметров ' \
                  '\n/get_opc_node_data -- параметры для ноды '
        return web.Response(text=message)

    # TODO: Переименовать метод, т.к. он для OPC UA только возвращает данные.
    @staticmethod
    async def get_opc_data(request):
        """
        Возвращает JSON объект со всеми данными от OPC сервера,
        если параметр запроса url не передан, используется url из конфиг файла
        :param request: url: str, optional
        :return: json object
        """
        client = opc.OpcClient(Config.get_config())
        data = client.get_full_data()
        print(data)
        # return web.Response(text=str(data))
        return web.json_response(data,
                                 headers={'Accept': 'application/json',
                                          'Access-Control-Allow-Origin': '*',
                                          'Access-Control-Allow-Methods': '*',
                                          'Access-Control-Allow-Headers': '*'
                                          }
                                 )

    @staticmethod
    async def get_opc_node_data(request):
        if request.query.keys() and request.query.get('param', False):
            param = request.query['param']
            client = opc.OpcClient(Config.get_config())
            data = client.get_data_by_nodeid(param)
            return web.json_response(data=data)

        data = {
            "status": "ERROR",
            "message": "Отсутствует обязательный параметр param."
        }
        return web.json_response(data=data, status=500)

    @staticmethod
    async def auth(request):
        pass
