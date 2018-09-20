# Setup the Local Development

fpdc requires Python 3.6.0+ to run. You can setup a local development environment using Python virtual environments.

Create a virtual environment

```
$ python3.6 -m venv .venv
```

Activate the virtual environment

```
$ source .venv/bin/activate
```

First upgrade pip and then install the dependencies

```
(.venv) $ pip install -U pip
(.venv) $ pip install -r requirements-dev.txt
```

### docker-compose environment

A docker-compose environment is available to give access to a development environment
which is close to the production environment.

To start with docker-compose first make sure you have docker installed and running on your system.

```
$ sudo dnf install docker
$ sudo systemctl start docker
```

Then inside your virtual environment install docker-compose.

```
(.venv) $ pip install docker-compose
```

If you do not wish to run docker-compose using sudo you will need to add your user to the docker group as follow.

```
$ sudo groupadd docker && sudo gpasswd -a $USER docker
$ MYGRP=$(id -g) ; newgrp docker ; newgrp $MYGRP
```

Note that this is has for effect to give root permission to users added to the docker group.

Once the installation is complete you can start the docker-compose cluster

```
(.venv) $ docker-compose up
```

You then will see the logs of the django web server and the postgresql database. You can
start the cluster in a daemon mode (ie without displaying the logs) using the `-d`
option.

```
(.venv) $ docker-compose up -d
```

Then to access the logs use :

```
(.venv) $ docker-compose logs web
(.venv) $ docker-compose logs bd

```

Finally you can stop the cluster :

```
(.venv) $ docker-compose stop
```

To clean up the cluster and the database use :

```
(.venv) $ docker-compose down --volumes
```

### Running the tests

You can run the tests with the following command.

```
$ py.test
```

You can also run all the checks (linting, format and licenses) that are validated by the CI pipeline using the tox command.

```
$ tox
```
