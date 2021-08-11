import time
import datetime

# to make the script actually return recognisable webelement,
# we have to import webdriver from selenium and initiate a driver
from selenium import webdriver

# and then assign a default driver, does not matter for what it is as it will not actually be used
# the only problem is that this will open a webdriver instance that takes memory and processing for a moment...
# so this might disappear
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.close()


def log_event(event, logfile='log.txt'):
    """
    Parameters:
        event (str): what should be logged

        logfile (str): (optional) the name(and path) of the log file ( default: 'log.txt')

    Returns:
            bool : True if everything went ok, False if something went wrong (such as creating file or writing to it)

    This function will write an event (what happened) to a file with timestamp, while also printing in the terminal what
    is being written.\n
    The function will write in the specified logfile, otherwise will create and/or write to a generic default log.txt file. Obviously
    any extension can be used (e.g.   .log,  .md,   .you_name_it)


    Usage Example: \n
    log_event('clicked login button', 'log_amazon_dot_com.txt')
    """
    time_now = (str(datetime.datetime.now())[:22])
    try:
        with open(logfile, 'a') as f:
            f.write(f'{time_now} {event}\n')
            print(f'Log :{time_now} {event}')
        return True
    except Exception as e:
        print(f'Log Error:{event}\n {e}')
        return False


def search_element(by, driver=driver, element='/html/body', element_name='', check_once=True, continuous=False,
                   timeout=30,
                   logfile='log.txt'):
    """ This function will search *by the method specified, with the passed *driver, the specified *element once or
    *continuous with one second break for the number of times specified in the *timeout
    while writing in the *logfile (by calling the log_event() function) the fact that the search started and
    the outcome of the search (if the element was found or not, in the second case, adding the reason)

    When searching repeatedly, the logfile will receive only the final result, and not all the tries, even though
    they will be printed in the terminal to let you know what the function is currently doing and why


    Parameters:
            by (str) : by what method the search will be done (options are: xpath, id, name, tag_name, css_selector,
                class, link_text, partial_link_text

            driver () : the selenium webdriver you are using for automation

            element (str) : the web element that you are looking for (e.g. '//*[@id="header"]/a[1]/img[1]')

            element_name (str) : an alias for the web element (e.g. 'logo_button' )

            check_once (bool) : whether to check once or not

            continuous (bool) : whether to check continuously or not (overrides check_once)

            timeout (int) : the number of times (with one second wait time) the element should be looked for when
                searching continuous

            logfile (str) : the log file that you want the log to be written in (defaults to 'log.txt' )

    Returns:
        WebElement if the element is found, otherwise, returns None
    """
    elem = None
    element_name = element if element_name == '' else element_name
    t = 0
    err = -1
    log_event(f"Testing for '{element_name}' {by}")
    while (check_once or continuous) and t < timeout:
        try:
            t += 1
            print(f"searching for '{element}' {by}...")
            time.sleep(1)
            if by == 'xpath':
                elem = driver.find_element_by_xpath(element)
            elif by == 'id':
                elem = driver.find_element_by_id(element)
            elif by == 'name':
                elem = driver.find_element_by_name(element)
            elif by == 'tag_name':
                elem = driver.find_element_by_tag_name(element)
            elif by == 'css_selector':
                elem = driver.find_element_by_css_selector(element)
            elif by == 'class':
                elem = driver.find_element_by_class_name(element)
            elif by == 'link_text':
                elem = driver.find_elements_by_link_text(element)
            elif by == 'partial_link_text':
                elem = driver.find_element_by_partial_link_text(element)
            else:
                raise RuntimeError("Wait a minute you, that's no means I can search the element by!")
            # if the driver fails to find the element, this results in error, so except: executes
            print('Found it')
            log_event(f"Found '{element_name}' {by}", logfile)
            break
        except Exception as e:
            err = e
            if continuous:
                print(f'looking for {timeout - t} more times:\n{e}')

            # in case no match for the means were found , raise an error and provide tips
            if "Wait a minute you" in str(e):
                raise RuntimeError("That's no means I can search the element by: '{}'\n"
                                   "options are : "
                                   "xpath, id, name, tag_name, css_selector, "
                                   "class, link_text, partial_link_text \n"
                                   "Check thy spelling or something... make it work !".format(by))

            # not to repeat if only once was desired
            if check_once:
                # print(f"'{element_name}' not present")
                log_event(f"'{element_name}' not present", logfile)
                check_once = False

    if t == timeout and elem is None:
        print(f"Time Out !!!\nCouldn't find {element_name}")
        log_event(
            f"Timeout, fail to find '{element_name}': {err if err else 'Unknown Reason'}", logfile)
        # probably there will always be a reason , so that might disappear
        # but will leave it for now

    return elem


