from selene import browser, have
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

    browser.element(".modal-header").should(have.text("Thanks for submitting the form"))
    browser.element(".modal-body").should(have.exact_text(
        'Label Values\n' 
        'Student Name Kek Cheburek\n' 
        'Student Email kekovich@mail.ru\n' 
        'Gender Female\n' 
        'Mobile 8985123456\n' 
        'Date of Birth 10 December,1990\n' 
        'Subjects Maths\n' 
        'Hobbies Reading\n' 
        'Picture pepe.jpeg\n' 
        'Address omsk\n' 
        'State and City NCR Delhi'
    ))
