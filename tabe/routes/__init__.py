from . import api


def init_app(app):
    app.register_blueprint(api.bp, url_prefix='/api')
