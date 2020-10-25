import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
import anotherone

logging.debug('Debug Message')
logging.info('Info Message')
logging.warning('Warning Message')
logging.error('Error Message')
logging.critical('Critical Message')

# Todo: Look more into logger before 28th Sept
