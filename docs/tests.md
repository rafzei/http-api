# Tests and scans documentation

## Docker image - Snyk scan

Docker image was scanned by Snyk:

```sh
docker scan http-api:latest
```

output:

```sh
Package manager:   apk
Project name:      docker-image|http-api
Docker image:      http-api
Platform:          linux/amd64
Base image:        python:3.10.1-alpine3.15
Licenses:          enabled

✔ Tested 37 dependencies for known issues, no vulnerable paths found.

According to our scan, you are currently using the most secure version of the selected base image
```

## Docker image - container-structure-test

Docker image tested by container-structure-test:

```sh
container-structure-test test --image http-api:latest --config tests/container.yml
```

output:

```sh
======================================
====== Test file: container.yml ======
======================================
=== RUN: Command Test: Check python
--- PASS
duration: 757.87055ms
stdout: Python 3.10.1

=== RUN: File Existence Test: /app/app.py
--- PASS
duration: 0s
=== RUN: File Existence Test: /app/payload.py
--- PASS
duration: 0s
=== RUN: File Existence Test: /app/requirements.txt
--- PASS
duration: 0s
=== RUN: Metadata Test
--- PASS
duration: 0s

=======================================
=============== RESULTS ===============
=======================================
Passes:      5
Failures:    0
Duration:    757.87055ms
Total tests: 5
```


## Helm test

To run Helm test, execute:

```sh
helm test -n http-api http-api
```
where `-n http-api` pointing to the namespace.

output:

```sh
NAME: http-api
LAST DEPLOYED: Fri Jan  7 18:02:22 2022
NAMESPACE: http-api
STATUS: deployed
REVISION: 9
TEST SUITE:     http-api-test-connection
Last Started:   Fri Jan  7 18:05:49 2022
Last Completed: Fri Jan  7 18:05:58 2022
Phase:          Succeeded
```
