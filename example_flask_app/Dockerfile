FROM astral/uv:python3.12-bookworm-slim

WORKDIR /app

COPY . .

RUN uv sync

EXPOSE 5000

ENTRYPOINT ["uv", "run", "main.py"]
CMD [ "--name", "World" ]