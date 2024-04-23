import logging

def setup_logger():
    # Create a custom logger
    logger = logging.getLogger('OpenWormLogger')
    logger.setLevel(logging.DEBUG)  # Set minimum log level to DEBUG

    # Create handlers for both file and console
    f_handler = logging.FileHandler('openworm.log')
    c_handler = logging.StreamHandler()

    # Set level for handlers
    f_handler.setLevel(logging.DEBUG)  # File handler logs everything
    c_handler.setLevel(logging.INFO)   # Console only logs INFO and above

    # Create formatters and add them to handlers
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

    f_handler.setFormatter(f_format)
    c_handler.setFormatter(c_format)

    # Add handlers to the logger
    logger.addHandler(f_handler)
    logger.addHandler(c_handler)

    return logger

def main():
    logger = setup_logger()
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

if __name__ == "__main__":
    main()

