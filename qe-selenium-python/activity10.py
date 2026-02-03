from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/drag-drop")
    print(driver.title)
    actions = webdriver.ActionChains(driver)
    print("Title of the page: " + driver.title)

    ballelement = driver.find_element(By.CSS_SELECTOR,"#ball")
    dropzone1 = driver.find_element(By.ID, "dropzone1")
    dropzone2 = driver.find_element(By.ID, "dropzone2")

    text = driver.find_element(By.XPATH,"//div[@id=\"dropzone1\"]/span").text
    actions.drag_and_drop(ballelement, dropzone1).perform()

    if text=="Dropped!":
        print("Ball entered dropzone1")

    actions.drag_and_drop(ballelement, dropzone2).perform()

    if (driver.find_element(By.XPATH,("//div[@id=\"dropzone1\"]/span")).text) == "Dropped!":
         print("Ball entered dropzone2")