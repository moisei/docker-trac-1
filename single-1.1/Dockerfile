FROM solsson/trac:1.1-base

# Don't declare a volume because it prevents downstream images from pre-initializing an env
#VOLUME /trac

EXPOSE 80

ENTRYPOINT ["tracd"]
CMD ["-s", "/trac"]
