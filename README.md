# http-api

Example application with Docker image, Helm chart and Kubernetes deployment.

Note: Because it's an example project, I won't use WSGI production-ready server to run Flask application. To check available WSGI servers please refer to: https://flask.palletsprojects.com/en/2.0.x/deploying/

## Application

The application is created in Flask (python framework). It serves HTTP API endpoint with sample data from https://jsonplaceholder.typicode.com/users.

Requirements:
Python3

### HTTP endpoints

Get all users data:

```sh
/api/v1/users/all
```

Get user by ID:

```sh
/api/v1/users?id=<id>
```

### How to run application

To run application locally, you have to create virtual environment, install requirements and start flask application:

Prepare virtual environment:

```sh
cd ./http-api
python3 -m venv venv
. venv/bin/activate
python3 -m pip install -r requirements.txt
```

Run application locally:

```sh
python3 ./http-api/app.py
```

### Docker image

You can easly build and run application in docker by typing the following commands:

```sh
docker build --tag http-api:latest .
docker run -d --name http-api:latest
```

The image is also available on Dockerhub:

```sh
docker pull rafzei/http-api:latest
```

## Monitoring

In addition, you could use provided docker-compose file. It contains Prometheus and Grafana image definitions. In `./configs` directory you can find config files for both, as well as Grafana dashboard.

The Flask application exposes its metrics on `/metrics` endpoint. Example:

```sh
<url>:5000/metrics
```

To reach provided Grafana dashboard:

```sh
<ulr>:3000/d/app/flask-app
```

## Helm

### Helm chart

To run a chart execute the following command:

```sh
helm helm upgrade --install http-api --namespace http-api --create-namespace ./http-api/
```

Note: To be able to run ingress on minikube, enable addon:

```sh
minikube addons enable ingress
```

For details see [the official documentation](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/)

### Helm hook

### Helm test

Please, refer to: [docs/tests](docs/tests.md)

## Kubernetes

### Open-policy-agent (OPA)
