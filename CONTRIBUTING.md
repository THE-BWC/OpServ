> [!WARNING]\
> This document is a **Work In Progress**.\
> Currently, login is implemented with an openid flow back to auth.sw.patrickpedersen.tech.\
> This document is also missing minio setup and configuration. Localstorage is being worked on.

## Install dependencies

The project requires:
- Python 3.12+ and [poetry](https://python-poetry.org/) to manage dependencies
- Node v20+ for front-end.
- MariaDB 11+

First, install all dependencies by running the following commands.
Feel free to use `virtualenv` or similar tools to isolate development environment.

```bash
poetry install
```

Install npm packages

```bash
npm install
```

Install pre-commit hooks

```bash
poetry run pre-commit install
```

To run the pre-commit checks manually, run:

```bash
poetry run pre-commit run --all-files -v
```

## Run the code locally

To run the code locally, please create a local setting file based on `.env-example`:

```
cp .env-example .env
```

Run the MariaDB database:

```bash
docker run -e MYSQL_DATABASE=opserv -e MYSQL_USER=opserv -e MYSQL_PASSWORD=opserv -e MYSQL_ROOT_PASSWORD=opserv -p 3306:3306 mariadb:11
```

Create the database schema:

```bash
poetry run flask db upgrade
```

Seed the database
```bash
poetry run flask seed
```

To run the server:

```
export FLASK_ENV=development
python app/server.py
```

then open http://localhost:5000, you should be able to login with `admin@example.com / admin` account.
