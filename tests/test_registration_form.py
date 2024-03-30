from selene.support.shared import browser
from selene import be, have, command

from pages.registration_page import RegistrationPage


def test_student_registration_form(browser_init):
    registration_page = RegistrationPage()
    # registration_page.open()
    registration_page.fill_first_name("Test")
    registration_page.fill_last_name("Test")
    registration_page.fill_email("test@test.test")
    registration_page.fill_gender('[for="gender-radio-1"]')
    registration_page.fill_phone('9999999999')
    registration_page.fill_birthday('1992', 'December', '1')
    registration_page.fill_subjects('Math')
    registration_page.fill_hobbies('[for="hobbies-checkbox-2"]')
    registration_page.fill_image('img.jpg')


    browser.element('#currentAddress').click().type("Moscow Leninskiy av. 120")
    browser.element('#react-select-3-input').should(be.blank).type('N').press_enter()
    browser.element('#city').should(be.visible)
    browser.element('#react-select-4-input').should(be.blank).type('D').press_enter()
    browser.element('#submit').should(be.visible).press_enter()

    browser.element('#submit').execute_script('element.click()')

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))

    registration_page.regestered_user_data().should(have.texts(
        'Test Test',
        'test@test.test',
        'Male',
        '9999999999',
        '01 December,1992',
        'Maths',
        'Reading',
        'img.jpg',
        'Moscow Leninskiy av. 120',
        'NCR Delhi'
        ))

'''
    registration_page.should_regestered_user_with(
        'Test Test',
        'test@test.test',
        'Male',
        '9999999999',
        '01 December,1992',
        'Maths',
        'Reading',
        'img.jpg',
        'Moscow Leninskiy av. 120',
        'NCR Delhi'
    )
'''