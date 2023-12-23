import logging


def ini_logger():
    logger = logging.getLogger('Filarmonic')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s] [%(name)s/%(module)s] [%(levelname)s] : %(message)s')

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    #fh = logging.FileHandler(FileUtils.get_new_session_log_file())
    #fh.setLevel(logging.DEBUG)
    #fh.setFormatter(formatter)

    #logger.addHandler(fh)
    logger.addHandler(ch)