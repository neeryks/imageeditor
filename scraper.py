from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



#os.environ['PATH'] += r"/Users/akashdeepsingh/Documents/mpro/imageeditor/mediaasset"
driver = webdriver.Safari()
driver.get("https://in-the-sky.org/skymap2.php?no_cookie=1&latitude=19.07&longitude=72.88&timezone=5.50&year=2022&month=8&day=27&hour=13&min=46&PLlimitmag=0&zoom=160&ra=11.82811&dec=19.07283")
driver.implicitly_wait(5)
ele1 = driver.find_element(By.CLASS_NAME,"chksn")
ele2 = driver.find_element(By.CLASS_NAME,"chksp")
ele3 = driver.find_element(By.CLASS_NAME,"chklp")
ele4 = driver.find_element(By.CLASS_NAME,"pl-export-y")
ele5 = driver.find_element(By.CLASS_NAME,"pl-export-x")
ele6 = Select(driver.find_element(By.CLASS_NAME,"pl_colors"))
ele7 = driver.find_element(By.CLASS_NAME,"pl-svg")


ele1.click()
ele2.click()
ele3.click()
ele4.send_keys("1000")
ele5.send_keys("1000")
ele6.select_by_value("5")
ele7.click()
time.sleep(5)
driver.quit()







