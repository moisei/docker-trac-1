
# Trac as microservice

See https://trac.edgewall.org/

## Base image `solsson/trac-single`

```
docker run -p 80:80 -v $(PWD)/trac-env-1:/trac -d --name trac solsson/trac:single
# If you didn't mount an existing env
docker exec -ti trac trac-admin /trac initenv
```

## Geared towards ticketing over JSON-RPC

We might some day make this image slimmer, remove wiki and VCS stuff for example.

```
docker run -p 80:80 -v $(PWD)/trac-env-1:/trac -d --name trac solsson/trac:ticket-engine
# If you didn't enable rpc in your env already
docker exec -ti trac trac-admin /trac config set components tracrpc.* enabled
# You may want "authenticated" here instead of "anonymous"
docker exec -ti trac trac-admin /trac permission add anonymous XML_RPC
# ok?
curl -s http://$(docker-machine ip default)/login/rpc -H "Accept: text/html" | grep "Installed API version"
```
