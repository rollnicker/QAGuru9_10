from demoqa_tests.data import users
from demoqa_tests.steps.automation_practice_form_steps import StudentRegistrationSteps


def test_demoqa_steps():
    registration_page = StudentRegistrationSteps()

    registration_page.open()
    registration_page.register(users.man)
    registration_page.should_have_registered(users.man)
