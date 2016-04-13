import flask
import settings


app = flask.Flask("backend")


def main():
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
    )


if __name__ == "__main__":
    main()
