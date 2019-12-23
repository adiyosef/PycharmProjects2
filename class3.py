from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "/Users/adi.y/PycharmProjects/devexp/webdriver/chromedriver")
driver.get("https://translate.google.co.il/")
print(driver.current_url)
print(driver.title)

# #print(driver.page_source)
# textbox = driver.find_element_by_id("source")
# if textbox.is_displayed():
#     textbox.click()
#     textbox.send_keys("hello")
# driver.find_element_by_xpath("//*[@autocorrect='off']")
# print(textbox.get_attribute("rows"))
elements = driver.find_elements_by_id("source")
elements[0].submit()
# driver.find_elements_by_id("123").send_keys(Keys.ENTER)
# print(len(elements))
# #driver.quit()
#
# driver = webdriver.Chrome(executable_path = "/Users/adi.y/PycharmProjects/devexp/webdriver/chromedriver")
# driver.get("https://gofile.io/?t=uploadFiles")
# driver.find_elements_by_id("divDragDrop").send_keys

