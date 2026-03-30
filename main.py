import json
import time
import os
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://nova.otava.fi"
#url = "http://bot.sannysoft.com"
filename = "index.html"

options = Options()
options.headless = True
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

#options.add_argument("--headless=new")
options.add_argument("--use-subprocess")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)


stealth(driver,
        languages=["en-GB","en-US","en","fi"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Google Inc. (NVIDIA)",
        renderer="	ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 (0x00002504) Direct3D11 vs_5_0 ps_5_0, D3D11)",
        fix_hairline=True,
        )

driver.get(url)

def click(max, xpath):
    try:
        WebDriverWait(driver, timeout=max).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        driver.find_element(By.XPATH, xpath).click()
    except Exception as e:
        print(e)

time.sleep(1)
click(5, "//a[@href='login/student']")

time.sleep(1)
click(5, "//*[@id='main']/div/div[2]/div/ul/li[2]/button")

time.sleep(1)

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

with open(desktop+"/userdata.json", "r") as f:
    data = json.load(f)

username = data["username"]
password = data["password"]

email_input = driver.find_element(By.XPATH, "//input[@id='username']")
email_input.send_keys(username)

password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys(password)

time.sleep(1)

ActionChains(driver).send_keys(Keys.TAB, Keys.TAB, Keys.SPACE).perform()

time.sleep(1)
click(5, "//button[@id='login-btn']")

click(5, "//button[normalize-space(text())='Yes']")

time.sleep(1)

driver.get("https://nova.otava.fi/materials/own")

time.sleep(2)

with open("index.html", "w") as f: 
    f.write(
driver.find_element(By.XPATH, "//*[@id='main']/div/div/div/div[2]/div/div[2]/ul").get_attribute("innerHTML"))

input()

driver.quit()