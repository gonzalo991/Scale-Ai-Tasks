import logging

# Log an exception
try:
    # Create a logger and set the log level to "DEBUG" and add a handler to log into a file
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [ %(filename)s: %(lineno)s ] - %(message)s', handlers=[logging.FileHandler("file_log.log"), logging.StreamHandler()])

    # Log a message with a custom format and extra information
    logging.info('Hello, %(name)s!', extra={'name': 'Alice'})

    # Log a message with a custom severity level
    logging.log(10, 'This is a custom severity level!')

    # Log an error
    logging.error('An error occurred!')

    # Log a critical message
    logging.critical('This is a critical message!')

    # Log a debug message
    logging.debug('This is a debug message!')

    # Log a warning
    logging.warning('Be careful!')


    # Log a critical message
    logging.critical('This is a critical message!')

except Exception as e:
    # Log the exception
    logging.error('An exception occurred: %s', e)
