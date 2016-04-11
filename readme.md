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

### Installing dependencies

For development:

    pip install -r requirements-dev.txt

For development and production:

    pip install -r requirements.txt

Apply `virtualenv`, various flags, etc as fit for your environment.

### Running tests

You should run:

    ./run_tests

### Configuration

Read carefully the contents of the file [`settings.py`](/settings.py),
everything is explained in great detail. In short, you need to set a
bunch of environment variables.

### Running in development

You should run:

    ./run_devserver

You can override the environment variables `HOST` and `PORT`, which
default to `127.0.0.1` and `5000` respectively.

Press Control-C to stop the server.

### Managing `.gitignore`

The `.gitignore` file is managed with the help of
<https://www.gitignore.io/>. It uses a simple list hinting at your
tech stack. It includes Python, OS X, Linux and Windows by default. If
you use a particular IDE or some other piece of tooling that may leave
some trash behind, you should check if `gitignore.io` supports it.

Edit the file [`update_gitignore`](/update_gitignore); change the
value of `$environment` to a comma-separated list describing your tech
stack; refer to `gitignore.io` for help.

## Acknowledgements

- Kamil Cholewiński <kamil@unit9.com>
- Mateusz Kubaczyk <mateusz.kubaczyk@unit9.com>
