<!-- -*- coding: utf-8 -*- -->

# Python boilerplate

To make starting new projects fast & easy :)

## Development of the boilerplate

Please use [this Trello board](https://trello.com/b/B2dKXJYG) to track
issues and features.

## Using in your project

1. Clone the repo
2. Copy the relevant bits into your source tree
3. Edit this readme and include references to your project
4. Commit!

## Quick start

1. `vagrant up`
2. `vagrant ssh`
3. `cd /vagrant`
4. `./run_devserver`
5. <http://localhost:5000>

### Installing dependencies

If you don't need a particular dependency, feel free to delete the
relevant code / integration.

#### Python

For development:

    pip install -r requirements-dev.txt

For development and production:

    pip install -r requirements-lock.txt

To update core dependencies:

    pip install -U -r requirements.txt
    pip freeze --local > requirements-lock.txt

Apply `virtualenv`, various flags, etc as fit for your environment.

#### PostgreSQL

You have two options:

- (Easy) use Vagrant (`vagrant up`, `vagrant ssh`) as your dev
  environment.
- (Expert) Set things up by hand:
    - Install and run a local PostgreSQL server, version 9.4, either
      from your operating system's packages/ports, or via
      [Docker](https://hub.docker.com/_/postgres/);
    - Set the `SQLALCHEMY_DATABASE_URI` environment variable (see
      "Configuration" below);
    - Use provided scripts in [`cmd`](/cmd) (`db_create`,
      `db_create_tables`).

### Running tests

You should run:

    ./run_tests

If external services, such as database, are not available, some of the
tests will be automatically skipped.

### Configuration

Read carefully the contents of the file [`settings.py`](/settings.py),
everything is explained in great detail. In short, you need to set a
bunch of environment variables.

#### PostgreSQL

You should define `SQLALCHEMY_DATABASE_URI` as follows:

    postgresql://user:password@host:port/database

- `:port` defaults to 5432; `:password` can be omitted if none is set.
- For CI builds / testing: `postgresql://postgres@localhost/test`

    This is the default in `run_tests`, if not defined.

- For Vagrant / local dev:  `postgresql://postgres@localhost/local`

    This is the default in `run_devserver`, if not defined.

- For production, it's sysop's job to figure it out!

    Amazon's [RDS](https://aws.amazon.com/rds/) managed database
    service works extremelly well.

### Running in development

You should run:

    ./run_devserver

You can override the environment variables `HOST` and `PORT`, which
default to `127.0.0.1` and `5000` respectively.

Visit <http://localhost:5000/> to see the website in development.

When you save a Python source file, the dev server will automatically
pick up that change and reload the code.

Press Control-C to stop the server.

#### Sentry

Do yourself a favor and get yourself a
[Sentry](https://www.getsentry.com/). Hosted Sentry is great; UNIT9
has an account, ask to get access.

For development / production servers, set the configuration variable
`SENTRY_DSN`. Don't do this for local development or unit testing,
someone else on the team may try to kill you for all your typos and
alert spam...

### Managing `.gitignore`

The `.gitignore` file is managed with the help of
<https://www.gitignore.io/>. It uses a simple list hinting at your
tech stack. It includes Python, OS X, Linux and Windows by default. If
you use a particular IDE or some other piece of tooling that may leave
some trash behind, you should check if `gitignore.io` supports it.

Edit the file [`update_gitignore`](/update_gitignore); change the
value of `$environment` to a comma-separated list describing your tech
stack; refer to <https://www.gitignore.io/> for help. 

If `gitignore.io` does not get the job done, you can also edit
[`.gitignore.tail`](/.gitignore.tail). The contents of the file will
be appended at the bottom of the generated `.gitignore`. 

Run `./update_gitignore` when done tweaking.

### Other goodies / bultin functionality

#### Browser blacklisting

There's a basic browser detection / blacklisting feature, which
handles a common requirement on many projects.

It can be used to serve an "unsupported browser" page for browsers /
devices that are explicitly blacklisted in the Technical Specification
and/or Statement of Work.

Use the `backend.utils.ua.is_supported` function to match the user
agent (this is already done for the landing page handler).

You can edit [`browsers.yml`](/browsers.yml) to tweak the blacklist.

### Running in production

#### The Stack

You will at least need to understand how WSGI works: spec for
[Python 2.x](https://www.python.org/dev/peps/pep-0333/),
[Python 3.x](https://www.python.org/dev/peps/pep-3333/),
[some explaining on SO](http://stackoverflow.com/a/9664122).

Currently, one of the best ways to run WSGI apps in production is
[uWSGI](https://uwsgi-docs.readthedocs.org/).

It is also recommended to use [Docker](https://www.docker.com/).

#### The App

Read [`settings.py`](/settings.py) to understand which runtime
parameters you can control.

The included [`Dockerfile`](/Dockerfile), based on
[`unit9/base`](https://hub.docker.com/r/unit9/base/), includes
everything you need to get started.

The run-script for production server comes from the base image
([`unit9/web-*`](https://github.com/unit9/docklabs/tree/master/web)),
and runs (via [runit](http://smarden.org/runit/)) a uWSGI master
process with a bunch of workers, under an unprivileged account.

When using the bundled script and/or `Dockerfile`, you can override
any of these environment variables:

- `PORT`, where uWSGI will listen (default: `5000`)
- `UWSGI_PROCESSES`, adjust number of uWSGI processes (default: 2),
  best if you can match the number of physical CPUs on the host
- `UWSGI_THREADS`, number of threads per uWSGI process (default: 32)
- And anything else, as defined in [`settings.py`](/settings.py)!

Note that for security reasons, `DEBUG` and `TESTING` are hardcoded to
`0`; change the run script if you absolutely must.

#### Building the image

Be smart. Don't do this by hand. Use a CI service, e.g. Shippable.

    docker build -t my_app_image .

#### Running the image

Be smart. Don't do this by hand. Use automation tools, e.g. Ansible.

    docker run --rm -ti -e PORT=8080 -e UWSGI_PROCESSES=4 -p 80:8080 --name myapp my_app_image

#### Database migrations

The tool used for database migrations is [Alembic][]; it is wrapped in
a script, [`manage.py`](/manage.py). The most important command is:

    ./manage.py db migrate

[Alembic]: https://alembic.readthedocs.org/

## Acknowledgements

- Kamil Cholewiński <kamil@unit9.com>
- Mateusz Kubaczyk <mateusz.kubaczyk@unit9.com>
