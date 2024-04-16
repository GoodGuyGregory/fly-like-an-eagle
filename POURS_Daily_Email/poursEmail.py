import win32com.client as win32
from selenium import webdriver
from getpass import getpass
import pyperclip as pyperclip
from datetime import datetime

# XPATH Detailed Hints : https://devhints.io/xpath

#  define the webdriver.
driver = webdriver.Chrome(
    r"C:\Users\058620\Chrome-Driver\chromedriver.exe")

driver.maximize_window()

driver.get("http://cis2319papp:3000/user/login?redirect_to=")

usernameResp = input('What is your Gitea Username? ')
passwordResp = getpass('enter your password? ')
driver.find_element('id', 'user_name').send_keys(usernameResp)
driver.find_element('id', 'password').send_keys(passwordResp)
driver.find_element(
    'xpath', "//button[@class='ui green button' and contains(text(),'Sign In')]").click()


#  navigate to the user's profile
driver.find_element('xpath', "//div[@class='right stackable menu']//div[@data-content='Profile and Settings…']").click()
driver.find_element('xpath',"//div[@class='right stackable menu']//div[@data-content='Profile and Settings…']//div//a[1]").click()
driver.find_element('xpath',"//div[@class='ui secondary stackable pointing menu']//a[2]").click()

# news feed component xPath
closedRecords = driver.find_elements('xpath', "//div[@class='news']//div//p")
pushRecords = driver.find_elements('xpath', "//div[@class='news']//div[@class='push news']//p")

dailyActivity = []

# pushed to a branch...

for record in closedRecords:
    if "hours ago" in record.text:
        dailyActivity.append(record.text)
    if "minutes ago" in record.text:
        dailyActivity.append(record.text)

# closed an issues etc... 

for record in pushRecords:
    if "hours ago" in record.text:
        dailyActivity.append(record.text)
    if "minutes ago" in record.text:
        dailyActivity.append(record.text)


# open a file and load a default greeting.
# add Dakota and the subject with the day

outlookApplication = win32.Dispatch('outlook.application')

message = outlookApplication.CreateItem(0)

message.To = 'karl.kuhn@avnet.com'
message.Cc = 'dakota.hall@avnet.com'
now = datetime.now()
dayMonth = now.strftime("%m/%d")

message.Subject = 'POURS Daily ' + dayMonth

message.Body = "Evening Karl, \n\nToday I worked on the following tasks:\n"

for activity in dailyActivity:
    message.Body += "* " + activity + "\n"

# Sign the email as Greg. and ensure it is sent to the Drafts folder of Outlook
message.Body += '\n\nLet me know if you have any questions,\n\nGreg'
# saves as a draft in outlook
message.save()


