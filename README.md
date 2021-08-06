# selenium_element_search

Just to mention, I'm a beginner to all this, so it it's very possible to make some mistakes

The idea is to create a Python script that contains various functions,  that with the help of the Selenium library, searches for web elements, raising no errors,  and in the same time writes automatically into a log file what is being searched and if the element was found.


## Important note:
    * you should already have selenium installed
    * along with the specific driver for your platform and web browser

Refer to  [https://selenium-python.readthedocs.io/installation.html](https://selenium-python.readthedocs.io/installation.html)  for help with that

## Current functions:
    log_event(event, logfile='log.txt')
    search_element(by, driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt')
    search_by_id(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt')
    search_by_name(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt')
    search_by_tag_name(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt')
    search_by_css_selector(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt')
    search_by_class(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt')
    search_by_link_text(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt')
    search_by_partial_link_text(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt')
