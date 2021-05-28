from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
from os import remove
# import pyperclip -> Used for copying to clipboard

#setting up
message = "Hello world"
filename = "Calllog.csv"

#Fetching data from CSV
rows = []
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.DictReader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

finalListofNumbers = []
for row in rows:
    if(row['Type'] == 'Missed'):
        finalListofNumbers.append(row['Phone'])
    elif (row['Phone'] in finalListofNumbers):
        finalListofNumbers.remove(row['Phone'])

print(finalListofNumbers)

#Send messages to numbers in 'finalListofNumbers'
driver = webdriver.Chrome('./chromedriver')
finalListofNumbers = ['+919400419216', '+919497072620']
for phoneNumber in finalListofNumbers:
    # urlLink = "https://wa.me/"+phoneNumber+"/?text="+message #Original API
    print("setting URL")
    urlLink = "https://web.whatsapp.com/send?phone=" + \
        phoneNumber+"&text="+message+"&app_absent=0"

    # Start: Copy the created API URL to clipboard
    # pyperclip.copy(urlLink)
    # a = int(input("Send to"+phoneNumber+"Continue?"))
    # End: Copy the created API URL to clipboard
    print("opening page")
    driver.implicitly_wait(10)
    driver.get(urlLink)
    print("Waiting for message to load")
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='_3-8er selectable-text copyable-text']/span"))
    )
    print("wait completed")
    try:
        print("In try")
        if(driver.find_element_by_xpath("//span[@class='_3-8er selectable-text copyable-text']/span").text):
            print("In if check")
            driver.find_element_by_xpath("//button[@class='_1E0Oz']").click()
            print("click completed")
    except:
        print("Exception catched")
