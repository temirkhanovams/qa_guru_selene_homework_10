from pages.registration_page import RegistrationPage


def test_student_registration_form(browser_init):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Test')
    registration_page.fill_last_name('Test')
    registration_page.fill_email('test@test.test')
    registration_page.fill_gender('Male')
    registration_page.fill_phone('9999999999')
    registration_page.fill_birthday('1992', 'December', '1')
    registration_page.fill_subjects('Math')
    registration_page.fill_hobbies('Reading')
    registration_page.fill_image('img.jpg')
    registration_page.fill_address("Moscow Leninskiy av. 120")
    registration_page.fill_city('NCR', 'Delhi')
    registration_page.click_button()
    registration_page.should_regestered_user_with('Test Test', 'test@test.test', 'Male', '9999999999',
                                                  '01 December,1992', 'Maths', 'Reading', 'img.jpg',
                                                  'Moscow Leninskiy av. 120', 'NCR Delhi')
