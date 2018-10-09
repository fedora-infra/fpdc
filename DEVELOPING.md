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

Get a client ID and secret, if you don't already have one.

```
(.venv) $ curl --request POST --header "Content-Type: application/json" --data '{"redirect_uris": ["http://localhost:1234", "http://localhost:8000/oidc/callback/"], "application_type": "native", "token_endpoint_auth_method": "client_secret_post"}' https://iddev.fedorainfracloud.org/openidc/Registration
```

Extract the client ID and secret received from the provider above and export them into the virtual
environment:

```
(.venv) $ export OIDC_RP_CLIENT_ID=...
(.venv) $ export OIDC_RP_CLIENT_SECRET=...
```

### docker-compose environment

A docker-compose environment is available to give access to a development environment
which is close to the production environment.

In order to use the client ID and secret generated in the previous step, put the ID
and secret into a `.env` file in the project root.

```
$ cat > .env <<EOF
> OIDC_RP_CLIENT_ID=...
> OIDC_RP_CLIENT_SECRET=...
> EOF
$
```

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

# Client examples

### Create a new release

An example of scripts that creates a new release using the OIDC authentication is available under `examples`. To run this example you need to
install `openidc-client`.

```
$ pip install openidc-client
$ docker-compose up -d
$ python examples/create_release.py
$ curl -X GET "http://localhost:8000/api/v1/release" -H  "accept: application/json"
```
