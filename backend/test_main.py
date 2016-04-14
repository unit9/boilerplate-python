from .test_utils import *


class MainTest(Test):

    def test_response(self):
        response = self.app.get("/")
        self.assertRequestSuccess(response)

    def test_response_404(self):
        response = self.app.get("/404")
        self.assertRequestClientFailure(response)
