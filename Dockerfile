FROM python:3.12-slim AS builder

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install uv --no-cache-dir uv
WORKDIR /usr/app/src
COPY pyproject.toml uv.lock ./
RUN uv sync --no-editable --frozen

FROM python:3.12-slim AS runtime

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /usr/app/src

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY src/ .


CMD [ "python" ]
