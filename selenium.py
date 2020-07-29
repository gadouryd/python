from selenium import webdriver
import time

path = r'/path/to/chromedriver'
browser = webdriver.Chrome(executable_path = path)

url = 'http://example.com'
browser.get(url)

browser.find_element_by_xpath("//input[@autocomplete='username']").send_keys(username)
browser.find_element_by_xpath("//input[@autocomplete='current-password']").send_keys(password)
browser.find_element_by_xpath("//button[@data-component-name='v-form__BaseButton-log-in']").click()
s_cookies = browser.get_cookies()


time.sleep(15)
browser.quit()
