FROM python:2

RUN easy_install Trac


RUN wget http://opensource.wandisco.com/wandisco-debian.gpg -O /tmp/wandisco-debian.gpg
RUN apt-key add /tmp/wandisco-debian.gpg
RUN echo "deb http://opensource.wandisco.com/debian/ jessie svn19" > /etc/apt/sources.list.d/wandisco.sources.list
RUN dpkg --remove subversion && \
	dpkg --purge subversion
RUN apt-get update && \
	apt-get install subversion subversion-tools -y

EXPOSE 80

ENTRYPOINT ["tracd"]
CMD ["-s", "/trac"]
