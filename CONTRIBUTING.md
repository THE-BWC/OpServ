> [!WARNING]\
> This document is a **Work In Progress**.\
> Currently, login is implemented with an openid flow back to auth.sw.patrickpedersen.tech.\
> This document is also missing minio setup and configuration.

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

## Run the code locally

To run the code locally, please create a local setting file based on `.env-example`:

```
cp .env-example .env
```

Run the MariaDB database:

```bash
docker run -e MYSQL_DATABASE=opserv -e MYSQL_USER=opserv -e MYSQL_PASSWORD=opserv -e MYSQL_ROOT_PASSWORD=opserv -p 3306:3306 mariadb:11
```

To run the server:

```
alembic upgrade head && python3 server.py
```

then open http://localhost:5000, you should be able to login with `john@wick.com / password` account.