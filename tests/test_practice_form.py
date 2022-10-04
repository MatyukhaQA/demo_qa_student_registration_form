import os.path
from selene.support.shared import browser
from selene import have
import allure
from allure_commons.types import Severity

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'matyukha')
@allure.feature('Student Registration Form')
@allure.story('Filling form of registration')
@allure.link('demoqa.com')

def test_student_registration_form():
    with allure.step("Open registrations form"):
        browser.open('https://demoqa.com/automation-practice-form')
    with allure.step('Fill form'):
        browser.element('#firstName').type('Albert')
        browser.element('#lastName').type('Morcerf')
        browser.element('#userEmail').type('AlbertMorcerf@gmail.com')
        browser.element('#gender-radio-1').double_click()
        browser.element('#userNumber').type('9998887766')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('March')
        browser.element('.react-datepicker__year-select').type('1990')
        browser.element('[aria-label = "Choose Thursday, March 8th, 1990"]').click()
        browser.element('#subjectsInput').type('English').press_enter()
        browser.element("label[for='hobbies-checkbox-2']").click()
        browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/pic.jpg'))
        browser.element('#currentAddress').type('New Delhi')
        browser.element('#state').click()
        browser.element('#state input').type('NCR').press_enter()
        browser.element('#city').click()
        browser.element('#city input').type('Delhi').press_enter()
        browser.element('#submit').press_enter()
    with allure.step('Check result'):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table-responsive').should(have.text('Albert Morcerf'))
        browser.element('.table-responsive').should(have.text('AlbertMorcerf@gmail.com'))
        browser.element('.table-responsive').should(have.text('Male'))
        browser.element('.table-responsive').should(have.text('9998887766'))
        browser.element('.table-responsive').should(have.text('8 March,1990'))
        browser.element('.table-responsive').should(have.text('English'))
        browser.element('.table-responsive').should(have.text('Reading'))
        browser.element('.table-responsive').should(have.text('pic.jpg'))
        browser.element('.table-responsive').should(have.text('New Delhi'))
        browser.element('.table-responsive').should(have.text('NCR Delhi'))