from selene import browser, have, command
from utils import resource_path


class StudentRegistrationPage:
    def __init__(self):
        self.browser_page = "https://demoqa.com/automation-practice-form"
        self.name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender = browser.all('[name=gender]')
        self.phone_number = browser.element("#userNumber")

        self.date_of_birth_field = browser.element("#dateOfBirthInput")
        self.b_year = browser.all(".react-datepicker__year-select>option")
        self.b_month = browser.all(".react-datepicker__month-select>option")
        self.b_day = browser.all(".react-datepicker__day")

        self.picture = browser.element("#uploadPicture")
        self.subject = browser.element("#subjectsInput")
        self.current_address = browser.element("#currentAddress")
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element("#submit")
        self.modal_table = browser.element('.table')
        self.hobbies = browser.all('[for^=hobbies-checkbox]')

    def open(self):
        browser.open("/automation-practice-form")

    def fill_name(self, value):
        self.name.type(value)

    def fill_last_name(self, param):
        self.last_name.type(param)

    def fill_email(self, param):
        self.email.type(param)

    def choose_gender(self, value):
        self.gender.element_by(have.value(value)).element("..").click()

    def fill_phone_nubmer(self, param):
        self.phone_number.type(param)

    def fill_date_of_birth(self):
        self.date_of_birth_field.click()

    def fill_birth_year(self, year):
        self.b_year.element_by(have.text(year)).click()

    def fill_birth_month(self, month):
        self.b_month.element_by(have.text(month)).click()

    def fill_birth_day(self, day):
        self.b_day.element_by(have.text(day)).click()

    def fill_subjects(self, *subject):
        self.subject.click().send_keys(subject)
        browser.element("#react-select-2-option-0").click()

    def choose_hobbie(self, hobbie):
        self.hobbies.element_by(have.text(hobbie)).click()

    def upload_picture(self, name):
        self.picture.perform(command.js.scroll_into_view).send_keys(resource_path.path(name))

    def fill_current_address(self, address):
        self.current_address.type(address)

    def choose_state(self, state):
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    def choose_city(self, city):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city)
        ).click()

    def submit_form(self):
        self.submit_button.press_enter()

    def should_registered_user_with(self,
                                    full_name,
                                    email,
                                    gender,
                                    phone,
                                    date,
                                    subjects,
                                    hobbies,
                                    picture,
                                    address,
                                    state_city):
        self.modal_table.all('td').even.should(
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
                state_city
            )
        )
        return self

    @property
    def read_modal_header(self):
        return browser.element(".modal-header")
