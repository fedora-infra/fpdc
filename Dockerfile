FROM registry.fedoraproject.org/fedora:28

WORKDIR /code
ADD requirements.txt /tmp
RUN dnf -y install postgresql\
    && dnf clean all\
    && pip3 install -r /tmp/requirements.txt
