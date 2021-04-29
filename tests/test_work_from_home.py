import time


def test_exceeding_permissible_value_dates(absent_office):
    absent_office.open_work_from_home_application()
    absent_office.start_application()
    time.sleep(5)
    absent_office.add_data_from_and_data_to()
    absent_office.check_max_day_aplication()


    pass
