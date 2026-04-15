FROM registry.access.redhat.com/ubi9/python-312

COPY . /src/sample_project
WORKDIR /src/sample_project

RUN source /tmp/hermeto.env \
    && pip install -r requirements.txt --verbose

CMD ["python3", "main.py"]