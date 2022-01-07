# Could use distroless but Snyk found 23 issues
FROM python:3-alpine
LABEL 'org.opencontainers.image.authors'="Rafal Zeidler"
LABEL 'org.opencontainers.image.version'="0.1.0"
ARG DIR='http-api'

EXPOSE 5000

COPY ${DIR}/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt && \
    apk --no-cache add shadow=4.8.1-r1 && \
    rm -rf /var/cache/apk/* && \
    groupadd -r app && \
    useradd -g app -d /app -s /sbin/nologin app

USER app

COPY ${DIR}/app.py /app/app.py
COPY ${DIR}/payload.py /app/payload.py

WORKDIR /app
CMD ["python", "app.py"]
