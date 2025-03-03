from .auth import Authenticator
import logging

class ServieProvider:
    def __init__(self,auth:Authenticator):
        self.auth = auth
        self.session = auth.session
        self.logger = logging.getLogger(__name__)
    
    def check(self):
        print(f"check:{self.session.cookies.get_dict()}")