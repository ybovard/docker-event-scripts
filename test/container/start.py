#!/bin/python

import docker
import os
import requests


def updateDNS(container):
  if 'DNSintern' in container['Labels']:
    d = {'a': '127.0.0.1', 'aaaa': '::1'}
    requests.put('https://'+os.environ['ETCD_ADDR']+'2379/v2/keys/ch/ybovard/intern/'+container['Labels']['DNSintern'], data = d, verify='/etc/ssl/etcd/full_chain.crt', cert=('/etc/ssl/etcd/ssl.crt', '/etc/ssl/etcd/ssl.key'))


def getContainer(idx):
  cli=docker.from_env()
  for container in cli.containers():
    if container['Id'] == idx:
      return container
  return None
    

if 'ID' in os.environ:
  container=getContainer(os.environ['ID'])
  if container is not None:
    with open('/etc/docker/events.d/data/toto', 'a') as ptr:
      ptr.write(str(container))

    got=updateDNS(container)
