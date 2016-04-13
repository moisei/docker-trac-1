from trac.core import *
from trac.config import BoolOption
from trac.web.api import IAuthenticator

class MyRemoteUserAuthenticator(Component):

    implements(IAuthenticator)

    auth_header = Option('trac', 'remote_user_auth_header', '',
               """Trust this HTTP header for login""")

    def authenticate(self, req):
        if self.auth_header and req.get_header(self.auth_header):
            return req.get_header(self.auth_header)
        return None
