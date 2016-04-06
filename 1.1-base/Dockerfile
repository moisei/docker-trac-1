FROM python:2

ENV trac_version=1.1.6

# https://trac.edgewall.org/browser/trunk/INSTALL.rst
RUN easy_install \
  Genshi \
  pytz \
  Babel \
  docutils \
  Pygments

RUN cd /usr/src && \
  curl -sL http://download.edgewall.org/trac/Trac-$trac_version.tar.gz | tar xvz && \
  cd Trac-$trac_version/ && \
  python ./setup.py install && \
  cd .. && \
  rm -Rf Trac-$trac_version/
