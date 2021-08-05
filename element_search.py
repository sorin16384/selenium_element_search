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
