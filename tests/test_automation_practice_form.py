from selene import have
from pages.automation_practice_form import StudentRegistrationPage


def test_demoqa():
    registration = StudentRegistrationPage()

    registration.open()
    registration.fill_name("Kek")
    registration.fill_last_name("Cheburek")
    registration.fill_email("kekovich@mail.ru")
    registration.choose_gender('Female')
    registration.fill_phone_nubmer(8985123456)
    registration.fill_date_of_birth('1990', 'March', '10')
    registration.fill_subjects('Maths')
    registration.choose_hobbie('Reading')
    registration.upload_picture('pepe.jpeg')
    registration.fill_current_address('omsk')
    registration.choose_state('NCR')
    registration.choose_city('Delhi')
    registration.submit_form()
    registration.read_modal_header.should(have.text("Thanks for submitting the form"))
    registration.should_registered_user_with('Kek Cheburek',
                                             'kekovich@mail.ru',
                                             'Female',
                                             '8985123456',
                                             '10 March,1990',
                                             'Maths',
                                             'Reading',
                                             'pepe.jpeg',
                                             'omsk',
                                             'NCR Delhi'
                                             )
