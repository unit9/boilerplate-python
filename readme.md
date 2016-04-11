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

Visit <http://localhost:5000/> to see the website in development.

When you save a Python source file, the dev server will automatically
pick up that change and reload the code.

Press Control-C to stop the server.

## Acknowledgements

- Kamil Cholewiński <kamil@unit9.com>
- Mateusz Kubaczyk <mateusz.kubaczyk@unit9.com>
