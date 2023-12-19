import os
from selene import browser, have, be, command


class StudentRegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")

    def fill_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, param):
        browser.element("#lastName").type(param)

    def fill_email(self, param):
        browser.element("#userEmail").type(param)

    def choose_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element("..").click()

    def fill_phone_nubmer(self, param):
        browser.element("#userNumber").type(param)

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.all(".react-datepicker__year-select>option").element_by(have.text(year)).click()
        browser.all(".react-datepicker__month-select").element_by(have.text(month)).click()
        browser.all(".react-datepicker__day").element_by(have.text(day)).click()

    def fill_subjects(self, *subject):
        browser.element("#subjectsInput").click().send_keys(subject)
        browser.element("#react-select-2-option-0").click()

    def choose_hobbie(self, param):
        browser.element(f"//*[text()='{param}']/parent::*").click()

    def upload_picture(self):
        (browser.element("#uploadPicture").perform(command.js.scroll_into_view)
         .send_keys(os.path.abspath("../tests/pictures/pepe.jpeg")))

    def scroll(self):
        browser.execute_script("window.scrollTo(0,500)")

    def fill_current_address(self, adress):
        browser.element("#currentAddress").type(adress)

    def choose_state_old(self):
        browser.element("#state").click()
        browser.element("#react-select-3-option-0").should(be.visible).click()
        browser.element("#city").click()
        browser.element("#react-select-4-option-0").click()

    def choose_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    def choose_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()

    def submit_form(self):
        browser.element("#submit").press_enter()

    def close_large_modal(self):
        browser.element("#closeLargeModal").press_enter()

    def close_tab(self):
        browser.element("[data-testid=ClearIcon]").click()

    def should_regitered_with(self):
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

    def should_registered_user_with(self, full_name, email, gender,
                                    phone, date, subjects, hobbies,
                                    picture, address, state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date,
                subjects,
                hobbies,
                picture,
                address,
                state_city,
            )
        )
        return self

    def read_modal_header(self):
        return browser.element(".modal-header")



