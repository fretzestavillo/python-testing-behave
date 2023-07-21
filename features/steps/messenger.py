from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)


@when('I open messenger')
def step_impl(context):
    context.driver.get("https://www.messenger.com/")


@when('Enter credentials')
def step_impl(context):
    email_input = context.driver.find_element(By.CSS_SELECTOR, 'input[id="email"]')
    password_input = context.driver.find_element(By.CSS_SELECTOR, 'input[id="pass"]')

    # input the credentials on field
    email_input.send_keys("your_email")
    password_input.send_keys("your_password")


@when('clicklogin button')
def step_impl(context):
    login_form = context.driver.find_element(By.CSS_SELECTOR, 'button[name="login"]')
    login_form.click()


@when('go to search bar and enter name of your friend')
def step_impl(context):
    # list of contacts
    First_contact = "name of your friend"
    Second_contact = "name of your friend"
    Third_contact = "name of your friend"

    contacts = [First_contact, Second_contact, Third_contact]

    # finding the elements of search bar
    search_input = context.driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
    # choose the second parameter in the contact list
    search_input.send_keys(contacts[0])


time.sleep(5)


@when('select specific friend')
def step_impl(context):
    # Effective clicks the first matching contact in the list
    click_second_contact = context.driver.find_element(By.CSS_SELECTOR, 'li[id="id of your friend"]')
    click_second_contact.click()
    time.sleep(2)


time.sleep(5)


@when('write message and send')
def step_impl(context):
    # writing a  message
    message = "Hi how are you today?"
    write_message = context.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Message"]')
    write_message.send_keys(message)
    print('Message sent!')

    # send message
    time.sleep(9)
    send = context.driver.find_element(By.CSS_SELECTOR, 'svg[class="xsrhx6k"]')
    send.click()


@then('User must successfully login to homepage')
def step_impl(context):
    # going to logout
    print("Logging out...")
    out = context.driver.find_element(
        By.CSS_SELECTOR, 'div[aria-label="Settings, help and more"]')
    out.click()

    # logout
    logout = context.driver.find_elements(By.CSS_SELECTOR, "div[role='menuitem']")[-1]
    logout.click()
    time.sleep(8)