import flask
import whitenoise

import settings


app = flask.Flask("backend")
application = whitenoise.WhiteNoise(
    app.wsgi_app,
    root="website",
    autorefresh=settings.DEBUG,
)


@app.route("/")
def index():
    return flask.send_file("../website/index.html")


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
