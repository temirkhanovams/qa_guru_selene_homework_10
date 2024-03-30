from selene import be, by, command
from selene.support.shared import browser

from qa_guru_selene_homework_10 import resource


class RegistrationPage:
    # def open(self):
    #     print('\nОткрываю браузер')
    #     browser.config.window_width = 1024
    #     browser.config.window_height = 780
    #     browser.open("https://demoqa.com/automation-practice-form")
    #
    #     yield
    #
    #     print('\nЗакрываю браузер')
    #     browser.quit()

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def fill_gender(self, value):
        browser.element(value).click()

    def fill_phone(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(by.text(year)).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(by.text(month)).click()
        browser.element('.react-datepicker__month').click()
        browser.element(by.text(day)).click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    def fill_hobbies(self, value):
        browser.element(value).perform(command.js.scroll_into_view)
        browser.with_(timeout=browser.config.timeout * 3).element(value).click()

    def fill_image(self, value):
        # browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#uploadPicture').send_keys(resource.path(value))

    def regestered_user_data(self):
        return browser.element('.table').all('tr td:nth-child(2)')


    #
    # def should_regestered_user_with(self, name, email, gender, phone, birthday, subjects, hobbies, file, address,
    #                                 state):
    #     browser.element('.table').all('tr td:nth-child(2)').should(have.texts
    #         (
    #         name,
    #         email,
    #         gender,
    #         phone,
    #         birthday,
    #         subjects,
    #         hobbies,
    #         file,
    #         address,
    #         state
    #     ) )
