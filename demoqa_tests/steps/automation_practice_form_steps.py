from selene import browser
from demoqa_tests.pages.registration_page import StudentRegistrationPage


class StudentRegistrationSteps:
    def __init__(self):
        self.page = StudentRegistrationPage()

    def open(self):
        browser.open(self.page.browser_page)

    def register(self, user):
        self.page.fill_name(user.first_name)
        self.page.fill_last_name(user.last_name)
        self.page.fill_email(user.email)
        self.page.choose_gender(user.gender)
        self.page.fill_phone_nubmer(user.mobile)
        self.page.fill_date_of_birth()
        self.page.fill_birth_year(user.year_of_birth)
        self.page.fill_birth_month(user.month_of_birth)
        self.page.fill_birth_day(user.day_of_birth)
        self.page.fill_subjects(user.subjects)
        self.page.choose_hobbie(user.hobbies)
        self.page.upload_picture(user.picture)
        self.page.fill_current_address(user.address)
        self.page.choose_state(user.state)
        self.page.choose_city(user.city)
        self.page.submit_form()

    def should_have_registered(self, user):
        self.page.should_registered_user_with(full_name=user.first_name + " " + user.last_name,
                                              email=user.email,
                                              gender=user.gender,
                                              phone=user.mobile,
                                              subjects=user.subjects,
                                              hobbies=user.hobbies,
                                              date=f"{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}",
                                              address=user.address,
                                              picture=user.picture,
                                              state_city=f"{user.state} {user.city}"
                                              )
