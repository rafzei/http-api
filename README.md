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

You can easly build application in docker by typing the following command:

```sh
docker build --tag http-api:latest .
```

The image is also available on Dockerhub:

```sh
docker pull rafzei/http-api:latest
```

To run an application in Docker, execute:

```sh
docker run -ti --name http-api http-api:latest
```

## Monitoring

In addition, you could use provided docker-compose file. It contains Prometheus and Grafana image definitions. In `./configs` directory you can find config files for both, as well as Grafana dashboard.

To run monitoring tools along with application, execute:

```sh
docker-compose up --build
```

The Flask application exposes its metrics on `/metrics` endpoint. Example:

```sh
http://<url>:5000/metrics
```

To reach provided Grafana dashboard:

```sh
http://<url>:3000/d/app/flask-app
```

To get Prometheus GUI:

```sh
http://<url>:9090/graph
```

As `<url>` you could use localhost or container ip address (check it via docker inspect).

## Helm

### Helm chart

To run a chart execute the following command:

```sh
helm helm upgrade --install http-api --namespace http-api --create-namespace ./charts/http-api/
```

Note: To be able to run ingress on minikube, make sure your minikube is in the latest released version and enable addon:

```sh
minikube addons enable ingress
```

For details see [the official documentation](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/)

### Helm hook

I've provided sample Helm hook (job) which can be adjusted and used for migrations between releases.
See [here](charts/http-api/templates/hooks/pre-hook.yaml)

### Helm test

Please, refer to: [docs/tests](docs/tests.md)

## Kubernetes

Because the yaml's are already in the Helm charts, you could use it as `source of true` and generate manifests needed for example by kubectl. Execute the following command:

```sh
helm template http-api ./charts/http-api/ --namespace http-api --create-namespace --output-dir ./kubernetes --no-hooks --skip-tests
```

Because the namespace is created during helm chart execution, you have to provide it mannualy before `kubectl apply -f <file.yml>` execution.

Example:

```sh
kubectl create namespace http-api
```

### Open-policy-agent (OPA)

This part assumes, that you already have OPA user, namespace and rbac created (TODO: Implement in v0.2.0).

Files related to OPA are included in [opa dir](opa/):

- deployment.yaml - deploys OPA in a cluster
- check-container-user.rego - provice policy file to check if user is not privileged
- service.yaml - provide clusterIP service for ingress
- ingress.yaml - provide ingress to reach OPA API

To apply OPA execute the following commands:

```sh
kubectl create configmap check-container-user --from-file ./opa/check-container-user.rego
kubectl apply -f ./opa/deployment.yaml
kubectl apply -f ./opa/service.yaml
kubectl apply -f ./opa/ingress.yaml
```
