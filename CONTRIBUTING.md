> [!WARNING]\
> This document is a **Work In Progress**.\
> Currently, login is implemented with an openid flow back to auth.sw.patrickpedersen.tech.\
> This document is also missing minio setup and configuration. Localstorage is being worked on.

## Setup development environment

Feel free to use `virtualenv` or similar tools to isolate development environment.
Below is an example of how to set up a virtual environment using `venv`.
```bash
git clone https://github.com/THE-BWC/OpServ.git
cd OpServ
python -m venv ./.venv
source .venv/bin/activate
```
You should now have a virtual environment created and activated.

## Install dependencies

The project requires:
- Python 3.12+ and [poetry](https://python-poetry.org/) to manage dependencies
- Node v20+ for front-end.
- MariaDB 11+

First, install all dependencies by running the following commands.
```bash
poetry install
```

Install npm packages
```bash
cd app/static
npm install
cd ../..
```

Install pre-commit hooks
```bash
poetry run task pre-commit
```

To run the pre-commit checks manually, run:
```bash
poetry run task lint
```

## Run the code locally
To run the code locally, please create a local setting file based on `.env-example`:
```
cp .env-example .env
```

Run docker compose to start all services:
```bash
docker compose up -f docker-compose.yml -d
```

Create the database schema:
```bash
poetry run task upgrade
```

Seed the database
```bash
poetry run task seed
```

To run the server:
```
export FLASK_ENV=development
poetry run flask run --host=0.0.0.0 --debug
```

then open http://localhost:5000, you should be able to login with `admin@example.com / admin` account.
