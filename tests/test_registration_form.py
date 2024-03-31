from selene.support.shared import browser
from selene import be, have, command

from data.users import User
from pages.registration_page import RegistrationPage


def test_student_registration_form(browser_init):
    registration_page = RegistrationPage()
    test_user = User(
        first_name="Марина",
        last_name="Темирханова",
        email='blabla@bla.bla',
        gender='Female',
        phone='9999999999',
        year='1992',
        month='December',
        day='1',
        subjects='Maths',
        hobbies='[for="hobbies-checkbox-2"]',
        file='img.jpg',
        address='Moscow Leninskiy av. 120',
        state='NCR',
        city='Delhi'
    )
    registration_page.fill_full_name(test_user.first_name, test_user.last_name)
    registration_page.fill_email(test_user.email)
    registration_page.fill_gender(test_user.gender)
    registration_page.fill_phone(test_user.phone)
    registration_page.fill_birthday(test_user.year, test_user.month, test_user.day)
    registration_page.fill_subjects(test_user.subjects)
    registration_page.fill_hobbies(test_user.hobbies)
    registration_page.fill_image(test_user.file)
    registration_page.fill_address(test_user.address)
    registration_page.fill_state(test_user.state, test_user.city)
    registration_page.click_button()
    registration_page.should_regestered_user_with(
        'Марина Темирханова',
        'blabla@bla.bla',
        'Female',
        '9999999999',
        '01 December,1992',
        'Maths',
        'Reading',
        'img.jpg',
        'Moscow Leninskiy av. 120',
        'NCR Delhi'

        # test_user.first_name + test_user.last_name,
        # test_user.email,
        # test_user.gender,
        # test_user.phone,
        # test_user.day + test_user.month + test_user.year,
        # test_user.subjects,
        # test_user.hobbies,
        # test_user.file,
        # test_user.address,
        # test_user.state + test_user.city
    )
