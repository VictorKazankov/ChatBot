def test_add_incorrect_date_period(absent_office):
    user_data_from = '1/6/2021'
    user_data_to = '20/6/2021'
    absent_office.open_work_from_home_application()
    absent_office.start_application()
    absent_office.add_data_from_and_data_to(user_data_from, user_data_to)
    absent_office.check_incorrect_period_messages(user_data_from, user_data_to)
