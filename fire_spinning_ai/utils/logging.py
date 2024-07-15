import logging

def setup_logger(name, log_file, level=logging.INFO):
    """
    Setup a logger.

    Args:
        name (str): Name of the logger.
        log_file (str): File path to save the log.
        level (int): Logging level.

    Returns:
        logging.Logger: Configured logger.
    """
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def log_message(logger, message, level=logging.INFO):
    """
    Log a message.

    Args:
        logger (logging.Logger): Logger instance.
        message (str): Message to log.
        level (int): Logging level.

    Returns:
        None
    """
    if level == logging.DEBUG:
        logger.debug(message)
    elif level == logging.INFO:
        logger.info(message)
    elif level == logging.WARNING:
        logger.warning(message)
    elif level == logging.ERROR:
        logger.error(message)
    elif level == logging.CRITICAL:
        logger.critical(message)
