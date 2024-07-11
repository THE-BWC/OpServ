# Main image
FROM python:3.12

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Add poetry to PATH
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /app

# Copy poetry files
COPY poetry.lock pyproject.toml ./

# Install and setup poetry
RUN pip install -U pip \
    && apt-get update \
    && apt-get install -y curl netcat-traditional gcc python3-dev git libre2-dev cmake ninja-build \
    && curl -sSL https://install.python-poetry.org | python3 \
    # Remove curl and netcat from the image
    && apt-get purge -y curl netcat-traditional \
    # Run poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root \
    # Clear apt cache \
    && apt-get purge -y libre2-dev cmake ninja-build \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \

# Copy project files into /app
COPY . .

EXPOSE 7777

#gunicorn wsgi:app -b 0.0.0.0:7777 -w 2 --timeout 15 --log-level=debug
CMD ["gunicorn","wsgi:app","-b","0.0.0.0:7777","-w","2","--timeout","15"]