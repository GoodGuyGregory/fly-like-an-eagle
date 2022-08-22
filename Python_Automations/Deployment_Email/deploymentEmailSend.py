from selenium import webdriver

driver = webdriver.Chrome("C:\chromedriver.exe")

driver.maximize_window()

#  site url for gitea
driver.get("http://cis2319papp:3000/issues?type=assigned&repo=0&sort=&state=open")

# id attribute for site user_name
#  id attribute for password

# driver.find_element_by_id("user_name").send_keys(username)
# driver.find_element_by_id("password").send_keys(password)
# driver.find_element_by_css_class("ui green button").click()

username = 'greg.witt@avnet.com'
password = 'goodguyg23g'
driver.find_element('id', 'user_name').send_keys(username)
driver.find_element('id', 'password').send_keys(password)
