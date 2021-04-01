import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(20)
# Тест - отображение страницы товара
# driver.find_element_by_id("menu-item-50").click()
# username = driver.find_element_by_id("username")
# username.send_keys("ramzy91@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("ABAKUMOV1234567890")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector("#content>ul>:nth-child(3)>a>a").click()
# head_book = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#product-181>:nth-child(2)>h1"), "HTML5 Forms"))
# Тест - количество товаров в категории
# driver.find_element_by_id("menu-item-50").click()
# username = driver.find_element_by_id("username")
# username.send_keys("ramzy91@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("ABAKUMOV1234567890")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# time.sleep(1)
# driver.find_element_by_css_selector("#woocommerce_product_categories-2>ul>:nth-child(2)>a").click()
# Тест - сортировка товара
# driver.find_element_by_id("menu-item-50").click()
# username = driver.find_element_by_id("username")
# username.send_keys("ramzy91@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("ABAKUMOV1234567890")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# time.sleep(1)
# default = driver.find_element_by_css_selector("#content>form>select")
# default_value = default.get_attribute("value")
# print("Сортировка по:", default_value)
# if default_value == 'menu_order':
#     print("Выбрана сортировка по умолчанию")
# else:
#     print(("Сортировка не по умолчанию"))
# driver.find_element_by_tag_name("select").click()
# driver.find_element_by_css_selector("option:nth-child(6)").click()
# high_to_low = driver.find_element_by_css_selector("#content>form>select")
# high_to_low_value = high_to_low.get_attribute("value")
# print("Сортировка по:", high_to_low_value)
# if high_to_low_value == 'price-desc':
#     print("Выбрана сортировка от большего к меньшему")
# else:
#     print(("Сортировка не от большего к меньшему"))
# Тест - отображение, скидка товара
# driver.find_element_by_id("menu-item-50").click()
# username = driver.find_element_by_id("username")
# username.send_keys("ramzy91@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("ABAKUMOV1234567890")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# time.sleep(1)
# driver.find_element_by_css_selector("#content>ul>:nth-child(1)>a>h3").click()
# old_price = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#product-169>:nth-child(3)>:nth-child(2)>p>del>span"), "₹600.00"))
# new_price = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#product-169>:nth-child(3)>:nth-child(2)>p>ins>span"), "₹450.00"))
# time.sleep(2)
# picture = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-169>:nth-child(2)>a>img")))
# picture.click()
# time.sleep(2)
# close = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div[2]/div[3]/a")))
# close.click()
# Тест - проверка цены в корзине
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[6]/a[2]").click()
# item = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#main-nav>:nth-child(6)>a>:nth-child(2)"), "1 Item"))
# price = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#main-nav>:nth-child(6)>a>:nth-child(3)"), "₹350.00"))
# driver.find_element_by_css_selector("#main-nav>:nth-child(6)>a").click()
# price1 = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34>div>:nth-child(1)>div>div>table>tbody>:nth-child(1)>td>span"), "350.00"))
# price2 = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34>div>:nth-child(1)>div>div>table>tbody>:nth-child(3)>td>strong>span"), "367.50"))
# Тест - работа в корзине
# driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[6]/a[2]").click()
# time.sleep(1)
# driver.find_element_by_css_selector("#main-nav>:nth-child(6)>a").click()
# time.sleep(2)
# driver.find_element_by_css_selector("#page-34>div>:nth-child(1)>form>table>tbody>:nth-child(1)>:nth-child(1)>a").click()
# driver.find_element_by_css_selector("#page-34>div>:nth-child(1)>a").click()
# item = driver.find_element_by_css_selector("#page-34>div>:nth-child(1)>form>table>tbody>:nth-child(1)>:nth-child(5)>div>input").clear()
# item1 = driver.find_element_by_css_selector("#page-34>div>:nth-child(1)>form>table>tbody>:nth-child(1)>:nth-child(5)>div>input")
# item1.send_keys("3")
# driver.find_element_by_css_selector("#page-34>div>:nth-child(1)>form>table>tbody>:nth-child(2)>td>:nth-child(2)").click()
# time.sleep(2)
# element = driver.find_element_by_css_selector('[value="3"]')
# element_text = element.text
# assert element_text == "3"
# time.sleep(1)
# driver.find_element_by_css_selector('[value="Apply Coupon"]').click()
# coupon = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34>div>:nth-child(1)>ul>li"), "Please enter a coupon code."))
# Тест - покупка товара
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[6]/a[2]").click()
time.sleep(1)
driver.find_element_by_css_selector("#main-nav>:nth-child(6)>a").click()
checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-34>div>:nth-child(1)>div>div>div>a")))
checkout.click()
first_name = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35>div>:nth-child(1)>:nth-child(5)>:nth-child(1)>:nth-child(1)>div>:nth-child(2)>label"), "First Name"))
first_name1 = driver.find_element_by_id("billing_first_name")
first_name1.send_keys("Alexey")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Abakumov")
time.sleep(1)
email = driver.find_element_by_id("billing_email")
email.send_keys("ramzy91@yandex.ru")
time.sleep(1)
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("123456789")
time.sleep(1)
driver.find_element_by_id("select2-chosen-1").click()
country = driver.find_element_by_css_selector("#select2-drop>div>input")
country.send_keys("Russia")
driver.find_element_by_css_selector("[class='select2-result-label']").click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Svoboda")
town = driver.find_element_by_id("billing_city")
town.send_keys("Moscow")
state = driver.find_element_by_id("billing_state")
state.send_keys("MO")
post = driver.find_element_by_id("billing_postcode")
post.send_keys("123456")
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_id("payment_method_cheque").click()
driver.find_element_by_id("place_order").click()
thank = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35>div>:nth-child(1)>:nth-child(1)"), "Thank you. Your order has been received."))
check = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35>div>:nth-child(1)>table>tfoot>:nth-child(3)>td"), "Check Payments"))