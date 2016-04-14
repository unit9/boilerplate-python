import unittest2
import logging
import json

from . import app as real_app


__all__ = [
    "Test",
]


class Test(unittest2.TestCase):

    def setUp(self):
        self.app = real_app.test_client()

    def tearDown(self):
        pass

    def assertRequestSuccess(self, response):
        if response.status_code not in xrange(200, 300):  # pragma: nocover
            logging.debug("response status: %s", response.status)
            if response.mimetype == "application/json":
                logging.debug("response data: %r", json.loads(response.data))
            else:
                logging.debug("response data: %r", response.data)
            raise AssertionError(response.status)

    def assertRequestClientFailure(self, response):
        self.assertIn(response.status_code, xrange(400, 500))
