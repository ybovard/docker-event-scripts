FROM alpine:latest

RUN apk update && apk upgrade && \
    apk add python3 && pip3 install --upgrade pip && \
    pip3 install docker-event-scripts && \
    mkdir -p /etc/docker/events.d

ENTRYPOINT /usr/bin/des
