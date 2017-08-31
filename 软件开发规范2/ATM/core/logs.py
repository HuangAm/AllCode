import logging

def get_logger():
    logger=logging.getLogger()
    fh=logging.FileHandler("test.log")
    ch=logging.S