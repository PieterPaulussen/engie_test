from .core_api import core_api


def register_views(app):
    """Register all endpoints within the core api."""
    app.register_blueprint(core_api)
