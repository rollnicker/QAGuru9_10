from selene import browser, have
from pages.automation_practice_form import StudentRegistrationPage


def test_demoqa():
    registration = StudentRegistrationPage()

    registration.open()
    #When
    registration.fill_name("Kek")
    registration.fill_last_name("Cheburek")
    registration.fill_email("kekovich@mail.ru")
    registration.choose_gender('Female')
    registration.fill_phone_nubmer(8985123456)
    registration.fill_date_of_birth('1990', 'March', '10')
    registration.fill_subjects('Maths')
    registration.choose_hobbie('Reading')
    registration.upload_picture()
    registration.fill_current_address('omsk')
    registration.choose_state('NCR')
    registration.choose_city('Delhi')
    registration.submit_form()
    #Then
    registration.should_have_header()
    registration.should_regitered_with()
    registration.should_registered_user_with('Kek Cheburek',
                                             'vkekovich@mail.ru',
                                             'Female',
                                             8985123456,
                                             '10 December,1990',
                                             'Maths',
                                             'Reading',
                                             'pepe.jpeg',
                                             'omsk',
                                             'NCR Delhi'
                                             )
