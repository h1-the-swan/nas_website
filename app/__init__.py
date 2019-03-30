import os
from flask import Flask
from six import string_types

from config import DevelopmentConfig, ProductionConfig

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app(config='production'):
    """
    :config: can be one of ['production', 'development'], or a config object
    """
    if isinstance(config, string_types):
        if config.lower().startswith('dev'):
            config = DevelopmentConfig()
        elif config.lower().startswith('prod'):
            config = ProductionConfig()
        else:
            raise RuntimeError("invalid `config`")

    app = Flask(__name__)
    app.config.from_object(config)
    if app.config.get('STATIC_FOLDER') is None:
        app.config['STATIC_FOLDER'] = app.static_url_path

    from . import main
    app.register_blueprint(main.bp)

    return app
