# Third party libs
from flask.ext.script import Manager
from flask.ext.script import Server

# Our libs
from server.app import create_app
from server.settings import Config

def main():
    app = create_app(Config)
    manager = Manager(app)
    manager.add_command('runserver', Server(host='0.0.0.0'))
    manager.run()

if __name__ == '__main__':
    main()

