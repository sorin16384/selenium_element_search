import time
import datetime


def log_event(event, logfile='log.txt'):
    """

    :param event: what should be logged
    :type event: str
    :param logfile: the name(and path) of the log file ( default: 'log.txt')
    :type logfile: str
    :return: True if everything went ok,
             False if an error occurred
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


def test_for_xpath(driver, element, element_name='', check_once=True, continuous=False, timeout=30, logfile='log.txt'):
    elem = None
    element_name = element if element_name == '' else element_name
    t = 0
    err = -1
    log_event(f"Testing for '{element_name}' xpath")
    while (check_once or continuous) and t < timeout:
        try:
            t += 1
            print(f"searching for '{element}' xpath...")
            time.sleep(1)
            elem = driver.find_element_by_xpath(element)
            # if the driver fails to find the element, this results in error, so except: executes
            print('Found it')
            log_event(f"Found '{element_name}' xpath", logfile)
            break
        except Exception as e:
            err = e
            if continuous:
                print(f'looking for {timeout - t} more times:\n{e}')
            # not to repeat if only once was desired
            if check_once:
                #print(f"'{element_name}' not present")
                log_event(f"'{element_name}' not present", logfile)
                check_once = False

    if t == timeout and elem is None:
        print(f"Time Out !!!\nCouldn't find {element_name}")
        log_event(
            f"Timeout, fail to find '{element_name}': {err if err else 'Unknown Reason'}", logfile)
        # probably there will always be a reason , so that might disappear
        # but will leave it for now

    return elem


def main():
    # this is how the basic code should look when importing this script
    # so it's practically a usage example
    # obviously you can import only certain functions or the whole thing with  import element_search
    # for functionality and demonstration purposes, here I'll use as example the  from *** import ***
    # in your code the import should be uncommented

    # important note:
    # you should already have selenium installed
    # along with the specific driver for your platform and web browser
    # refer to  https://selenium-python.readthedocs.io/installation.html  for help with that

    #from element_search import log_event
    from selenium import webdriver

    # example of how to use the log_event() function
    # pass a string argument with whatever you want to write into the log
    # the log filename defaults to log.txt unless otherwise specified
    log_event('if there is no log.txt, create it, if it exists, add this line in it')

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


if __name__ == '__main__':
    main()
