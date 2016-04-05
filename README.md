
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
docker run -p 80:80 -v $(PWD)/trac-env-1:/trac -d --name trac solsson/trac:engine
# If you didn't enable rpc in your env already
docker exec -ti trac trac-admin /trac config set components tracrpc.* enabled
# You may want "authenticated" here instead of "anonymous"
docker exec -ti trac trac-admin /trac permission add anonymous XML_RPC
# ok?
curl -s http://$(docker-machine ip default)/jsonrpc -H "Accept: text/html" | grep "Installed API version"
```

## Development version

```
docker build -t solsson/trac:1.2-base 1.2-base/
docker build -t solsson/trac:1.2-single single-1.2/
docker build -t solsson/trac:1.2-engine engine-1.2/
docker run -p 80:80 -v $(PWD)/trac-env-2:/trac -d --name trac solsson/trac:1.2-engine
# let everyone do everything
docker exec -ti trac trac-admin /trac permission add anonymous TICKET_ADMIN
```
