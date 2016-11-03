FROM python:2

ENV trac_version=cf0b57499eb658fdb7430311f3e08f814b538c49

# https://trac.edgewall.org/browser/trunk/INSTALL.rst
RUN easy_install \
  Genshi \
  pytz \
  Babel \
  docutils \
  Pygments \
  MySQL-python==1.2.5

RUN cd /usr/src && \
  curl -sL https://codeload.github.com/edgewall/trac/tar.gz/$trac_version | tar xvz && \
  cd trac-$trac_version/ && \
  python ./setup.py install && \
  cd .. && \
  rm -Rf trac-$trac_version/
