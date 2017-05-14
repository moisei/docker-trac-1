FROM python:2

RUN easy_install Trac

EXPOSE 80

ENTRYPOINT ["tracd"]
CMD ["-s", "/trac"]
