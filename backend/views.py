import flask
from flask import Blueprint

from backend.utils import ua

view_handler = Blueprint('views', __name__)


@view_handler.route("/")
def index():
    user_agent = flask.request.headers.get("User-Agent", "")
    if ua.is_supported(user_agent):
        site = "index.html"
    else:
        site = "unsupported.html"
    return flask.send_file("../website/{}".format(site))
