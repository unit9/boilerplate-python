#!/usr/bin/env python
"""Manage common tasks

usage: manage.py [-?] <command> ...

For development, please refer to the documentation:

https://flask-script.readthedocs.org/
"""
from __future__ import print_function

import json

from flask import Flask, current_app
from flask.ext.script import Manager
from flask.ext.script.commands import ShowUrls, Clean

from backend import app


manager = Manager(app)


@manager.command
def dumpconfig():
    "Dumps config"
    for key in sorted(current_app.config):
        print(key, "=", repr(current_app.config[key]))


manager.add_command("urls", ShowUrls())
manager.add_command("clean", Clean())


if __name__ == "__main__":
    manager.run()
