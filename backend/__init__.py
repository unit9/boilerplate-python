import flask
import whitenoise

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from raven.contrib.flask import Sentry

import settings
from backend.views import view_handler
from backend.utils.hacks import install_hacks


# Apply any required hacks/workarounds
install_hacks()


# Initialise app and config
app = flask.Flask("backend")
app.config.from_object(settings)


# Static content
application = whitenoise.WhiteNoise(
    app.wsgi_app,
    root="website",
    autorefresh=settings.DEBUG,
)


# Database
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


# Sentry
sentry = Sentry()
sentry.init_app(app, app.config["SENTRY_DSN"])


# Register views
app.register_blueprint(view_handler)


# Meta
def main():  # pragma: nocover
    from werkzeug.serving import run_simple
    run_simple(
        settings.HOST,
        settings.PORT,
        application,
        use_reloader=settings.DEBUG,
        use_debugger=settings.DEBUG,
    )


if __name__ == "__main__":  # pragma: nocover
    main()
