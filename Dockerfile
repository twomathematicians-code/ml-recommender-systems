FROM python:3.11-slim AS build
RUN pip install poetry==1.8.3
WORKDIR /app
COPY pyproject.toml ./
RUN poetry config virtualenvs.in-project true && poetry install --only main --no-root

FROM python:3.11-slim
WORKDIR /app
COPY --from=build /app/.venv .venv
COPY src/ src/
RUN useradd -m recuser && chown -R recuser .venv src
USER recuser
ENV PATH=/app/.venv/bin:$PATH
EXPOSE 9000
CMD ["uvicorn", "src.api.main:app", "--port", "9000", "--host", "0.0.0.0"]
