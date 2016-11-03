FROM python:2

ENV trac_version=1.0.13

RUN easy_install Trac==$trac_version MySQL-python==1.2.5

# Don't declare a volume because it prevents downstream images from pre-initializing an env
#VOLUME /trac

EXPOSE 80

ENTRYPOINT ["tracd"]
CMD ["-s", "/trac"]
