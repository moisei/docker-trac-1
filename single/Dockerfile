FROM python:2

ENV trac_version=1.0.13

RUN easy_install Trac==$trac_version MySQL-python==1.2.5

VOLUME /trac

EXPOSE 80

ENTRYPOINT ["tracd", "-s", "/trac"]
