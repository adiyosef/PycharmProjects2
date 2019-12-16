from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path="/Users/adi.y/PycharmProjects/devexp/webdriver/chromedriver")
#
# # 1 a
# driver.get("http://www.walla.co.il")
# #
# # 1 b
#driver_firefox = webdriver.Firefox(executable_path="/Users/adi.y/PycharmProjects/devexp/webdriver/geckodriver")
#driver_firefox.get("http://www.ynet.co.il")
#
# # 2
# driver.get("http://www.walla.co.il")
# title = driver.title
# driver.refresh()
# if(title==driver.title):
#     print("title is the same")
#
# # 3
# yes
#
# # 4
# driver.get("https://translate.google.com")
# textbox = driver.find_element_by_id("source")
# if textbox.is_displayed():
#     textbox.send_keys("תתרגם את זה")
#
# # 5
# driver.get("https://www.youtube.com")
# textbox = driver.find_element_by_id("search")
# search_button = driver.find_element_by_id("search-icon-legacy")
# if textbox.is_displayed():
#     textbox.send_keys("i need you armin van buuren & garibay feat. olaf blackwood live")
#     search_button.click()
#
# # 6
# driver.get("https://translate.google.com")
# textbox1 = driver.find_element_by_id("source")
# print(textbox1)
# textbox2 = driver.find_element_by_class_name("orig")
# print(textbox2)
# textbox3 = driver.find_element_by_xpath("//textarea[@autocorrect='off']")
# print(textbox3)
#
# # 7
# driver.get("https://www.facebook.com")
# email_box = driver.find_element_by_name("email")
# email_box.send_keys("****@****.***")
# password_box = driver.find_element_by_name("pass")
# password_box.send_keys("Aa123456")
# login = driver.find_element_by_xpath("//input[@value='Log In']")
# login.submit()
#
# # 8
# driver.get("http://www.walla.co.il")
# all_cookies = driver.get_cookies()
# print(all_cookies)
# driver.delete_all_cookies()
# all_cookies = driver.get_cookies()
# print(all_cookies)
#
# # 9
# driver.get("https://github.com")
# search_box = driver.find_element_by_name("q")
# search_box.send_keys("Selenium")
# search_box.send_keys(Keys.RETURN)

# 10
# ?

