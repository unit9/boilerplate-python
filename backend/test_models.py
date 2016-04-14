from .test_utils import *

from .models import User


def test_create_user(db):
    u = User(username="test", email="test@example.com")
    db.session.add(u)
    db.session.commit()

    assert User.query.one()


def test_model_repr(db):
    u = User(username="test", email="test@example.com")
    assert repr(u) == "<User None>"

    db.session.add(u)
    db.session.commit()

    u = User.query.one()
    assert repr(u) == "<User 1>"
