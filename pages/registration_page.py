from selene import browser, be, by, command, have

from qa_guru_selene_homework_10 import resource


class RegistrationPage:

    def open(self):
        return browser.open(f'/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

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

    def fill_hobbies(self, param):
        browser.element('#hobbies-checkbox-2').perform(command.js.scroll_into_view)
        browser.all('.custom-checkbox').element_by(have.exact_text(param)).click()

    def fill_image(self, value):
        browser.element('#uploadPicture').send_keys(resource.path(value))

    def fill_address(self, value):
        browser.element('#currentAddress').click().type(value)

    def fill_city(self, state, city):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()

    def click_button(self):
        browser.element('#submit').execute_script('element.click()')

    def should_regestered_user_with(self, name, email, gender, phone, birthday, subjects, hobbies, file, address,
                                    state):
        browser.element('.table').all('tr td:nth-child(2)').should(
            have.texts(name, email, gender, phone, birthday, subjects, hobbies, file, address, state))
