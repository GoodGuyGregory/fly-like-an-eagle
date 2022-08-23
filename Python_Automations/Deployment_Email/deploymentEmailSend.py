from selenium import webdriver
from datetime import datetime


def getTimeForGreeting():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

def getMilestoneIssue():
    milestoneRelease = input('what is the milestone number? ').upper()


    driver = webdriver.Chrome("C:\chromedriver.exe")

    driver.maximize_window()

    #  site url for gitea
    driver.get("http://cis2319papp:3000/issues?type=assigned&repo=0&sort=&state=open")

    # id attribute for site user_name
    #  id attribute for password

    # driver.find_element_by_id("user_name").send_keys(username)
    # driver.find_element_by_id("password").send_keys(password)
    # driver.find_element_by_css_class("ui green button").click()

    # Establish these in a KEY_ENV
    #  Login:
    username = ''
    password = ''
    driver.find_element('id', 'user_name').send_keys(username)
    driver.find_element('id', 'password').send_keys(password)
    driver.find_element(
        'xpath', "//button[@class='ui green button' and contains(text(),'Sign In')]").click()

    #  Find Release Milestone
    #  find the relevent place to click for POURS Milestone
    driver.get("http://cis2319papp:3000/Avnet/POURS/milestones")
    # get the latest milestone number

    driver.find_element(
        'xpath', f".//div[@class='milestone list']//child::li/a[contains(text(),'0.0.{milestoneRelease}')]").click()

    driver.find_element(
        'xpath', ".//div[@id='issue-filters']/div/div/a[@class='ui  basic button']").click()

    foundMilestoneIssues = []

    foundIssues = singleIssue = driver.find_elements('xpath', ".//div[@class='issue list']/li")

    for issue in foundIssues:
        foundMilestoneIssues.append(issue.text.split("\n")[0])
        
    print(foundMilestoneIssues)

def main():
    getTimeForGreeting()


main()