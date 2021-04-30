from dialogs.base_dialog import BaseDialog


class AbsentOffice(BaseDialog):

    def open(self):
        # send Отсутствие в офисе
        raw_text = '#notInOfficeMenu'
        self.send_command_to_alf(raw_text)

    def open_work_from_home_application(self):
        # send Заявка на работу из дома
        raw_text = '#workfromhomemenu'
        self.send_command_to_alf(raw_text)

    def start_application(self):
        # send Оформить заявку
        raw_text = '#workfromhomesimple'
        self.send_command_to_alf(raw_text)

    def add_data_from_and_data_to(self, data_from, data_to):
        # join dates
        period = f'{data_from}-{data_to}'
        # send data period
        self.send_command_to_alf(period)

    def check_incorrect_period_messages(self, data_from, data_to):
        # data
        count_days = self.get_count_days(data_from, data_to)
        max_count_days_text_expected = 'К сожалению, максимальное количество календарных дней работы из дому - 14. '
        incorrect_count_days_text_expected = \
            f'В выбранном Вами периоде {data_from} - {data_to} количество календарных дней - {count_days}'
        # check
        messages_text_list = self.get_text_from_message_card_objects()
        # get text for need message and split this text by lines
        text_list = messages_text_list[1].split('\n')
        # verify these lines to except patterns
        assert max_count_days_text_expected == text_list[0]
        assert incorrect_count_days_text_expected == text_list[1]

    def get_text_from_message_card_objects(self):
        # get all messages from chat
        messages = self.chat.getMsgs()
        # get messages only SkypeCardMsg type
        messages_card = []
        [messages_card.append(message) for message in messages if hasattr(message, 'buttons')]
        # get body values from messages(it is text value)
        messages_text_list = list(map(lambda i: i.body, messages_card))
        return messages_text_list
