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
(.venv) $ oidc-register https://iddev.fedorainfracloud.org/openidc/ http://localhost:12345/ http://localhost:23456/ http://localhost:8000/oidc/callback/
```

You can also use curl if you do not wish to use `oidc-register`

```
(.venv) $ curl --request POST --header "Content-Type: application/json" --data '{"redirect_uris": ["http://localhost:1234", "http://localhost:8000/oidc/callback/"], "application_type": "native", "token_endpoint_auth_method": "client_secret_post"}' https://iddev.fedorainfracloud.org/openidc/Registration
```

Extract the client ID and secret received from the provider (inside the client_secrets.json file) above and export them into the virtual
environment:

```
(.venv) $ export OIDC_RP_CLIENT_ID=...
(.venv) $ export OIDC_RP_CLIENT_SECRET=...
```

### container development environment

A container based environment is available to give access to a development environment
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

To start with this environment first make sure you have podman installed and running on your system.

```
$ sudo dnf install podman
```

Note: The following requires at least podman version 1.0.0

If you are not running fedora you can check how to install podman on your system [here](https://github.com/containers/libpod/blob/master/install.md)

You also need to have GNU make installed

```
$ sudo dnf install make
```

Once the installation is complete you can build the fpdc-web container

```
$ make build
```

After the container finished building, you can start a pod. This will start 2 containers inside the pod, a container running the django application `fpdc-web` and a container runnning a postgresql database `database`

```
$ make up
```

Then to access the logs of the container use:

```
$ make logs-web
$ make logs-db

```

Finally you can stop the pod:

```
$ make stop
```

Start the pod:

```
$ make start
```

Check which containers are running in the pod:

```
$ make ps
```

To brind down the pod:

```
$ make down
```

Clean the database volume:

```
$ make prune
```

You can also get a shell access to the fpdc-web container

```
$ make shell
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

An example of scripts that creates a new release using the OIDC authentication is available under `examples`.

```
$ docker-compose up -d
$ python examples/create_release.py
```

This script will open the browser and ask you to login using you FAS credentials.
