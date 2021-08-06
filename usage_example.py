# this is how the basic code should look when importing the element_search script
# so it's practically a usage example

# important note:
# you should already have selenium installed
# along with the specific driver for your platform and web browser
# refer to  https://selenium-python.readthedocs.io/installation.html  for help with that

import element_search as es
from selenium import webdriver

# example of how to use the log_event() function:
# pass a string argument with whatever you want to write into the log
# the log filename defaults to log.txt unless otherwise specified
# if the file doesn't exist, it will be created,
# it will add a line with the timestamp and specified string
# also printing in the terminal what is sent to the log file
es.log_event('Starting session !')

# side hint:
# when defining the driver, if using Chrome and you get the following error:
# 'Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)'
# add to your code this option tweak when defining the driver:
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# we'll use as example the selenium web page
driver.get('https://www.selenium.dev/')

# using the test_for_xpath() function with minimum preferred arguments
logo = es.search_element(driver, '//*[@id="header"]/a[1]/img[1]', 'logo-icon')
print(logo)
# logo is now a selenium webelement object that is clickable and whatnot
# and there is now a log.txt file containing the results of the search with timestamps

es.log_event('Session End \n')
# since all logs will continue to be written in the same file,
# preferably finnish the last log_event with a new line at the end as a session separator
# so the file is more readable