'''
handle all the logging works
'''

import logging
from conf import setting

def logger(log_type):

    #create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(setting.LOG_LEVEL)


    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(setting.LOG_LEVEL)

    # create file handler and set level to warning
    log_file = setting.LOG_TYPES[log_type]
    fh = logging.FileHandler(log_file)
    fh.setLevel(setting.LOG_LEVEL)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
    # 'application' code
    '''logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')'''