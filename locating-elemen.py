from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.tokopedia.com/login")
driver.find_element(By.ID, "input")

input("Tekan enter apabila keluar dari chrome")

driver.quit()