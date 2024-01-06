import allure

from demoqa_tests.data import users
from demoqa_tests.steps.automation_practice_form_steps import StudentRegistrationSteps


@allure.title("Successful fill form")
def test_fill_form_demoqa():
    registration_page = StudentRegistrationSteps()

    with allure.step("Open registrations form"):
        registration_page.open()
    with allure.step("Fill form"):
        registration_page.register(users.man)
    with allure.step("Check form results"):
        registration_page.should_have_registered(users.man)
