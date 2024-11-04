from app.database.models import EnumE
from app.log import LOG


class LoginEvent:
    class ActionType(EnumE):
        success = 0
        failed = 1
        disabled_login = 2
        not_activated = 3
        email_not_verified = 4

    class Source(EnumE):
        web = 0
        api = 1

    def __init__(self, action: ActionType, source: Source = Source.web):
        self.action = action
        self.source = source

    def send(self):
        LOG.d("LoginEvent: Action=%s, Source=%s", self.action.name, self.source.name)


class RegisterEvent:
    class ActionType(EnumE):
        success = 0
        failed = 1
        invalid_email = 2
        captcha_failed = 3

    class Source(EnumE):
        web = 0
        api = 1

    def __init__(self, action: ActionType, source: Source = Source.web):
        self.action = action
        self.source = source

    def send(self):
        LOG.d("RegisterEvent: Action=%s, Source=%s", self.action.name, self.source.name)
