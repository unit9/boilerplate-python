import json
import logging
import pytest

from . import app as real_app


__all__ = [
    "app",
    "assert_success",
    "assert_client_failure",
]


@pytest.fixture
def app():
    return real_app.test_client()


def assert_success(response):
    __tracebackhide__ = True
    if response.status_code not in xrange(200, 300):  # pragma: nocover
        logging.debug("response status: %s", response.status)
        if response.mimetype == "application/json":
            logging.debug("response data: %r", json.loads(response.data))
        else:
            logging.debug("response data: %r", response.data)
        pytest.fail("Response error code: {}".format(response.status))


def assert_client_failure(response):
    __tracebackhide__ = True
    if response.status_code not in xrange(400, 500):  # pragma: nocover
        pytest.fail("Response error code: {}".format(response.status))
