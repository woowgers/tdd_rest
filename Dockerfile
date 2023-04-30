FROM python:3.11-alpine

ARG UID=1000
ARG GID=1000

WORKDIR /app

RUN addgroup -g ${GID} -S python &&\
    adduser -u ${UID} -SG python python

USER python
