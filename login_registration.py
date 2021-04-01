import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(20)
# ТЕСТ - Регистрация аккаунта
# driver.find_element_by_id("menu-item-50").click()
# email = driver.find_element_by_id("reg_email")
# email.send_keys("ramzy91@yandex.ru")
# regpassword = driver.find_element_by_id("reg_password")
# regpassword.send_keys("ABAKUMOV1234567890")
# driver.find_element_by_name("register").click()
# driver.quit()
# ТЕСТ - Логин в систему
# driver.find_element_by_id("menu-item-50").click()
# username = driver.find_element_by_id("username")
# username.send_keys("ramzy91@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("ABAKUMOV1234567890")
# driver.find_element_by_name("login").click()
# logout_btn_text = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-36>div>div>nav>ul>:nth-child(6)>a"), "Logout"))
# driver.quit()