import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

print("\nTest Case 5: Filter produk")


def pilih_filter(text):
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_visible_text(text)
    time.sleep(1)
    print(f"PASS: Filter {text} berhasil")

pilih_filter("Name (A to Z)")
pilih_filter("Name (Z to A)")
pilih_filter("Price (low to high)")
pilih_filter("Price (high to low)")


driver.quit()
