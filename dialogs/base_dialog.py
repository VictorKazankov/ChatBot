import time
from datetime import datetime, timedelta

from data.alf import Alf


class BaseDialog:

    def __init__(self, chat):
        self.chat = chat

    def send_command_to_alf(self, text):
        message = f'<at id="28:{Alf.dev["id"]}">{Alf.dev["skype_name"]}</at> {text}'
        self.chat.sendMsg(message, rich=True)
        time.sleep(5)

    def get_count_days(self, data_from, data_to):
        d1 = datetime.strptime(data_to, "%d/%m/%Y")
        d2 = datetime.strptime(data_from, "%d/%m/%Y")
        # +1 day for correct calculation of period
        d1 = d1 + timedelta(days=1)
        return str(abs((d2 - d1).days))
