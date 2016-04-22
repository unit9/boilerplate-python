from backend.tests.test_utils import assert_success
from backend.tests.test_utils import assert_client_failure
from backend.tests.test_utils import app


def test_response(app):
    response = app.get("/")
    assert_success(response)


def test_response_404(app):
    response = app.get("/404")
    assert_client_failure(response)
