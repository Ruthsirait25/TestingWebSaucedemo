from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = "https://www.saucedemo.com/"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5) 

def login(username, password):
    driver.get(url)
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def get_error_message():
    try:
        error_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        return error_element.text.strip()
    except:
        return None

print("Test Case 1: Login dengan kredensial benar")
login("standard_user", "secret_sauce")
if "inventory" in driver.current_url:
    print("PASS: Login berhasil")
else:
    print("FAIL: Login gagal")
time.sleep(1)

print("\nTest Case 2: Login dengan password salah")
login("standard_user", "wrong_password")
error_message = get_error_message()
print(f"[DEBUG] Pesan error: {error_message}")
if error_message and "do not match any user" in error_message.lower():
    print("PASS: Error message muncul")
else:
    print("FAIL: Tidak ada atau salah error message")
time.sleep(1)

def get_error_message():
    try:
        error_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        )
        return error_element.text.strip()
    except Exception as e:
        print(f"[DEBUG] Tidak ada error message: {e}")
        return None

print("\nTest Case 3: Login tanpa username")
login("", "secret_sauce")

time.sleep(0.5)

error_message = get_error_message()
print(f"[DEBUG] Pesan error: {error_message}")
if error_message and "username is required" in error_message.lower():
    print("PASS: Error message muncul")
else:
    print("FAIL: Tidak ada atau salah error message")

driver.quit()