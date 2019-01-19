# Introduction
This is just an integration of https://github.com/colebrumley/des into a docker container.

Thanks a lot https://github.com/colebrumley !!!!

# Usage
```
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v docker-events.d:/etc/docker/events.d des -v
```
