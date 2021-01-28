from mysql import connector
from config import Config

# Тут будет соединение с ДБ. методы уже не статические.
# Создавать объект в МЭЙНЕ, передаем конфиг в конструктор. 

# print(connector.connect(host='localhost', database='scada', user='root', password='root'))


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

# TODO: Сделать методы типа селект инсерт апдейт.
class DB(Singleton):

    connection = None
    config = {}

    def set_config(self, config):
        self.config = config['db']

    def connect(self, config=False):
        if config and not self.config:
            print(bool(config), bool(self.config))
            self.set_config(config)
        if self.connection is None:
            print('I run')
            try:
                self.connection = connector.connect(host=self.config['host'],
                                                    database=self.config['dbname'],
                                                    user=self.config['login'],
                                                    password=self.config['pass'])
                if self.connection.is_connected():
                    print("Connect to DB")
                    return self.connection
            except connector.Error as e:
                print('Error :: ', e)
        else:
            return self.connection

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection to DB close")

    def exec(self, query, params=''):
        cursor = self.connection.cursor()
        cursor.execute(query)
        if cursor.lastrowid:
            self.connection.commit()
        else:
            result = cursor.fetchall()
            return result


db = DB()
db.connect(config=Config.get_config())
# conn = db.connection(config=Config.get_config())
query = 'INSERT INTO monitoring.user (username, pass, token, tokendate) VALUES' \
        '(\'ramir2\',\'ramir8778\',\'sdkfjhgk4o3849384hfi34f34\', SYSDATE())'

result = db.exec(query)

print(result)


