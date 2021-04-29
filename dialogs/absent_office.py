from dialogs.base_dialog import BaseDialog


class AbsentOffice(BaseDialog):
    alf_id = '4616742d-0abe-4a74-a951-ae547424add6'
    alf_name = 'ALF_development'

    def open(self):
        raw_text = '#notInOfficeMenu'
        message = f'<at id="28:{self.alf_id}">{self.alf_name}</at> {raw_text}'
        self.alf.sendMsg(message, rich=True)

    def open_work_from_home_application(self):
        raw_text = '#workfromhomemenu'
        message = f'<at id="28:{self.alf_id}">{self.alf_name}</at> {raw_text}'
        self.alf.sendMsg(message, rich=True)

    def start_application(self):
        raw_text = '#workfromhomesimple'
        message = f'<at id="28:{self.alf_id}">{self.alf_name}</at> {raw_text}'
        self.alf.sendMsg(message, rich=True)

    def add_data_from_and_data_to(self):
        data_from_to = '01/06/2021-20/06/2021'
        message = f'<at id="28:{self.alf_id}">{self.alf_name}</at> {data_from_to}'
        self.alf.sendMsg(message, rich=True)

    def check_max_day_application(self):
        pass
    pass