def search_by_xpath(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt'):
    """ This function will search by xpath, with the passed *driver, the specified *element once or
        *continuous with one second break for the number of times specified in the *timeout
        while writing in the *logfile (by calling the log_event() function) the fact that the search started and
        the outcome of the search (if the element was found or not, in the second case, adding the reason)

        When searching repeatedly, the logfile will receive only the final result, and not all the tries, even though
        they will be printed in the terminal to let you know what the function is currently doing and why


        Parameters:

                driver () : the selenium webdriver you are using for automation

                element (str) : the web element that you are looking for (e.g. '//*[@id="header"]/a[1]/img[1]')

                element_name (str) : an alias for the web element (e.g. 'logo_button' )

                check_once (bool) : whether to check once or not

                continuous (bool) : whether to check continuously or not (overrides check_once)

                timeout (int) : the number of times (with one second wait time) the element should be looked for when
                    searching continuous

                logfile (str) : the log file that you want the log to be written in (defaults to 'log.txt' )

        Returns:
            WebElement if the element is found, otherwise, returns None
        """
    return search_element('xpath', driver, element, element_name=element_name, check_once=check_once,
                          continuous=continuous, timeout=timeout, logfile=logfile)


def search_by_id(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt'):
    """ This function will search by id, with the passed *driver, the specified *element once or
            *continuous with one second break for the number of times specified in the *timeout
            while writing in the *logfile (by calling the log_event() function) the fact that the search started and
            the outcome of the search (if the element was found or not, in the second case, adding the reason)

            When searching repeatedly, the logfile will receive only the final result, and not all the tries, even though
            they will be printed in the terminal to let you know what the function is currently doing and why


            Parameters:

                    driver () : the selenium webdriver you are using for automation

                    element (str) : the web element that you are looking for (e.g. '//*[@id="header"]/a[1]/img[1]')

                    element_name (str) : an alias for the web element (e.g. 'logo_button' )

                    check_once (bool) : whether to check once or not

                    continuous (bool) : whether to check continuously or not (overrides check_once)

                    timeout (int) : the number of times (with one second wait time) the element should be looked for when
                        searching continuous

                    logfile (str) : the log file that you want the log to be written in (defaults to 'log.txt' )

            Returns:
                WebElement if the element is found, otherwise, returns None
            """
    return search_element('id', driver, element, element_name=element_name, check_once=check_once,
                          continuous=continuous, timeout=timeout, logfile=logfile)


def search_by_name(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt'):
    """ This function will search by xpath, with the passed *driver, the specified *element once or
            *continuous with one second break for the number of times specified in the *timeout
            while writing in the *logfile (by calling the log_event() function) the fact that the search started and
            the outcome of the search (if the element was found or not, in the second case, adding the reason)

            When searching repeatedly, the logfile will receive only the final result, and not all the tries, even though
            they will be printed in the terminal to let you know what the function is currently doing and why


            Parameters:

                    driver () : the selenium webdriver you are using for automation

                    element (str) : the web element that you are looking for (e.g. '//*[@id="header"]/a[1]/img[1]')

                    element_name (str) : an alias for the web element (e.g. 'logo_button' )

                    check_once (bool) : whether to check once or not

                    continuous (bool) : whether to check continuously or not (overrides check_once)

                    timeout (int) : the number of times (with one second wait time) the element should be looked for when
                        searching continuous

                    logfile (str) : the log file that you want the log to be written in (defaults to 'log.txt' )

            Returns:
                WebElement if the element is found, otherwise, returns None
            """
    return search_element('name', driver, element, element_name=element_name, check_once=check_once,
                          continuous=continuous, timeout=timeout, logfile=logfile)


def search_by_tag_name(driver, element, element_name='', check_once=True, continuous=False, timeout=30,
                       logfile='log.txt'):
    """ This function will search by tag name, with the passed *driver, the specified *element once or
            *continuous with one second break for the number of times specified in the *timeout
            while writing in the *logfile (by calling the log_event() function) the fact that the search started and
            the outcome of the search (if the element was found or not, in the second case, adding the reason)

            When searching repeatedly, the logfile will receive only the final result, and not all the tries, even though
            they will be printed in the terminal to let you know what the function is currently doing and why


            Parameters:

                    driver () : the selenium webdriver you are using for automation

                    element (str) : the web element that you are looking for (e.g. '//*[@id="header"]/a[1]/img[1]')

                    element_name (str) : an alias for the web element (e.g. 'logo_button' )

                    check_once (bool) : whether to check once or not

                    continuous (bool) : whether to check continuously or not (overrides check_once)

                    timeout (int) : the number of times (with one second wait time) the element should be looked for when
                        searching continuous

                    logfile (str) : the log file that you want the log to be written in (defaults to 'log.txt' )

            Returns:
                WebElement if the element is found, otherwise, returns None
            """
    return search_element('tag_name', driver, element, element_name=element_name, check_once=check_once,
                          continuous=continuous, timeout=timeout, logfile=logfile)


def search_by_css_selector(driver, element, element_name='', check_once=True, continuous=False, timeout=30,
                           logfile='log.txt'):
    """ This function will search by css selector, with the passed *driver, the specified *element once or
            *continuous with one second break for the number of times specified in the *timeout
            while writing in the *logfile (by calling the log_event() function) the fact that the search started and
            the outcome of the search (if the element was found or not, in the second case, adding the reason)

            When searching repeatedly, the logfile will receive only the final result, and not all the tries, even though
            they will be printed in the terminal to let you know what the function is currently doing and why


            Parameters:

                    driver () : the selenium webdriver you are using for automation

                    element (str) : the web element that you are looking for (e.g. '//*[@id="header"]/a[1]/img[1]')

                    element_name (str) : an alias for the web element (e.g. 'logo_button' )

                    check_once (bool) : whether to check once or not

                    continuous (bool) : whether to check continuously or not (overrides check_once)

                    timeout (int) : the number of times (with one second wait time) the element should be looked for when
                        searching continuous

                    logfile (str) : the log file that you want the log to be written in (defaults to 'log.txt' )

            Returns:
                WebElement if the element is found, otherwise, returns None
            """
    return search_element('css_selector', driver, element, element_name=element_name, check_once=check_once,
                          continuous=continuous, timeout=timeout, logfile=logfile)


def search_by_class(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt'):
    return search_element('class', driver, element, element_name=element_name, check_once=check_once,
                          continuous=continuous, timeout=timeout, logfile=logfile)


def search_by_link_text(driver, element, element_name='', check_once=True, continuous=False, timeout=30,
                        logfile='log.txt'):
    return search_element('link_text', driver, element, element_name=element_name, check_once=check_once,
                          continuous=continuous, timeout=timeout, logfile=logfile)


def search_by_partial_link_text(driver, element, element_name='', check_once=True, continuous=False, timeout=30,
                                logfile='log.txt'):
    return search_element('partial_link_text', driver, element, element_name=element_name, check_once=check_once,
                          continuous=continuous, timeout=timeout, logfile=logfile)


if __name__ == '__main__':
    print('Refer to   usage_example.py   for usage examples ...')
