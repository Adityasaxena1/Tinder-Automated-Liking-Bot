from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys  import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

time.sleep(5)

base_window = driver.window_handles[0]
login = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(2)


more_options = driver.find_element(By.XPATH, value="/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button")
more_options.click()
time.sleep(2)


try:
    fb_login = driver.find_element(By.XPATH, value="/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button")
    fb_login.click()
    time.sleep(2)
except:
        cut = driver.find_element(By.XPATH, value="/html/body/div[2]/main/div/div[2]/button/svg/path")
        cut.click()
        time.sleep(2)
        login = driver.find_element(By.XPATH,
                                    value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login.click()
        time.sleep(2)

        more_options = driver.find_element(By.XPATH,
                                           value="/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button")
        more_options.click()
        time.sleep(2)


#FB LOGIN
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(2)
email_input = driver.find_element(By.XPATH, value='/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_input.send_keys(YOUR_MAIL_ID)
time.sleep(2)
pass_input = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
pass_input.send_keys(YOUR_PASSWORD)
time.sleep(2)
login_button = driver.find_element(By.ID, value="loginbutton")
login_button.click()


time.sleep(5)


#TINDER
driver.switch_to.window(base_window)
print(driver.title)

allow_cookies = driver.find_element(By.XPATH, value="/html/body/div[2]/main/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
allow_cookies.click()

time.sleep(2)

location_access = driver.find_element(By.XPATH, value="/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
location_access.click()
time.sleep(2)

allow_notification = driver.find_element(By.XPATH, value="/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]")
allow_notification.click()
time.sleep(2)

like_button = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span")
like_button.click()


#TINDER SWIPE

time.sleep(5)
like = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span/svg")
like.click()























