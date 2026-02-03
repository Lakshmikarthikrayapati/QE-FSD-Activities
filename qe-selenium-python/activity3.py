from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/login-form")
    print(driver.title)
    driver.find_element(By.xpath("//input[@id = 'username']")).sendKeys("admin")
    driver.find_element(By.xpath("//input[@id = 'password']")).sendKeys("password")
    driver.find_element(By.xpath("//button[@class = 'svelte-1pdjkmx']")).click()
    driver.quit()