import time

from skpy import Skype, SkypeMsg


def test_skpy():
    sk = Skype('chatbottestqa@gmail.com', '9TcisuIv', '_token.txt')  # connect to Skype

    #sk.user  # you
    con = sk.contacts  # your contacts
    sk.chats  # your conversations
    ch = sk.chats.create(members=('4616742d-0abe-4a74-a951-ae547424add6', 'live:.cid.f000db266a490222'))
    #ch = sk.chats["19:4616742d-0abe-4a74-a951-ae547424add6"]
    ch.setAlerts(False)

    # ch = sk.chats.create(['ALF-my_robot'])  # new group conversation
    # ch = sk.contacts["joe.4"].chat  # 1-to-1 conversation

    a = ch.sendMsg("Privet grebanu bot")  # plain-text message
    # ch.sendFile(open("song.mp3", "rb"), "song.mp3")  # file upload
    # ch.sendContact(sk.contacts["daisy.5"])  # contact sharing
    time.sleep(3)
    c = ch.getMsgs()  # retrieve recent messages
    button_list = []
    for i in c:
        if hasattr(i, 'buttons'):
            button_list.append(i)
    pass
    time.sleep(1)
    n = button_list[0].buttons[0].title
    #buttons = list(map(lambda i: c.buttons.text, c))
    time.sleep(3)
    alf_id = '4616742d-0abe-4a74-a951-ae547424add6'
    alf_name = 'ALF_development'
    raw_text = '#notInOfficeMenu'
    raw_text2 = '#workfromhomemenu'
    raw_text3 = '#workfromhomesimple'
    raw_text4 = '01/06/2021-20/06/2021'
    # message = f'<at id="28:{alf_id}">{alf_name}</at> {raw_text}'
    # ch.sendMsg(message, rich=True)
    # message2 = f'<at id="28:{alf_id}">{alf_name}</at> {raw_text2}'
    # time.sleep(3)
    # ch.sendMsg(message2, rich=True)
    message3 = f'<at id="28:{alf_id}">{alf_name}</at> {raw_text3}'
    time.sleep(3)
    ch.sendMsg(message3, rich=True)
    message4 = f'<at id="28:{alf_id}">{alf_name}</at> {raw_text4}'
    time.sleep(4)
    ch.sendMsg(message4, rich=True)
    response_text = ch.getMsgs()
    pass
