FROM python:2

ENV trac_version=1.0.10

RUN easy_install Trac==$trac_version

VOLUME /trac

EXPOSE 80

ENTRYPOINT ["tracd", "-s", "/trac"]
