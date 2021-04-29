import pytest
from skpy import Skype

from dialogs.absent_office import AbsentOffice


@pytest.fixture()
def skype_connect():
    sk = Skype('chatbottestqa@gmail.com', '9TcisuIv', '_token.txt')
    return sk


@pytest.fixture()
def create_chat(skype_connect):
    ch = skype_connect.chats.create(members=('4616742d-0abe-4a74-a951-ae547424add6', 'live:.cid.f000db266a490222'))
    yield ch
    # delete chat


@pytest.fixture()
def absent_office(create_chat):
    chat = create_chat
    work_from_home_dialog = AbsentOffice(chat)
    work_from_home_dialog.open()
    return work_from_home_dialog
