#!/usr/bin/env python3

import argparse

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def search(serialNumber):
    #Change to executable path of your driver
    service = Service(executable_path = "./chromedriver") 

    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://pcsupport.lenovo.com/us/en/warranty-lookup#/")

    try:
        # Search Serial Number
        input_element = driver.find_element(By.CLASS_NAME, "button-placeholder__input")
        input_element.clear()
        input_element.send_keys(serialNumber + Keys.ENTER)
    except Exception as e:
        print("Unable to search Serial Number")

        # Obtain all info on first page
    try:
        endDate = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app-psp-warranty']/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[5]/span[2]"))
        ).text
    except Exception as e:
        print("Unable to find end date")
    try:
        onSite = driver.find_element(By.XPATH, "//*[@id='app-psp-warranty']/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[6]/span[2]").text
    except Exception as e:
        print("Unable to find the type (on site?)")
    try:
        startDate = driver.find_element(By.XPATH, "//*[@id='app-psp-warranty']/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/span[2]").text
    except Exception as e:
        print("Unable to find the start date")
    try:
        warrantyType = driver.find_element(By.CLASS_NAME, "title-content").text
    except Exception as e:
        print("Unable to find the warranty type")
    try:
        model = driver.find_element(By.CLASS_NAME, "prod-name").text
    except Exception as e:
        print("Unable to find the model")

        # Click Product Home
    try:
        productHome = driver.find_element(By.XPATH, "/html/body/div[2]/section[2]/div[1]/div[3]/ul/li[1]/a/span[2]")
        productHome.click();
    except Exception as e:
        print("Failed to click Product Home")

    try:
        # Click View to obtain info about device
        viewButton = WebDriverWait(driver, 10).until (
            EC.presence_of_all_elements_located((By.CLASS_NAME, "new-other-info-right"))
        )
        for view in viewButton:
            if view.text == "View":
                view.click()
                break;
    except Exception as e:
        print("Failed to click view")
        
    try:
        configName = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "desc-config-name"))
        )
    except Exception as e:
        print("Unable to find the config name")

    try:
        configDetail = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "desc-config-detail"))
        )
    except Exception as e:
        print("Unable to find the config details")

    print()
    print("====================================================================")
    print("DEVICE INFO")
    print("Serial #:", serialNumber.upper())
    print("Model:", model)
    print()

    print("WARRANTY INFO")
    print("Warranty:", warrantyType, "-", onSite)
    print("Start Date:", startDate)
    print("End Date:", endDate)
    print()

    print("SPEC INFO")
    for name, detail in zip(configName, configDetail):
        if (name.text != '' or detail.text != ''):
            print(f"{name.text}: {detail.text}")
    print("====================================================================")
    print()
    driver.quit()

def main():
    parser = argparse.ArgumentParser(description = "Search for Lenovo device information by serial number")
    parser.add_argument("serial_number", type=str, help="The serial number of the Lenovo device.")
    args = parser.parse_args()

    if len(vars(args)) != 1:
        parser.error("Please only pass in the serial number")

    search(args.serial_number)

if __name__ == '__main__':
    main()