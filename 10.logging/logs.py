import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('Debug Message')
logging.info('Info Message')
logging.warning('Warning Message')
logging.error('Error Message')
logging.critical('Critical Message')

import anotherone

try:
    num = 1 / 0
except Exception as e:
    logging.error(e, exc_info=True)
