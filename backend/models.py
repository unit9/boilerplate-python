from . import db


class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return "<{} {!r}>".format(type(self).__name__, self.id)


class User(db.Model, BaseMixin):
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email
