"""settings -- application settings, knobs and configuration

How to use! As a developer:

- Keep It Simple, Silly! A sysop will have to read and use it.

- Use simple, flat variables - scalars like integers or strings; avoid
  deeply nested dicts or arrays.

- Make conversion between an environment variable and a Python
  datatype simple and obvious:

    - ISO8601 for dates and times

    - "0"/"1" for bool False/True

    - comma-separated values for arrays, like: IPS=127./8,192.168./16

    - KISS

- Look at the current examples, try to follow the conventions!

As a system administrator / when preparing for deployment:

- Read this file!

- Everything else is in environment variables:

    - LOGLEVEL can be adjusted between:
      DEBUG, INFO, WARNING, ERROR, FATAL;

    - HOST and PORT are for the builtin dev server, and will be of
      little use, since you must use a real application server like
      uWSGI;

- Talk to the developers!

"""

import os
import logging


# Local development server
HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "5000"))

# Logging, debugging
DEBUG = int(os.environ.get("DEBUG", "0"))
TESTING = int(os.environ.get("TESTING", "0"))
LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()

# Database-related; http://flask-sqlalchemy.pocoo.org/latest/config/
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "")

# Sentry
SENTRY_DSN = os.environ.get("SENTRY_DSN", "")

# Avoid changing things below this line, unless necessary.

logging.basicConfig(level=getattr(logging, LOGLEVEL))
