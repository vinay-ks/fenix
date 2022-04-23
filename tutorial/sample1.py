from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://github.com/golang/go")
l = driver.find_elements_by_css_selector("h2.h4.mb-3")
print("Used by:" +l[4].text)

