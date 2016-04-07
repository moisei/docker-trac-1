
# Trac as microservice

See https://trac.edgewall.org/.

Trac lends itself nicely to configuration after launch. It refreshes at reload, so there's no need to prepare an "env" beforehand. Instead run [trac-admin](https://trac.edgewall.org/wiki/TracAdmin) over [docker exec](https://docs.docker.com/engine/reference/commandline/exec/) / [docker-compose run](https://docs.docker.com/compose/reference/run/) / [kubectl exec](http://kubernetes.io/docs/user-guide/kubectl/kubectl_exec/).

Regarding trac versions, 1.0 is considered latest stable. But we've been running 1.1 since long with no issues. We like the `time` field type and there is progress, albeit slow, towards a more mobile-friendly UI.

## Base image `solsson/trac-single`

```
docker run -p 80:80 -v $(PWD)/trac-env-1:/trac -d --name trac solsson/trac:single
# If you didn't mount an existing env
docker exec -ti trac trac-admin /trac initenv

# You may have mounted a volume, say /git, with your repositories
docker exec trac trac-admin /trac config set components tracopt.versioncontrol.git.* enabled
docker exec trac trac-admin /trac repository add Testing/repo1 /git/Testing/repo1.git git
```

## Geared towards ticketing over JSON-RPC

We might some day make this image slimmer, for example remove wiki and VCS stuff.

```
docker run -p 80:80 -v $(PWD)/trac-env-1:/trac -d --name trac solsson/trac:engine
# If you didn't enable rpc in your env already
docker exec trac trac-admin /trac config set components tracrpc.* enabled
# You may want "authenticated" here instead of "anonymous"
docker exec trac trac-admin /trac permission add anonymous XML_RPC
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
docker exec trac trac-admin /trac permission add anonymous TICKET_ADMIN
```

## Additional plugins

The `solsson/trac:1.1-extras` image is an example of a Dockerfile that adds plugins from trac-hacks. This isn't something you'd want to do after container launch. What you do want to do per environment is to run trac-admin:

```
docker exec trac trac-admin /trac config set components tractoc.* enabled
docker exec trac trac-admin /trac config set components Markdown.* enabled
# ... and so on

# If command based admin isn't enough...
docker exec trac trac-admin /trac permission add authenticated TRAC_ADMIN
# or even
docker exec trac trac-admin /trac permission add anonymous TRAC_ADMIN
```
