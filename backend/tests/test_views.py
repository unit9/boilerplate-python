from backend.tests.test_utils import assert_success
from backend.tests.test_utils import assert_client_failure
from backend.tests.test_utils import app


def test_response(app):
    response = app.get("/")
    assert_success(response)
    assert "Hello" in response.data
    assert "Unsupported" not in response.data


def test_unsupported(app):
    my_ua = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) "
             "AppleWebKit/537.78.2 (KHTML, like Gecko) "
             "Version/7.0.6 Safari/537.78.2")
    response = app.get("/", headers={"user-agent": my_ua})
    assert_success(response)
    assert "Hello" not in response.data
    assert "Unsupported" in response.data


def test_response_404(app):
    response = app.get("/404")
    assert_client_failure(response)
