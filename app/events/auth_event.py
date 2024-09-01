from app.database.main import EnumE
from app.log import LOG


class LoginEvent:
    class ActionType(EnumE):
        success = 0
        failed = 1
        disabled_login = 2
        not_activated = 3

    class Source(EnumE):
        web = 0
        api = 1

    def __init__(self, action: ActionType, source: Source = Source.web):
        self.action = action
        self.source = source

    def send(self):
        LOG.d("LoginEvent: Action=%s, Source=%s", self.action, self.source)
