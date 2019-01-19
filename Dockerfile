FROM fedora:latest

WORKDIR /code

ENV PYTHONPATH=/code

ADD requirements.txt /tmp

RUN dnf -y install postgresql\
    && dnf clean all\
    && pip3 install -r /tmp/requirements.txt

ENTRYPOINT ["/code/run-container.sh"]
