import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SHOW_BROWSER = True  
STEP_DELAY = 1.5       

chromedriver_autoinstaller.install()

chrome_options = Options()
if not SHOW_BROWSER:
    chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)  
wait = WebDriverWait(driver, 5)

url = "https://www.saucedemo.com/"

def pause():
    time.sleep(STEP_DELAY)

def login(username, password):
    driver.get(url)
    pause()
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    pause()
    driver.find_element(By.ID, "password").send_keys(password)
    pause()
    driver.find_element(By.ID, "login-button").click()
    pause()

print("Step 1: Login ke SauceDemo")
login("standard_user", "secret_sauce")
if "inventory" in driver.current_url:
    print("PASS: Login berhasil")
else:
    print("FAIL: Login gagal")
    driver.quit()
    exit()

print("\nTest Case 1: Produk tampil di halaman")
products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
pause()
if len(products) > 0:
    print(f"PASS: Ada {len(products)} produk yang tampil")
else:
    print("FAIL: Tidak ada produk ditemukan")

print("\nTest Case 2: Tambah produk ke keranjang")
first_add_button = driver.find_element(By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")
first_add_button.click()
pause()
cart_badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
if cart_badge.text == "1":
    print("PASS: Produk berhasil ditambahkan ke keranjang")
else:
    print("FAIL: Produk tidak masuk ke keranjang")

print("\nTest Case 3: Hapus produk dari keranjang")
remove_button = driver.find_element(By.XPATH, "(//button[contains(text(),'Remove')])[1]")
remove_button.click()
pause()
cart_badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
if len(cart_badges) == 0:
    print("PASS: Produk berhasil dihapus dari keranjang")
else:
    print("FAIL: Produk masih ada di keranjang")

print("\nTest Case 4: Buka detail produk")
product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
pause()
driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
pause()
detail_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name"))).text
if product_name == detail_name:
    print("PASS: Nama produk di detail sesuai")
else:
    print("FAIL: Nama produk di detail tidak sesuai")

driver.quit()
print("\nTesting selesai.")