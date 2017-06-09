import json
import logging
import pytest

from backend import app as real_app
from backend import db as real_db


__all__ = [
    "app",
    "db",

    "assert_client_failure",
    "assert_success",
]


@pytest.fixture
def app():
    return real_app.test_client()


@pytest.fixture(scope="function")
def db(request):
    if not real_app.config["SQLALCHEMY_DATABASE_URI"]:
        pytest.skip("Database not configured")  # pragma: nocover

    ctx = real_app.app_context()

    def fin():
        real_db.session.close_all()
        real_db.drop_all()
        # This is a bit of a hack, since we can't use `with`
        ctx.__exit__(None, None, None)

    ctx.__enter__()
    request.addfinalizer(fin)
    real_db.session.close_all()
    real_db.drop_all()
    real_db.create_all()
    return real_db


def assert_success(response):
    __tracebackhide__ = True
    if response.status_code not in range(200, 300):  # pragma: nocover
        logging.debug("response status: %s", response.status)
        if response.mimetype == "application/json":
            logging.debug("response data: %r", json.loads(response.data))
        else:
            logging.debug("response data: %r", response.data)
        pytest.fail("Response error code: {}".format(response.status))


def assert_client_failure(response):
    __tracebackhide__ = True
    if response.status_code not in range(400, 500):  # pragma: nocover
        pytest.fail("Response error code: {}".format(response.status))
