FROM python:2

ENV trac_version=trunk

# https://trac.edgewall.org/browser/trunk/INSTALL.rst
RUN easy_install \
  Genshi \
  pytz \
  Babel \
  docutils \
  Pygments

RUN cd /usr/src && \
  curl -sL https://github.com/edgewall/trac/archive/$trac_version.tar.gz | tar xvz && \
  cd trac-$trac_version/ && \
  python ./setup.py install && \
  cd .. && \
  rm -Rf trac-$trac_version/
