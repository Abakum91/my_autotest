import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(20)
# Тест -Добавление комментария
# driver.execute_script("window.scrollBy(0, 100);")
# driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/ul/li/a/h3").click()
# driver.find_element_by_css_selector("#content>div>:nth-child(3)>ul>:nth-child(2)>a").click()
# driver.find_element_by_css_selector("#commentform>:nth-child(2)>p>span>:nth-child(5)").click()
# comment = driver.find_element_by_id("comment")
# comment.send_keys("Nice book!")
# author = driver.find_element_by_id("author")
# author.send_keys("Alexey")
# email = driver.find_element_by_id("email")
# email.send_keys("ramzy91@yandex.ru")
# driver.find_element_by_id("submit").click()
# driver.quit()