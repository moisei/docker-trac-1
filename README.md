

## Base image `solsson/trac-single`

```
docker run -p 80:80 -v $(PWD)/trac-env-1:/trac -d --name trac solsson/trac-single
# If you didn't mount an existing env
docker exec -ti trac trac-admin /trac initenv
```
