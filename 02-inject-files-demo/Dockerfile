FROM registry.access.redhat.com/ubi9/python-312
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY . /src/sample_project
WORKDIR /src/sample_project
RUN bash -c "source /tmp/hermeto.env && uv pip install --system --python /opt/app-root/bin/python3.12 . --verbose"
CMD ["python3", "-c", "from importlib.metadata import version; print(f'flask=={version(\"flask\")}'); print(f'httpx=={version(\"httpx\")}'); print(f'click=={version(\"click\")}'); print('SUCCESS')"]
