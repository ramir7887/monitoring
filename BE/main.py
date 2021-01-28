from aiohttp import web
import logging
from start_axioma import Axioma

# пользовательские модули
from routes import Route


def init_app(config):
    app = web.Application()
    Route.init_routes(app)
    return app


def main():
    logging.basicConfig(filename='../logs/logfile.log', level=logging.DEBUG,
                        format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
    # Стартанем аксиому
    Axioma.start()

    app = init_app('config')
    web.run_app(app, host='127.0.0.1', port=8081)


if __name__ == '__main__':
    main()
