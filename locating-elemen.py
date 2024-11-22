from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.tokopedia.com/login")

input("Tekan enter apabila keluar dari chrome")

driver.quit()