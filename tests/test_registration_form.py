from data import users
from pages.registration_page import RegistrationPage


def test_student_registration_form(browser_init, test_user = users.admin):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill(test_user)
    registration_page.submit()
    registration_page.should_registered_user_with(test_user)
