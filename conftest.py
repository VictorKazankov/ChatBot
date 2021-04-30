import pytest
from skpy import Skype

from dialogs.absent_office import AbsentOffice
from data.users import Users
from data.alf import Alf


@pytest.fixture()
def skype_connect():
    sk = Skype(Users.test_user_1['email'], Users.test_user_1['password'], '_token.txt')
    return sk


@pytest.fixture()
def create_chat(skype_connect):
    chat = skype_connect.chats.create(members=(Alf.dev['id'], Users.test_user_chak['id']))
    yield chat
    # chat.delete()


@pytest.fixture()
def absent_office(create_chat):
    chat = create_chat
    work_from_home_dialog = AbsentOffice(chat)
    work_from_home_dialog.open()
    return work_from_home_dialog
