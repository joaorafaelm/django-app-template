FROM python:3.13

ENV PYTHONWARNINGS=ignore
ENV DISPLAY=:99
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/venv/bin:$PATH

RUN apt update -y

RUN pip install --upgrade pip uv
WORKDIR /app

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.13 \
    UV_PROJECT_ENVIRONMENT=/venv

COPY pyproject.toml /_lock/
COPY uv.lock /_lock/

RUN --mount=type=cache,target=/root/.cache <<EOT
cd /_lock
uv sync \
    --locked \
    --no-dev \
    --no-install-project
EOT

COPY . /app

RUN --mount=type=cache,target=/root/.cache \
    uv pip install \
        --python=$UV_PROJECT_ENVIRONMENT \
        --no-deps \
        /app

ENTRYPOINT ["/app/docker-entrypoint.sh"]
