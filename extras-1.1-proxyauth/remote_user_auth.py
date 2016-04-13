from trac.core import *
from trac.config import BoolOption
from trac.web.api import IAuthenticator
import re

class MyRemoteUserAuthenticator(Component):

    implements(IAuthenticator)

    auth_header = Option('trac', 'remote_user_auth_header', '',
               """Trust this HTTP header for login""")

    # trac's permission system, at least in 1.1, bails out on @ in username
    authmail = re.compile(r'^(.)[^\.]*\.([^@]*).*$', re.IGNORECASE)

    def authenticate(self, req):
        if self.auth_header and req.get_header(self.auth_header):
            account = req.get_header(self.auth_header)
            tracsafe = self.authmail.sub('\\1\\2',account)
            if not tracsafe:
                return account
            return tracsafe
        return None
